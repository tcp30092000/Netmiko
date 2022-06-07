from netmiko import ConnectHandler
SW1 = {
    'device_type':'cisco_ios',
    'ip':'10.215.26.241',
    'username':'vnpro',
    'password':'vnpro@123',
    'secret':'vnpro@321',
}
net_connect=ConnectHandler(**SW1)
net_connect.enable()
them_vlan=input('Nhap so vlan muon tao: ')
for n in range (1,int(them_vlan)+1,1):
    taovlan = ['vlan ' + str(n)]
    ipvlan = ['int vlan '+str(n),'ip add 172.16.'+str(n)+'.1 255.255.255.0','no shut']
    net_connect.send_config_set(taovlan)
    net_connect.send_config_set(ipvlan)
    output = net_connect.send_command('show ip int br')
print(output)

# xoa_vlan=input('Nhap vlan muon xoa: ')
# for m in range (int(xoa_vlan),int(xoa_vlan)+1,1):
#     xoavlan=['no int vlan '+str(m)]
#     xoaipvlan=['no vlan '+str(m)]
#     net_connect.send_config_set(xoavlan)
#     net_connect.send_config_set(xoaipvlan)
#     output =  net_connect.send_command('show ip int br')
# print(output)

giu_vlan=input('Nhap vlan muon giu: ')
for i in range (1,int(them_vlan)+1,1):
    if i != int(giu_vlan):
        xoavlan=['no int vlan '+str(i)]
        xoaipvlan=['no vlan '+str(i)]
        net_connect.send_config_set(xoavlan)
        net_connect.send_config_set(xoaipvlan)
        output =  net_connect.send_command('show ip int br')
print(output)


