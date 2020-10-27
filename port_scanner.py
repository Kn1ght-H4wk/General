import socket


open_port_file = open('Open ports.csv', 'w')
closed_port_file = open('Closed ports.csv', 'w')


def scan_port(ipaddress, port):

    try:
        sock = socket.socket()
        sock.settimeout(1)
        sock.connect((ipaddress, port))
        print('Port ' + str(port) + ' is open. ')

        open_port_file.write('Port ' + str(port) + ' is open. ')
        open_port_file.write('\n')

    except:
        print('Port ' + str(port) + ' is closed. ')

        closed_port_file.write('Port ' + str(port) + ' is closed. ')
        closed_port_file.write('\n')


ipaddress = input('Enter target to scan: ')
port_range_1 = int(input('On which port would you like the port scan to begin? '))
port_range_2 = int(input('And on which port would you like the scan to end?  '))
total_ports = range(port_range_1, port_range_2)


for port in total_ports:
    scan_port(ipaddress, port)

open_port_file.close()
closed_port_file.close()

print('Port scan complete. Results saved to file. ')










