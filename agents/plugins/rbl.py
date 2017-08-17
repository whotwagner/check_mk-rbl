#!/usr/bin/env python

# Required packages:
# 	python-dnspython
# 	python-netifaces
# 	python-ipy

import dns.resolver
import dns.exception
import re
import netifaces
from IPy import IP

class RBL:
	defaultbl = ["cbl.abuseat.org", "b.barracudacentral.org", "zen.spamhaus.org", "ix.dnsbl.manitu.net"]

	def __init__(self,inifile=None):
		self.inifile = inifile

	# this method reads a given ini-file and returns a list of dnsrb-server
	def readini(self):
		# if no inifile is set then simply return 
		if self.inifile == None:
			return
		arr = []
		try:
			file = open(self.inifile,"r")
		except Exception:
			# if the given inifile is not readable or doesn't exist return
			return

		comment = re.compile('^\s*[;#]')
		server = re.compile('^\s*server=.+')
		# read the ini-file
		for line in file:
			# leave out comments
			if comment.match(line):
				continue
			# if this is a server-line:
			if server.match(line):
				# ..parse the server-part
				back = re.search(r'\s*server=(.+)$',line)
				# ..and append it to the list
				arr.append(back.group(1).replace("\n",""))
		file.close()
		# return the list of dns-servers
		return arr
	
	# this method checks an ip against a dns-server
	def check(self,ip,dnsbl):
		revip = ".".join(reversed(ip.split('.')))
		data = False
		try:
			data = dns.resolver.query(revip + '.' + dnsbl + '.')
		except dns.exception.DNSException:
			pass

		if data:
			print ip, dnsbl, "found"
			return "found"
		else:
			print ip, dnsbl, "notfound"
			return "notfound"

	# run this method for checking
	def run(self,ip,dnsbl=[]):
		# if a dnsbl-list is given, use this instead
		if dnsbl:
			for d in dnsbl:
				self.check(ip,d)
			return
		# is it possible to read a inifile?
		arr = self.readini()
		if arr:
			# ..then use the inifile-entries
			for d in arr:
				self.check(ip,d)
		else:
			# ..otherwise use the default-list
			for d in self.defaultbl:
				self.check(ip,d)


# did we already set the banner?
banner = 0
# create RBL-Object with standard-rbl.ini
r = RBL("/etc/check_mk/check_rbl.ini")

# iterate through all interfaces
for interface in netifaces.interfaces():
	# get ipv4-entries
	if netifaces.AF_INET in netifaces.ifaddresses(interface):
		# get ip-adress
		for ip in map(lambda x: x['addr'], netifaces.ifaddresses(interface)[netifaces.AF_INET]):
			ipx = IP(ip)
			# Only run rbl-check if this is a public ip
			if ipx.iptype() == 'PUBLIC':
				if banner == 0:
					# if we didn't already print the banner:
					print '<<<rbl_check>>>'
					banner = 1
				# run dns-checks against the public ip
				r.run(ip)

