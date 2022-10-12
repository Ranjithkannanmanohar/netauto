import sys
import os, os.path, time
from netmiko import ConnectHandler
from getpass import getpass
import datetime
from sh_ip_int_brief import *
from sh_cdp_neigh import *
from sh_ver import *
from sh_env_all import *
from config import *

IP = input("Enter the IP address or Hostname: ")
print( "Select the commands to be executed." )
print( "1.Sh ip int brief " )
print( "2.Sh cdp neigh" )
print( "3.Sh ver" )
print( "4.sh environment all" )
print( "5.Configuration" )

RTR = {
            'device_type': 'cisco_ios',
            'host': IP,
            'username': 'cisco',
            'password': 'cisco',
        }

while True:
    # take input from the user
    choice = input( "Enter choice(1/2/3/4/5): " )

    if choice in ('1', '2', '3', '4','5'):

        if choice == '1':
            print(sh_ip_int_brief(**RTR) )
        elif choice == '2':
            print(sh_cdp_neigh( **RTR ) )
        elif choice == '3':
            print( sh_ver( **RTR ) )
        elif choice == '4':
            print(sh_env_all( **RTR ) )
        elif choice == '5':
            print(config( **RTR ) )

        print( "Select the commands to be executed." )
        print( "1.Sh ip int brief " )
        print( "2.Sh cdp neigh" )
        print( "3.Sh ver" )
        print( "4.sh environment all" )
        print( "5.Configuration" )
        next_command = input( "Let's check for Another command for same device? (yes/no): " )
        if next_command == "no":
            print("------- End of Connection", IP, '---------------' )
            break
    else:
        print("invalid")





