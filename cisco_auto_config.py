#!/usr/bin/python3
import os
import sys
from netmiko import ConnectHandler
from netmiko import Netmiko
import itertools
import paramiko
import time
from commands import *

original_stdout = sys.stdout

c_username = sys.argv[1]
c_password = sys.argv[2]

location_file = "location.db"

def wanlog(loc):
   try:
       net_connect = Netmiko(loc, username = c_username, password = c_password, device_type='cisco_ios')
       executeFirst = net_connect.send_config_set(firstCommand)
       executeSecond = net_connect.send_config_set(secondCommand)
       print(executeFirst + "\n")
       print(executeSecond + "\n")
       myReport.write(executeFirst + "\n")
       myReport.write(executeSecond + "\n")
       net_connect.disconnect()
   except:
       print("Error connection to: {}", format(loc))
       error_file = open("unavailable.txt", "a")
       error_file.write(loc)


if os.path.isfile(location_file) == True:

    myReport = open("myreport.txt","a")
    error_file = open("unavailable.txt", "w")
    selection = open(location_file, 'r')
    location_list = selection.readlines()
    print ("Cisco AutoConfig v0.1\n")
    print ("Usage:  cisco_auto_config.py <username> <password>")
    print("Location DB present")
    for items in location_list:
    wanlog(items)

    myReport.close()

else:
    print("Location file is missing")
    sys.exit()

