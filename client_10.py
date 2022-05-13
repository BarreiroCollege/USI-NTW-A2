import socket
from typing import List

from settings import HOST, BUFF_SIZE, ENCODING, get_port_for_challenge


def get_two_bytes(s: socket) -> List[int]:
    data = s.recv(BUFF_SIZE)
    two_bytes = data.decode(ENCODING).strip()
    print(two_bytes)
    bs = []
    for byte in two_bytes.split(" "):
        bs.append(int(byte, 2))
    return bs


def calculate_checksum(bs: List[int]) -> str:
    byte = 2 ** 8
    add = sum(bs)
    total = (add % byte) + (add // byte)
    int_checksum = (byte - 1) - total
    checksum = "{0:b}".format(int_checksum).zfill(8)
    return checksum


def send_checksum(s: socket, checksum: str):
    s.send(checksum.encode(ENCODING))
    print(checksum)


def get_flag(s: socket) -> None:
    data = s.recv(BUFF_SIZE)
    flag = data.decode(ENCODING).strip()
    print(flag)


def challenge10() -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, get_port_for_challenge(10)))
        bs = get_two_bytes(s)
        checksum = calculate_checksum(bs)
        send_checksum(s, checksum)
        get_flag(s)


if __name__ == '__main__':
    challenge10()
