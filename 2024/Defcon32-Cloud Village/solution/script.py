from azure.identity import DefaultAzureCredential
from azure.keyvault.keys import KeyClient
from azure.keyvault.keys.crypto import CryptographyClient, EncryptionAlgorithm
from azure.core.exceptions import HttpResponseError

# Key identifier
key_identifier = "https://mysticcoffer.vault.azure.net/keys/wyrmguard/85261814726c4e1aaedccaf8f2eabca8"

# Extract the vault URL, key name, and version from the key identifier
vault_url = "https://mysticcoffer.vault.azure.net/"
key_name = "wyrmguard"
key_version = "85261814726c4e1aaedccaf8f2eabca8"

# Create a KeyClient using DefaultAzureCredential
credential = DefaultAzureCredential()
key_client = KeyClient(vault_url=vault_url, credential=credential)

# Get the specific version of the key from the Key Vault using the key name and version
key = key_client.get_key(key_name, key_version)

# Create a CryptographyClient
crypto_client = CryptographyClient(key, credential=credential)

# The encrypted message to decrypt
encrypted_message = b'\x19\x03\xc4d"\\.\xab \xae\xa1\x08\xe6\xfb6A\xfe\x83n\\\xcf\xb2\xf2\xc8|\x97J\xcds^\xf0\xcfK\x95a\x7f\xe4U\x8d\xa8\x1b[k\x02W\x101\xd4\xaa\xc6\xf9\x11\xeb_\x04\x95kmP*\x1b}\x88\xfed\xf76\xbd\xde*XRP\xcb\xc1\t\xfa!\x83\x1d\xd7r\x95\xd7\x08\x80\xcfnn\xcf\xf6\xc1d\x8e\x0f\xfb7\xfa`=\xad\xc2\xbfMF6\xe1\x05\xf3\xa8\xd8Ky\xdckV3\xc5\xbev3\xbe\\\xc7U\x8c\x87V\x19#B\xfa\xd8#\x94\x9f\x84\x82~\xddg\xca\xe2\xfd\x80\xe4\xa3@\x12\x9be\x99e_\xf6\x91\x85sEef\'\xe9\x86\x99\xd1%\x85\x91{\xae\xb6M<n\x16\xa8\xe5\xe1\x1b\x07\x9e\x82\xcd\xa6r\xc7\xba\xcc\x9c\xe3\x0b\x93\xe5\x97\xc2\x04\x03\x88{,\xe5\x9fL\x0b\xe0^\x00\xc3\x8dn\x8f6N\xf0q\x92y\x8e\x08\x12>?{\x1a\xa6\xf5\xac\xd0t\\\x81\x10\xab\xaa\x8e8)\xd1GZ\xce\xe7\x95S9QN\xe2\xe1\xfb\xc9\xab\xbd\xbc\xad'

# Attempt to decrypt the encrypted message
try:
    decrypt_result = crypto_client.decrypt(EncryptionAlgorithm.rsa_oaep, encrypted_message)
    decrypted_message = decrypt_result.plaintext.decode()
    print(f"Decrypted: {decrypted_message}")
except HttpResponseError as e:
    print(f"An error occurred during decryption: {e.message}")
    print(f"Code: {e.error.code}, Message: {e.error.message}")

    # Additional debugging: Check if the key and encrypted message are correct
    print(f"Key: {key}")
    print(f"Encrypted message: {encrypted_message}")
