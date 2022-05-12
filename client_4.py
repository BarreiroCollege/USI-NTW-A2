import socket
from typing import Tuple

from settings import HOST, BUFF_SIZE, ENCODING, get_port_for_challenge


def get_data(s: socket) -> Tuple[int, float, int]:
    data = s.recv(BUFF_SIZE)
    raw_data = data.decode(ENCODING).strip()
    print(raw_data)
    rtt, alpha, lrtt = raw_data.replace("ms", "").split(" ")
    rtt = int(rtt)
    alpha = float(alpha)
    lrtt = int(lrtt)
    return rtt, alpha, lrtt


def calculate_ertt(rtt: int, alpha: float, lrtt: int) -> int:
    return round((rtt * (1 - alpha)) + (lrtt * alpha))


def send_ertt(s: socket, ertt: int):
    ertt = str(ertt)
    s.send(ertt.encode(ENCODING))
    print(ertt)


def get_flag(s: socket):
    data = s.recv(BUFF_SIZE)
    flag = data.decode(ENCODING).strip()
    print(flag)


def challenge4():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, get_port_for_challenge(4)))
        rtt, alpha, lrtt = get_data(s)
        ertt = calculate_ertt(rtt, alpha, lrtt)
        send_ertt(s, ertt)
        get_flag(s)


if __name__ == '__main__':
    challenge4()
