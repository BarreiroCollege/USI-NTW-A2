import socket

server_ip = '162.243.73.199'
server_port = 9994

d_classes = {"G":10**9,"M":10**6, "K":10**3}

#create tcp socket
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (server_ip, server_port)

tcp_socket.connect(server_address)

response = tcp_socket.recv(1024)
response_str = response.decode()



response_parts = response_str.split("=")
first_part = response_parts[1].split()
second_part = response_parts[2].split()
third_part = response_parts[3].split()


def get_number(parts):

    num = int(parts[0])
    power = parts[1][0]
    if power.isupper():
        num *= d_classes[power]
    return num

print(response_str)
print(response_parts)

L = get_number(first_part)
R1 = get_number(second_part)
R2 = get_number(third_part)

total = L/R1 + L/R2
print(total)



tcp_socket.send(str.encode(str(total)))
response = tcp_socket.recv(1024)
response_str = response.decode()

print(response_str)




