import socket
from settings import HOST, ENCODING, BUFF_SIZE, get_port_for_challenge

d_classes = {"G":10**9,"M":10**6, "K":10**3}

def get_number(parts):
    num = int(parts[0])
    power = parts[1][0]
    if power.isupper():
        num *= d_classes[power]
    return num

def get_flag(s: socket):
    data = s.recv(BUFF_SIZE)
    flag = data.decode(ENCODING).strip()
    print(flag)


def send_delay(s: socket, delay):
    s.send(str(delay).encode(ENCODING))


def get_delay(s:socket):
    data = s.recv(BUFF_SIZE)
    response = data.decode(ENCODING).strip()
    print(response)
    response_parts = response.split("=")

    L = get_number(response_parts[1].split())
    R1 = get_number(response_parts[2].split())
    R2 = get_number(response_parts[3].split())

    total = L/R1 + L/R2
    print(total)
    return total
    

def challenge5():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, get_port_for_challenge(5)))
        delay = get_delay(s)
        send_delay(s,delay)
        get_flag(s)


if __name__ == '__main__':
    challenge5()
