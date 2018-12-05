import getpass
import sys
import telnetlib

HOST = "1.1.1.12"
user = raw_input("Enter your remote account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("Username: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

tn.write("ena\n")
tn.write("cisco\n")
tn.write("sh ip int bri\n")
tn.write("exit\n")

print tn.read_all()

