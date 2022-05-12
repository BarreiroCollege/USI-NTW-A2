import socket

from settings import HOST, BUFF_SIZE, ENCODING, get_port_for_challenge


def get_port(s: socket) -> int:
    data = s.recv(BUFF_SIZE)
    random_port = data.decode(ENCODING).strip()
    print(random_port)
    port = random_port.split(" ")[-1]
    return int(port)


def get_flag(s: socket):
    data = s.recv(BUFF_SIZE)
    flag = data.decode(ENCODING).strip()
    print(flag)


def challenge3():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, get_port_for_challenge(3)))
        port = get_port(s)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, port))
        get_flag(s)


if __name__ == '__main__':
    challenge3()
