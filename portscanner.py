import socket
import termcolor

def scan(target, ports):
    print('\n' + ' Starting Scan For ' + str(target))
    for port in range(1, ports + 1):
        scan_port(target, port)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ipaddress, port))
        if result == 0:
            print("[+] Port {} is open".format(port))
        sock.close()
    except Exception as e:
        print("Error:", e)

targets = input("[*] Enter Targets To Scan (split them by ,): ")
ports = int(input("[*] Enter How Many Ports You Want To Scan: "))

if ',' in targets:
    print(termcolor.colored("[*] Scanning Multiple Targets"), 'purple')
    for ip_addr in targets.split(','):
        scan(ip_addr.strip(), ports)
else:
    scan(targets, ports)
