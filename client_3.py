import socket

from settings import HOST, ENCODING, BUFF_SIZE, get_port_for_challenge


def get_flag(s: socket):
    data = s.recv(BUFF_SIZE)
    flag = data.decode(ENCODING).strip()
    print(flag)

def get_random_port(s: socket):
    data = s.recv(BUFF_SIZE)
    port = data.decode(ENCODING).strip()
    print(port)
    port_num = port.split(" ")[2]
    return int(port_num)

def challenge3():
    random_port = ""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, get_port_for_challenge(3)))
        random_port = get_random_port(s)
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, random_port))
        get_flag(s)



if __name__ == '__main__':
    challenge3()