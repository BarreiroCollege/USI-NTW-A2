import socket
from typing import Tuple

from settings import HOST, BUFF_SIZE, ENCODING, get_port_for_challenge


def get_ip_and_mask(s: socket) -> Tuple[str, int]:
    data = s.recv(BUFF_SIZE)
    ip_mask = data.decode(ENCODING).strip()
    print(ip_mask)
    ip, mask = ip_mask.split(" ")
    mask = int(mask)
    return ip, mask


def calculate_network(ip: str, mask: int) -> str:
    real_ip = 0
    for i, part in enumerate(ip.split(".")):
        real_ip += int(part) << (8 * (3 - i))
    real_mask = ((2 ** mask) - 1) << (32 - mask)
    real_net = real_ip & real_mask

    octets = []
    helper = (2 ** 8) - 1
    for exp in [3, 2, 1, 0]:
        byte = helper << (8 * exp)
        octets.append(str((real_net & byte) >> (8 * exp)))
    network = ".".join(octets)
    return network


def send_network(s: socket, network: str):
    s.send(network.encode(ENCODING))
    print(network)


def get_flag(s: socket):
    data = s.recv(BUFF_SIZE)
    flag = data.decode(ENCODING).strip()
    print(flag)


def challenge8():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, get_port_for_challenge(8)))
        ip, mask = get_ip_and_mask(s)
        network = calculate_network(ip, mask)
        send_network(s, network)
        get_flag(s)


if __name__ == '__main__':
    challenge8()
