#!/usr/bin/env python3
import base64
import zlib
import sys

def obfuscate_code(input_file):
    """
    Reads a Python file and returns its obfuscated version
    """
    with open(input_file, 'r') as f:
        code = f.read()

    # Compress and encode the code
    compressed = zlib.compress(code.encode())
    encoded = base64.b64encode(compressed)
    
    return encoded.decode()

def create_loader(encoded_code):
    """
    Creates the loader code that will decode and run the challenge
    """
    return f'''#!/usr/bin/env python3
import base64
import os
import time
from datetime import datetime

# Verschleierte Challenge-Logik
CHALLENGE_LOGIC = """
{encoded_code}
"""

def load_challenge():
    import zlib
    import importlib
    code = zlib.decompress(base64.b64decode(CHALLENGE_LOGIC))
    namespace = {{}}
    exec(code, namespace)
    return namespace['run_challenge']

if __name__ == "__main__":
    challenge = load_challenge()
    challenge()
'''

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Obfuscate the code
    encoded = obfuscate_code(input_file)
    
    # Create and save the loader
    loader_code = create_loader(encoded)
    with open(output_file, 'w') as f:
        f.write(loader_code)

    print(f"Successfully obfuscated {input_file} and created loader in {output_file}")
