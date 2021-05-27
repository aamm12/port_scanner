import socket
import termcolor


def scan(target, ports):
	print('\n' + '[*] Starting Scan For ' + target)
	for port in range(1, ports):
		scan_port(target, port)


def scan_port(addr, port):
	try:
		sock = socket.socket()
		sock.settimeout(1)
		sock.connect((addr, port))
		print("[+] Port Open " + str(port))
		sock.close()
	except:
		pass


targets = input("[*] Enter Targets To Scan(split them by ,): ")
ports = int(input("[*] How Many Ports To Scan: "))

if ',' in targets:
	print(termcolor.colored("[*] Scanning Multiple Targets", 'green'))
	for ip_addr in targets.split(','):
		scan(ip_addr, ports)
else:
	print("[*] Scanning Target")
	scan(targets, ports)