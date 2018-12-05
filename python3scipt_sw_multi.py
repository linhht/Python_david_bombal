import getpass
import telnetlib

user = input("Enter your telnet account: ")
password = getpass.getpass()

f = open('sw_list')

for IP in f:
    IP=IP.strip()
    print('Configuring SW '+(IP))
    tn = telnetlib.Telnet(IP)
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")
    tn.write(b"conf t\n")
    for n in range (2, 11):
        tn.write(b"vlan "+str(n).encode('ascii')+b"\n")
    tn.write(b"end\n")
    tn.write(b"wr\n")
    tn.write(b"exit\n")
    print(tn.read_all().decode('ascii'))

