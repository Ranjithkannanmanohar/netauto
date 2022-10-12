from netmiko import ConnectHandler

def sh_ver(**RTR):
    net_connect = ConnectHandler(**RTR)
    output = net_connect.send_command( "Sh version" )
    print( output )