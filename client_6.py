import socket

from settings import HOST, BUFF_SIZE, ENCODING, get_port_for_challenge


def send_syn(s: socket):
    s.send("SYN Seq=0".encode(ENCODING))
    print("SYN Seq=0")

def recv_ack(s: socket):
    data = s.recv(BUFF_SIZE)
    ack = data.decode(ENCODING).strip()
    assert ack == "SYN,ACK Seq=0 Ack=1"
    print(ack)

def send_ack(s: socket):
    s.send("ACK Seq=1 Ack=1".encode(ENCODING))
    print("ACK Seq=1 Ack=1")

def get_flag(s: socket):
    data = s.recv(BUFF_SIZE)
    flag = data.decode(ENCODING).strip()
    print(flag)

# Plan pseudo-code
def challenge6():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, get_port_for_challenge(6)))
        send_syn(s)
        recv_ack(s)
        send_ack(s)
        get_flag(s)


if __name__ == '__main__':
    challenge6()
