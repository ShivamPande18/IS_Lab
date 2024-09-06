import base64
import logging
import threading
import time
from Crypto.Cipher import AES
from Crypto.Util import number

# Configuration
KEY_SIZE = 1024
RENEWAL_INTERVAL = 365 * 24 * 3600  # 12 months in seconds
PASS_PHRASE = 'your-passphrase'  # Use a more secure passphrase in a real application

# Set up logging
logging.basicConfig(filename='key_management.log', level=logging.INFO)

keys_db = {}

def generate_rabin_keys(key_size=KEY_SIZE):
    """Generate Rabin key pair."""
    p = number.getPrime(key_size // 2)
    q = number.getPrime(key_size // 2)
    while p == q:
        q = number.getPrime(key_size // 2)
    n = p * q
    return {'public_key': n, 'private_key': (p, q)}

def encrypt_private_key(private_key, passphrase):
    """Encrypt the private key using AES."""
    cipher = AES.new(passphrase.encode(), AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(str(private_key).encode())
    return base64.b64encode(ciphertext).decode()

def log_operation(operation, hospital_id):
    """Log key management operations."""
    logging.info(f"{operation} performed for {hospital_id}")

def generate_keys(hospital_id):
    """Generate and return keys for a hospital or clinic."""
    if hospital_id not in keys_db:
        keys_db[hospital_id] = generate_rabin_keys()
        # Encrypt and store the private key securely
        encrypted_key = encrypt_private_key(keys_db[hospital_id]['private_key'], PASS_PHRASE)
        keys_db[hospital_id]['encrypted_private_key'] = encrypted_key
        log_operation('Key Generation', hospital_id)
        return {'public_key': keys_db[hospital_id]['public_key']}
    else:
        return {'public_key': keys_db[hospital_id]['public_key']}

def revoke_keys(hospital_id):
    """Revoke and regenerate keys for a hospital or clinic."""
    if hospital_id in keys_db:
        keys_db[hospital_id]['revoked'] = True
        new_keys = generate_rabin_keys()
        encrypted_key = encrypt_private_key(new_keys['private_key'], PASS_PHRASE)
        keys_db[hospital_id] = {'public_key': new_keys['public_key'], 'encrypted_private_key': encrypted_key}
        log_operation('Key Revocation and Renewal', hospital_id)
        return {'message': 'Keys revoked and new keys generated'}
    else:
        return {'message': 'No keys found for the given hospital ID'}

def renew_keys():
    """Renew keys for all hospitals and clinics periodically."""
    while True:
        for hospital_id in keys_db:
            if not keys_db[hospital_id].get('revoked'):
                new_keys = generate_rabin_keys()
                encrypted_key = encrypt_private_key(new_keys['private_key'], PASS_PHRASE)
                keys_db[hospital_id] = {'public_key': new_keys['public_key'], 'encrypted_private_key': encrypted_key}
                log_operation('Key Renewal', hospital_id)
        time.sleep(RENEWAL_INTERVAL)

def main():
    """Command-line interface for key management."""
    while True:
        print("\nKey Management System")
        print("1. Generate Keys")
        print("2. Revoke Keys")
        print("3. Exit")

        choice = input("Enter your choice: ")
        
        if choice == '1':
            hospital_id = input("Enter hospital ID: ")
            result = generate_keys(hospital_id)
            print(f"Generated keys for {hospital_id}: {result}")

        elif choice == '2':
            hospital_id = input("Enter hospital ID: ")
            result = revoke_keys(hospital_id)
            print(result)

        elif choice == '3':
            print("Exiting...")
            break

        else:
            print("Invalid choice, please try again.")

# Start key renewal in the background
renewal_thread = threading.Thread(target=renew_keys)
renewal_thread.daemon = True
renewal_thread.start()

if __name__ == '__main__':
    main()
