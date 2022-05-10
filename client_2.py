import socket

from settings import HOST, ENCODING, BUFF_SIZE, FLAG_LENGTH, get_port_for_challenge


def send_helo(s: socket):
    helo = 'helo'
    s.sendto(helo.encode(ENCODING), (HOST, get_port_for_challenge(2)))
    print(helo)


def get_flag(s: socket):
    data, server = s.recvfrom(BUFF_SIZE)
    flag = data.decode(ENCODING).strip()
    assert len(flag) == FLAG_LENGTH
    print(flag)


def challenge2():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        send_helo(s)
        get_flag(s)


if __name__ == '__main__':
    challenge2()
