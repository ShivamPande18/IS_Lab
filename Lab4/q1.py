from cryptography.hazmat.primitives.asymmetric import rsa, dh
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
import os

# RSA key generation and management
class RSAKeyManager:
    def __init__(self):
        self.keys = {}

    def generate_key_pair(self, subsystem_name):
        """Generate RSA key pair for the subsystem"""
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        public_key = private_key.public_key()

        # Store the keys
        self.keys[subsystem_name] = {
            'private_key': private_key,
            'public_key': public_key
        }
        return public_key

    def get_public_key(self, subsystem_name):
        """Get the public key of a subsystem"""
        return self.keys[subsystem_name]['public_key']

    def encrypt_with_rsa(self, public_key, message):
        """Encrypt message using RSA"""
        ciphertext = public_key.encrypt(
            message,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return ciphertext

    def decrypt_with_rsa(self, subsystem_name, ciphertext):
        """Decrypt message using RSA"""
        private_key = self.keys[subsystem_name]['private_key']
        plaintext = private_key.decrypt(
            ciphertext,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return plaintext

# Diffie-Hellman Key Exchange
class DiffieHellmanKeyExchange:
    def __init__(self):
        # Generate DH parameters
        self.parameters = dh.generate_parameters(generator=2, key_size=2048, backend=default_backend())

    def generate_private_key(self):
        """Generate DH private key"""
        return self.parameters.generate_private_key()

    def generate_shared_key(self, private_key, peer_public_key):
        """Generate shared key using private and peer's public key"""
        shared_key = private_key.exchange(peer_public_key)
        derived_key = HKDF(
            algorithm=hashes.SHA256(),
            length=32,
            salt=None,
            info=b'dh key exchange',
            backend=default_backend()
        ).derive(shared_key)
        return derived_key

# Communication between subsystems
class SecureCommunicationSystem:
    def __init__(self):
        self.rsa_manager = RSAKeyManager()
        self.dh_key_exchange = DiffieHellmanKeyExchange()
        self.subsystems = {}

    def register_subsystem(self, name):
        """Register a new subsystem and generate RSA key pair"""
        public_key = self.rsa_manager.generate_key_pair(name)
        self.subsystems[name] = {
            'public_key': public_key
        }
        print(f'Subsystem {name} registered with RSA public key.')

    def exchange_keys(self, subsystem1, subsystem2):
        """Simulate key exchange between two subsystems using Diffie-Hellman"""
        print(f'Performing Diffie-Hellman key exchange between {subsystem1} and {subsystem2}.')
        private_key1 = self.dh_key_exchange.generate_private_key()
        private_key2 = self.dh_key_exchange.generate_private_key()

        # Simulate public key exchange
        public_key1 = private_key1.public_key()
        public_key2 = private_key2.public_key()

        # Generate shared keys
        shared_key1 = self.dh_key_exchange.generate_shared_key(private_key1, public_key2)
        shared_key2 = self.dh_key_exchange.generate_shared_key(private_key2, public_key1)

        assert shared_key1 == shared_key2, "Shared keys do not match!"

        print(f"Shared key established between {subsystem1} and {subsystem2}.")

    def send_secure_message(self, sender, receiver, message):
        """Encrypt and send a secure message using RSA"""
        receiver_public_key = self.rsa_manager.get_public_key(receiver)
        encrypted_message = self.rsa_manager.encrypt_with_rsa(receiver_public_key, message)
        print(f"{sender} sent encrypted message to {receiver}")
        return encrypted_message

    def receive_secure_message(self, receiver, encrypted_message):
        """Decrypt and read the secure message"""
        decrypted_message = self.rsa_manager.decrypt_with_rsa(receiver, encrypted_message)
        print(f"{receiver} received message: {decrypted_message.decode()}")
        return decrypted_message


# Example usage
if __name__ == "__main__":
    secure_comm_system = SecureCommunicationSystem()
    
    # Register subsystems
    secure_comm_system.register_subsystem("System A")  # Finance
    secure_comm_system.register_subsystem("System B")  # HR
    secure_comm_system.register_subsystem("System C")  # Supply Chain

    # Perform Diffie-Hellman key exchange between System A and System B
    secure_comm_system.exchange_keys("System A", "System B")

    # Send a secure message from System A to System B
    encrypted_msg = secure_comm_system.send_secure_message("System A", "System B", b"Confidential Financial Report")

    # System B receives and decrypts the message
    secure_comm_system.receive_secure_message("System B", encrypted_msg)
