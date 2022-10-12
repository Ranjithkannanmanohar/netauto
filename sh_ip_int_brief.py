from netmiko import ConnectHandler

def sh_ip_int_brief(**RTR):
    net_connect = ConnectHandler(**RTR)
    output = net_connect.send_command( "Sh ip int brief" )
    print( output )

