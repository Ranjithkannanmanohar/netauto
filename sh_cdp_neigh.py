from netmiko import ConnectHandler

def sh_cdp_neigh(**RTR):
    net_connect = ConnectHandler(**RTR)
    output = net_connect.send_command( "Sh cdp neigh" )
    print( output )