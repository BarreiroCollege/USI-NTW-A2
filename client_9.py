import socket
from typing import Tuple, List, Optional

from settings import HOST, BUFF_SIZE, ENCODING, get_port_for_challenge


def get_interfaces_and_destination(s: socket) -> Tuple[List[Tuple[str, int, str]], str, str]:
    data = s.recv(BUFF_SIZE)
    ifaces_dest = data.decode(ENCODING).strip()
    print(ifaces_dest)
    entries = ifaces_dest.split(",")

    ifaces = []
    for entry in entries[:-2]:
        net, iface = entry.split(" ")
        ip, mask = net.split("/")
        mask = int(mask)
        ifaces.append((ip, mask, iface))

    default = entries[-2].split(" ")[1]
    destination = entries[-1]

    return ifaces, default, destination


def dotted_to_int(addr: str) -> int:
    ip = 0
    for i, part in enumerate(addr.split(".")):
        ip += int(part) << (8 * (3 - i))
    return ip


def get_out_iface(ifaces: List[Tuple[str, int, str]], destination: str) -> Optional[str]:
    ip = dotted_to_int(destination)
    iface_out, max_mask = None, None

    for addr, mask, iface in ifaces:
        network = dotted_to_int(addr)
        # matches = ((network >> antimask) ^ (ip >> antimask)) == 0
        bitmask = ((2 ** mask) - 1) << (32 - mask)
        matches = (ip & bitmask) == network
        if matches:
            if max_mask is None or mask > max_mask:
                iface_out = iface
                max_mask = mask

    return iface_out


def send_interface(s: socket, iface: str):
    s.send(iface.encode(ENCODING))
    print(iface)


def get_flag(s: socket) -> None:
    data = s.recv(BUFF_SIZE)
    flag = data.decode(ENCODING).strip()
    print(flag)


def challenge9() -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, get_port_for_challenge(9)))
        ifaces, default, destination = get_interfaces_and_destination(s)
        iface = get_out_iface(ifaces, destination)
        if iface is None:
            iface = default
        send_interface(s, iface)
        get_flag(s)


if __name__ == '__main__':
    challenge9()
