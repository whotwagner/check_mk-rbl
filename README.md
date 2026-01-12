> [!WARNING]  
> This repository has been moved to [https://codeberg.org/whotwagner/check_mk-rbl](https://codeberg.org/whotwagner/check_mk-rbl). Please visit the new location for the latest updates.

# check_mk-rbl

Check_mk-rbl is a simble rbl-check-plugin for check_mk. This plugin gathers all IPv4-adresses of a server and checks public adresses if they are listed on any blacklist.  

This project is a fork of [HeinleinSupports version](https://github.com/HeinleinSupport/check_mk).


## Requirements

* python-dnspython
* python-netifaces
* python-ipy    

## Install

### Using Check_MK Package

Clone the repo and install the Check_MK Package:
```
check_mk -vP install check_mk-rbl-1.0.mkp 
```

If you are using OMD, you need to become the user of your OMD environment before, (e.g. su - prod).

### Manually
Just copy the agent/plugin into /usr/lib/check_mk_agent/plugins/ of the check_mk-Agent  and the check-file into /opt/omd/versions/default/share/check_mk/checks/ of the check_mk-Server.


## Usage

The plugin checks if /etc/check_mk/check_rbl.ini exists and reads all dns-server. If the file doesn't exist or isn't readable, default-blacklists will be used. 

## Licence

GPL

## Author Information

Wolfgang Hotwagner [**(https://tech.feedyourhead.at/)**](https://tech.feedyourhead.at)
