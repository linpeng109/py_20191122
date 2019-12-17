import uuid


def get_mac_address(h=None):
    uuid_int = uuid.getnode()
    print(uuid_int)
    mac = uuid.UUID(int=uuid_int)
    # .hex[-12:]
    # print(mac)
    print(mac.hex[-12:])
    return mac.hex[-12:]


# if __name__ == '__main__':
#     result = get_mac_address()
#     print(result)
