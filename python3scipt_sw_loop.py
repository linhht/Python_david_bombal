import getpass
import telnetlib

HOST = "1.1.1.11"
user = input("Enter your telnet account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"ena\n")
tn.write(b"cisco\n")
tn.write(b"conf t\n")

for n in range (6, 11):
 tn.write(b"vlan "+str(n).encode('ascii')+b"\n")

tn.write(b"end\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))

