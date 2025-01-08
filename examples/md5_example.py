import hashlib

def md5_hash(message):
    # Return the hexadecimal representation of the hash
    return hashlib.md5(message.encode()).hexdigest()

if __name__ == "__main__":
    # Call the function
    message = "Hello World!!"
    print(f'The MD5 hash of "{message}" is: {md5_hash(message)}')

"""
- **MD5**: Produces a 128-bit hash but it is vulnerable to collisions.

"""