import os
import subprocess

def main():
    plaintext = input("Enter plaintext: ")
    key = os.urandom(16)
    key_hex = key.hex()
    print(f"Generated Key: {key_hex}")
    
    encrypt_proc = subprocess.run(
        ['python3', 'aesencrypt.py', key_hex, plaintext],
        capture_output=True, text=True
    )
    if encrypt_proc.returncode != 0:
        print(f"Encryption Error: {encrypt_proc.stderr}")
        return
    ciphertext = encrypt_proc.stdout.strip()
    print(f"Ciphertext: {ciphertext}")
    
    decrypt_proc = subprocess.run(
        ['python3', 'aesdecrypt.py', key_hex, ciphertext],
        capture_output=True, text=True
    )
    if decrypt_proc.returncode != 0:
        print(f"Decryption Error: {decrypt_proc.stderr}")
        return
    decrypted = decrypt_proc.stdout.strip()
    print(f"Decrypted Text: {decrypted}")

if __name__ == "__main__":
    main()