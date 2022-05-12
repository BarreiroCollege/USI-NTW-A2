import socket
from typing import Tuple

from settings import HOST, BUFF_SIZE, ENCODING, get_port_for_challenge


def get_ip_and_mask(s: socket):
    data = s.recv(BUFF_SIZE)
    ip_mask = data.decode(ENCODING).strip()
    print(ip_mask)
    ip, mask = ip_mask.split(" ")
    mask = int(mask)
    return ip, mask


def calculate_network(ip: str, mask: int):
    ip_new = ip.split(".")
    real_ip = 0
    for i, part in enumerate(ip_new):
        part = int(part)
        temp = part << 8*(3-i)
        real_ip = real_ip + temp
    real_mask = ((2**mask) - 1) << (32 - mask)
    real_network = real_ip & real_mask

    octets = []
    helper = (2**8) - 1
    for exp in [3,2,1,0]:
        byte = helper << (exp*8)
        temp = real_network & byte
        temp2 = temp >> (exp*8)
        octets.append(str(temp2))
    return ".".join(octets)


def send_network(s: socket, network: str):
    s.send(network.encode(ENCODING))
    print(network)

def get_flag(s: socket):
    data = s.recv(BUFF_SIZE)
    flag = data.decode(ENCODING).strip()
    print(flag)

# Plan pseudo-code
def challenge8():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, get_port_for_challenge(8)))
        ip, mask = get_ip_and_mask(s)
        network = calculate_network(ip, mask)
        send_network(s, network)
        get_flag(s)


if __name__ == '__main__':
    challenge8()
