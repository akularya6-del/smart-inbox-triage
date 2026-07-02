import base64
import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from app.config import settings

def _get_key() -> bytes:
    # Ensure key is 32 bytes
    key = settings.ENCRYPTION_KEY.encode('utf-8')
    if len(key) < 32:
        key = key.ljust(32, b'0')
    elif len(key) > 32:
        key = key[:32]
    return key

def encrypt_token(token: str) -> str:
    if not token:
        return token
    aesgcm = AESGCM(_get_key())
    nonce = os.urandom(12)
    ciphertext = aesgcm.encrypt(nonce, token.encode('utf-8'), None)
    return base64.b64encode(nonce + ciphertext).decode('utf-8')

def decrypt_token(encrypted_token: str) -> str:
    if not encrypted_token:
        return encrypted_token
    
    try:
        data = base64.b64decode(encrypted_token.encode('utf-8'))
        nonce = data[:12]
        ciphertext = data[12:]
        aesgcm = AESGCM(_get_key())
        decrypted = aesgcm.decrypt(nonce, ciphertext, None)
        return decrypted.decode('utf-8')
    except Exception:
        # If decryption fails (e.g., key changed), log and return None or handle securely
        # For this MVP, raise an error or return empty
        raise ValueError("Decryption failed. Check ENCRYPTION_KEY.")

def mask_secret(secret: str) -> str:
    if not secret:
        return ""
    if len(secret) <= 8:
        return "*" * len(secret)
    return secret[:4] + "*" * (len(secret) - 8) + secret[-4:]
