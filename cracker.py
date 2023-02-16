import hashlib
from pwn import *
import sys


# if len(sys.argv) != 2:
#     print("[X] invalid input. please call the script with a sha256 hash as an argument...")
#     print(f"{sys.argv[0]} <sha256sum>")
#     exit()

attempts = 1
password_file = "/home/osboxes/code/tcmsec_python/env/rockyou.txt"
target_hash = sys.argv[1]

with log.progress(f"Attempting to crack {target_hash}\n") as p:
    with open(password_file, "r", encoding="latin-1") as password_list:
        for password in password_list:
            password = password.strip("\n").encode("latin-1")
            password_hash = hashlib.sha256(password).hexdigest()
            p.status(f"[{attempts}] {password.decode('latin-1')} == {password_hash}")
            if password_hash == target_hash:
                p.success(f"Password hash found after {attempts} attempts! {password.decode('latin-1')} hashes to {password_hash}")
                exit()
            attempts += 1
        p.failure("Password hash not found")
        exit()
        