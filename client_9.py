import socket

server_ip = '162.243.73.199'
server_port = 9998



# create tcp socket
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (server_ip, server_port)
tcp_socket.connect(server_address)

response = tcp_socket.recv(1024)
print(response.decode())

# response_str = str(response.decode()).split()[2]
# port_num = int(response_str.strip())

# # new socket
# tcp_socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # new server address
# server_address = (server_ip, port_num)
# tcp_socket1.connect(server_address)
# response = tcp_socket1.recv(1024)

# print(response.decode())