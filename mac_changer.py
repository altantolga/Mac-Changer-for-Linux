import subprocess
import optparse
import re

def get_user_input():
    parse_object=optparse.OptionParser();
    parse_object.add_option("-i","--interface",dest="interface",help="changing interface")
    parse_object.add_option("-m","--mac",dest="mac_address",help="desired MAC address")
    return parse_object.parse_args()
def change_mac_address(user_interface,user_mac_address):
    subprocess.call(["ifconfig",user_interface,"down"])
    subprocess.call(["ifconfig",user_interface,"hw","ether",user_mac_address])
    subprocess.call(["ifconfig",user_interface,"up"])
def check_new_mac(interface):
    ifconfig=subprocess.check_output(["ifconfig",interface])
    new_mac=re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(ifconfig))
    if new_mac:
        return new_mac.group(0)
    else:
        return None

print("MAC Changer started!!!")
(user_input, arguments)=get_user_input()
change_mac_address(user_input.interface, user_input.mac_addresss)
check_new_mac(user_input.interface)
final_mac=check_new_mac(str(user_input.interface))

if final_mac==user_input.mac_addresss:
    print("----Success!!!----")
else:
    print("----ERROR----")