from netmiko import ConnectHandler
Router = {
    'device_type':'cisco_ios',
    'ip':'10.215.26.',
    'hostname':'vnpro',
    'password':'vnpro@123',
    'secret':'vnpro@321'
}

net_connect_1=ConnectHandler(**Router)
net_connect_1.enable()

Switch = {
    'device_type':'cisco_ios',
    'ip':'10.215.26.',
    'hostname':'vnpro',
    'password':'vnpro@123',
    'secret':'vnpro@321'
}

net_connect_2=ConnectHandler(**Switch)
net_connect_2.enable()

#Tao sub-interface cho Router
so_vlan=input('Nhap so vlan muon tao: ')
for i in range (10,int(so_vlan)*10+1,10):
    net_connect_1.send_command=['int e0/0','no shut']
    tao_subif=['int e0/0.'+str(i)]
    tao_ip_subif=['ip add 192.168.'+str(i)+'.1 255.255.255.0']
    net_connect_1.send_config_set(tao_subif)
    net_connect_1.send_config_set(tao_ip_subif)
    output1 = net_connect_1.send_command('show ip int br')
print(output1)

#Tao VLAN cho SW, access VLAN den tung PC
for j in range (10,int(tao_vlan)*10+1,10):
    taovlan=['vlan '+str(j)]
    
for k in range (1,int(so_vlan)+1,1):
    access_vlan=['int e0/'+str(k),'sw mode access','sw access vlan '+str(k*10)]
    net_connect_2.send_config_set(access_vlan)
    output2 = net_connect_2.send_command('show vlan br')
print(output2)

#Cap DHCP cho tung VLAN
for a in range (10,int(so_vlan)*10+1,10):
    tao_dhcp_pool=['ip dhcp pool VLAN'+str(a)]
    tao_add_dhcp=['network 192.168.'+str(a)+'.0 255.255.255.0','network 192.168.'+str(a)+'.1']
    net_connect_1.send_config_set(tao_dhcp_pool)
    net_connect_1.send_config_set(tao_add_dhcp)






