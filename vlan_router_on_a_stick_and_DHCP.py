from netmiko import ConnectHandler
Router = {
    'device_type':'cisco_ios',
    'ip':'192.168.242.135',
    'username':'vnpro',
    'password':'vnpro@123',
    'secret':'vnpro@321'
}

net_connect_1=ConnectHandler(**Router)
net_connect_1.enable()

Switch = {
    'device_type':'cisco_ios',
    'ip':'192.168.242.136',
    'username':'vnpro',
    'password':'vnpro@123',
    'secret':'vnpro@321'
}

net_connect_2=ConnectHandler(**Switch)
net_connect_2.enable()

#Lien ket duong trunk giua Switch va Router
no_shut = ['int e0/0','no shut']
trunk_switch = ['int e0/0','sw trunk encapsulation dot1q','sw mode trunk']
net_connect_2.send_config_set(trunk_switch)
net_connect_1.send_config_set(no_shut)
#Tao sub-interface cho Router
so_vlan=input('Nhap so vlan muon tao: ')
for i in range (10,int(so_vlan)*10+1,10):
    tao_ip_subif=['int e0/0.'+str(i),'encapsulation dot1q '+str(i),'ip add 192.168.'+str(i)+'.1 255.255.255.0']
    net_connect_1.send_config_set(tao_ip_subif)
    output = net_connect_1.send_command('show ip int br')
print(output)
   

#Tao VLAN cho SW, access VLAN den tung PC
for j in range (10,int(so_vlan)*10+1,10):
    taovlan=['vlan '+str(j)]
    
for x in range (1,int(int(so_vlan)+1/2)+1,1):
    access_vlan_1=['int e1/'+str(x),'sw mode access','sw access vlan '+str(x*10)]
    access_vlan_2=['int e2/'+str(x),'sw mode access','sw access vlan '+str(x*10)]
    net_connect_2.send_config_set(access_vlan_1)
    net_connect_2.send_config_set(access_vlan_2)
    output2 = net_connect_2.send_command('show vlan br')
print(output2)

 
    

#Cap DHCP cho tung VLAN
for a in range (10,int(so_vlan)*10+1,10):
    tao_add_dhcp=['ip dhcp pool VLAN'+str(a),'network 192.168.'+str(a)+'.0 255.255.255.0','default-router 192.168.'+str(a)+'.1']
    net_connect_1.send_config_set(tao_add_dhcp)






