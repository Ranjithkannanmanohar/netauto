from netmiko import ConnectHandler

def sh_env_all(**RTR):
    net_connect = ConnectHandler(**RTR)
    output = net_connect.send_command( "Sh environment all" )
    print( output )