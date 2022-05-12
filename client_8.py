import socket

server_ip = '162.243.73.199'
server_port = 9997

#create tcp socket
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (server_ip, server_port)

tcp_socket.connect(server_address)

response = tcp_socket.recv(1024)
response_str = response.decode()
print(response_str)
(ip_address, subnet) = response_str.split()

# takes an integer as an input and return the 8-bit binary form of the number
def decimal_to_binary(decimal: int) -> str:
    binary = "{0:b}".format(decimal)
    binary = "0"*(8-len(binary))+binary
    return binary

def binary_to_decimal(binary: str, stop_length=8) -> str:
    if stop_length != 8:
        binary = binary[:stop_length] + "0"*(8-stop_length)
    return str(int(binary,2))


subnet = int(subnet)
n_full_parts = subnet // 8
n_part = subnet % 8


ip_parts = ip_address.split('.')
# convert ip address to binary form
bin_form = ""
for i in range(len(ip_parts)):
    current_binary = decimal_to_binary(int(ip_parts[i]))+"."
    if i == n_full_parts:
        bin_form += current_binary[:n_part] + "0"*(8-n_part)+"."
        break
    else:
        bin_form += current_binary

for i in range(4-n_full_parts-1):
    bin_form += 8*"0"+"."
# ignore the last dot
bin_form = bin_form[:len(bin_form)-1]

binary_parts = bin_form.split(".")
dec_form = ""
for part in binary_parts:
    dec_form += binary_to_decimal(part)+"."

dec_form = dec_form[:len(dec_form)-1]

print(dec_form)

tcp_socket.send(str.encode(dec_form))

response = tcp_socket.recv(1024)
print(response.decode())



