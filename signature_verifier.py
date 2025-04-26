"""
Signature Verifier — проверка подписи сообщения, подписанного Bitcoin-адресом.
"""

import argparse
import base64
import hashlib
import ecdsa
import base58
from bitcoin import ecdsa_verify, ecdsa_recover, privkey_to_address

def verify_message(address, signature, message):
    import bitcoin
    try:
        valid = bitcoin.ecdsa_verify(message, signature, address)
        return valid
    except Exception as e:
        print("❌ Ошибка при проверке:", e)
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Проверка Bitcoin-подписи сообщения.")
    parser.add_argument("address", help="Bitcoin-адрес")
    parser.add_argument("signature", help="Подпись (base64)")
    parser.add_argument("message", help="Оригинальное сообщение")

    args = parser.parse_args()

    print("🔍 Проверка подписи:")
    if verify_message(args.address, args.signature, args.message):
        print("✅ Подпись действительна.")
    else:
        print("❌ Подпись недействительна.")
