import socket
from typing import Tuple

from settings import HOST, BUFF_SIZE, ENCODING, get_port_for_challenge


def get_data(s: socket) -> Tuple[float, float, float]:
    data = s.recv(BUFF_SIZE)
    raw_data = data.decode(ENCODING).strip()
    print(raw_data)

    l_v, l_u, r1_v, r1_u, r2_v, r2_u = raw_data.split(" ")
    l_v = float(l_v.replace("L=", ""))
    r1_v, r2_v = float(r1_v.replace("R1=", "")), float(r2_v.replace("R2=", ""))

    expos = {'K': 10 ** 3, 'M': 10 ** 6, 'G': 10 ** 9}
    for key, value in expos.items():
        if l_u.startswith(key):
            l_v *= value
        if r1_u.startswith(key):
            r1_v *= value
        if r2_u.startswith(key):
            r2_v *= value

    return l_v, r1_v, r2_v


def calculate_delay(l, r1, r2) -> float:
    n1 = l / r1
    n2 = l / r2
    return n1 + n2


def send_delay(s: socket, delay: float):
    delay = str(delay)
    s.send(delay.encode(ENCODING))
    print(delay)


def get_flag(s: socket):
    data = s.recv(BUFF_SIZE)
    flag = data.decode(ENCODING).strip()
    print(flag)


def challenge5():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, get_port_for_challenge(5)))
        l, r1, r2 = get_data(s)
        delay = calculate_delay(l, r1, r2)
        send_delay(s, delay)
        get_flag(s)


if __name__ == '__main__':
    challenge5()
