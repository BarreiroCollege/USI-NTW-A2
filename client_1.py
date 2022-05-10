import socket

from settings import HOST, BUFF_SIZE, ENCODING, get_port_for_challenge


def get_flag(s: socket):
    data = s.recv(BUFF_SIZE)
    flag = data.decode(ENCODING).strip()
    print(flag)


def challenge1():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, get_port_for_challenge(1)))
        get_flag(s)


if __name__ == '__main__':
    challenge1()
