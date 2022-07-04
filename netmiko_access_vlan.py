from netmiko import ConnectHandler
SW = {
    'device_type' : 'cisco_ios',
    'ip' : '192.168.242.132',
    'username' : 'vnpro',
    'password' : 'vnpro@123',
    'secret' : 'vnpro@321'
}

net_connect=ConnectHandler(**SW)
net_connect.enable()


#Tao VLAN cho SW
tao_vlan=input('Nhap so vlan theo so PC: ')
for i in range (1,int(tao_vlan)+1,1):
    taovlan=['vlan '+str(i)]
    ipvlan=['int vlan '+str(i),'ip add 172.16.'+str(i)+'.1 255.255.255.0','no shut']
    capvlan=['int e0/'+str(i),'sw mode access','sw access vlan '+str(i)]
    net_connect.send_config_set(taovlan)
    net_connect.send_config_set(ipvlan)
    net_connect.send_config_set(capvlan)
    output1 = net_connect.send_command('show ip int br')
    output2 = net_connect.send_command('show vlan br')
print(output1,output2)

    
