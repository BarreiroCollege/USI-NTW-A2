import socket
import random

from settings import HOST, BUFF_SIZE, ENCODING, get_port_for_challenge


def send_fin_ack(s: socket):
    s.send("FIN,ACK Seq=1 Ack=5".encode(ENCODING))
    print("FIN,ACK Seq=1 Ack=5")

def recv_ack_fin(s: socket):
    data = s.recv(BUFF_SIZE)
    ack, fin = data.decode(ENCODING).strip().split("\n")
    assert ack == "ACK Seq=5 Ack=2"
    print(ack)
    assert fin == "FIN,ACK Seq=5 Ack=2"
    print(fin)

def send_ack(s: socket):
    s.send("ACK Seq=2 ACK=6".encode(ENCODING))
    print("ACK Seq=2 ACK=6")

def get_flag(s: socket):
    data = s.recv(BUFF_SIZE)
    flag = data.decode(ENCODING).strip()
    print(flag)

# Plan pseudo-code
def challenge7():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, get_port_for_challenge(7)))
        send_fin_ack(s)
        recv_ack_fin(s)
        send_ack(s)
        get_flag(s)


if __name__ == '__main__':
    challenge7()
