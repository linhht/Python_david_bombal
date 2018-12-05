import getpass
import telnetlib

user = input("Enter your telnet account: ")
password = getpass.getpass()

f = open('sw_list')

for IP in f:
    IP=IP.strip()
    print('Get config of SW '+(IP))
    tn = telnetlib.Telnet(IP)
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")
    tn.write(b"ter len 0\n")
    tn.write(b"sh run\n")
    tn.write(b"exit\n")

    readoutput = tn.read_all()
    saveoutput = open('sw_'+IP,'w')
    saveoutput.write(readoutput.decode('ascii'))
    saveoutput.write('\n')
    saveoutput.close
   # print(tn.read_all().decode('ascii'))

