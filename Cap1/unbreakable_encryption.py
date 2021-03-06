from secrets import token_bytes
from typing import Tuple


def random_key(length: int) -> int:
    # gera length bytes aleatórios
    tb: bytes = token_bytes(length)

    # converte esses bytes em uma cadeia de bits e a devolve
    return int.from_bytes(tb, "big")


def encrypt(original: str) -> Tuple[int, int]:
    original_bytes : bytes = original.encode()
    dummy: int = random_key(len(original_bytes))
    original_key: int = int.from_bytes(original_bytes, "big")
    encrypted: int = original_key ^ dummy
    """XOR: Basicamente retornará 1 para 0^1 e 1^0, mas 0 para 0^0 e 1^1"""
    return dummy, encrypted


def decrypt(key1: int, key2: int) -> str:
    decrypted: int = key1 ^ key2 # XOR
    temp: bytes = decrypted.to_bytes((decrypted.bit_length()+ 7) // 8, "big")
    return temp.decode()


if __name__ == "__main__":
    key1, key2 = encrypt("One Time Pad!")
    result: str = decrypt(key1, key2)
    print(result)