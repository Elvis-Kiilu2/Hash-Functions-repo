import hashlib

def sha256_hash(message):
    return hashlib.sha256(message.encode()).hexdigest()

if __name__ == '__main__':
    message = "Hello World"
    print(f'THe SHA256 Hash of "{message}" is: {sha256_hash(message)}')
'''
 **SHA-256**: Part of the SHA-2 family, produces a 256-bit hash. Widely used in cryptography.

'''