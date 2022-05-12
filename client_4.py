import socket

server_ip = '162.243.73.199'
server_port = 9993

#create tcp socket
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (server_ip, server_port)

tcp_socket.connect(server_address)


response = tcp_socket.recv(1024)
response_str = response.decode()
print(response_str)

response_parts = response_str.split()

current_rtt = int(response_parts[0][:-2])
alpha = float(response_parts[1])
sample_rtt = int(response_parts[2][:-2])

new_rtt = (1-alpha)*current_rtt + alpha*sample_rtt
new_rtt = int(round(new_rtt, 0))
print(new_rtt)


tcp_socket.send(str.encode(str(new_rtt)))
response = tcp_socket.recv(1024)
response_str = response.decode()
print(response_str)


