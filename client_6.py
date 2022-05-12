import socket

server_ip = '162.243.73.199'
server_port = 9995

#create tcp socket
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (server_ip, server_port)

tcp_socket.connect(server_address)

initiate = 'SYN Seq=0'

print(initiate)
tcp_socket.send(str.encode(initiate))
response = tcp_socket.recv(1024)
response_str = response.decode()
print(response_str, end="")

acknowledge = 'ACK Seq=1 ACK=1'
print(acknowledge)
tcp_socket.send(str.encode(acknowledge))
response = tcp_socket.recv(1024)
response_str = response.decode()

print(response_str)