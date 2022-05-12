import socket

from settings import HOST, ENCODING, BUFF_SIZE, get_port_for_challenge

def send_rtt(s: socket, rtt):
    s.send(str(rtt).encode(ENCODING))
    

def get_flag(s: socket):
    data = s.recv(BUFF_SIZE)
    flag = data.decode(ENCODING).strip()
    print(flag)

def get_rtt(s: socket):
    data = s.recv(BUFF_SIZE)
    response = data.decode(ENCODING).strip()
    print(response)
    response_parts = response.split()

    current_rtt = int(response_parts[0][:-2])
    alpha = float(response_parts[1])
    sample_rtt = int(response_parts[2][:-2])

    new_rtt = (1-alpha)*current_rtt + alpha*sample_rtt
    new_rtt = int(round(new_rtt, 0))
    print(new_rtt)
    return new_rtt

def challenge4():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, get_port_for_challenge(4)))
        rtt = get_rtt(s)
        send_rtt(s, rtt)
        get_flag(s)
    
    
if __name__ == '__main__':
    challenge4()
