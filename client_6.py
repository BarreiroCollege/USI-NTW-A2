import socket

from settings import HOST, BUFF_SIZE, ENCODING, get_port_for_challenge


def send_syn(s: socket, seq: int) -> int:
    syn = "SYN Seq={}".format(seq)
    s.send(syn.encode(ENCODING))
    print(syn)
    return seq + 1


def recv_ack(s: socket, expected_ack: int, expected_seq) -> int:
    data = s.recv(BUFF_SIZE).decode(ENCODING).strip()
    print(data)
    msg, raw_seq, raw_ack = data.split(" ")
    assert msg == "SYN,ACK"

    v_seq, r_seq = raw_seq.split("=")
    seq = int(r_seq)
    assert v_seq == "Seq"
    assert seq == expected_seq

    v_ack, r_ack = raw_ack.split("=")
    ack = int(r_ack)
    assert v_ack == "Ack"
    assert ack == expected_ack

    return seq + 1


def send_ack(s: socket, seq: int, srv_ack: int) -> int:
    ack = "ACK Seq={} Ack={}".format(seq, srv_ack)
    print(ack)
    s.send(ack.encode(ENCODING))
    return seq + 1


def get_flag(s: socket):
    data = s.recv(BUFF_SIZE)
    flag = data.decode(ENCODING).strip()
    print(flag)


def challenge6():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, get_port_for_challenge(6)))
        seq, srv_seq = 0, 0
        seq = send_syn(s, seq)
        srv_seq = recv_ack(s, seq, srv_seq)
        send_ack(s, seq, srv_seq)
        get_flag(s)


if __name__ == '__main__':
    challenge6()
