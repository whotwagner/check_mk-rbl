# check_mk-rbl

Check_mk-rbl is a simble rbl-check-plugin for check_mk. This plugin gathers all IPv4-adresses of a server and checks all public adresses if they are listed on any blacklist.  

This project is a fork of [HeinleinSupports version](https://github.com/HeinleinSupport/check_mk).

## Install

Just copy the agent/plugin into /usr/lib/check_mk_agent/plugins/ of the check_mk-Agent  and the check-file into /opt/omd/versions/default/share/check_mk/checks/ of the check_mk-Server.


## Usage

The plugin checks if /etc/check_mk/check_rbl.ini exists and reads all dns-server. If the file doesn't exist or isn't readable, default-blacklists will be used. 

## Licence

GPL

## Author Information

Wolfgang Hotwagner [**(https://tech.feedyourhead.at/)**](https://tech.feedyourhead.at)
