import subprocess
from subprocess import check_output
from win10toast import ToastNotifier
import time

toast = ToastNotifier()

def get_initial_mac_gw():
    init_mac_gw = ""
    ip_gw = "192.168.1.1"
    line_mac = check_output(['arp','-a', ip_gw])
    return line_mac


def service_anti_poisoning(init_mac_gw):
    print("Service Anti-ARP-Poisoning")
    ip_gw = "192.168.1.1"
    while True:
        current_mac_gw = check_output(['arp','-a', ip_gw])
        if init_mac_gw != current_mac_gw:
            print("Health status: Attack Detected!!")
            toast.show_toast("Amenaza detectada","Es posible que este bajo un ataque de red", duration=10)
        else:
            print("Health Status: Good!!")
        time.sleep(5)

def main():
    init_mac_gw = get_initial_mac_gw()
    #print(init_mac_gw)
    service_anti_poisoning(init_mac_gw)

## Calling main function ##
main()
