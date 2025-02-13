#!/usr/bin/env python3
import base64
import os
import time
from datetime import datetime

# Der verschleierte Challenge-Code
CHALLENGE_LOGIC = """
H4sIAAAAAAAAA62TQW+CMBiG7/yKL96AgAKKt2VLNpeYZdm8GCptv36A2hbXtNk8AH2/t0/f
L4V6KIpsXocxEOqVj6YK4zhZhwDVuQ6d5Cy1QSkLRsKfXCPOF8wTVyhnV8UTR5Jz4UhOXvkC
cxFLj0slw4YpzqJpQWODkqBA04JkWHjBl4CaVxP7JcG8BH4n8PyIJ3EWwV8JmJa55y+NrwT0
vL4SCC3BHwnEGX+kSZbFka+a7SsBl0QRDH/hqMVeYcMhG5+DVj22zxvs9gbHZniqm8Ppre44
tJ2BozV0rWqomvOhea+brl33H7Xxre/6rtl1jfl0HJrns+4+L91gGF3XrdqPU1OZTlaVNQAA
"""

def load_challenge():
    import zlib
    import importlib
    code = zlib.decompress(base64.b64decode(CHALLENGE_LOGIC))
    namespace = {}
    exec(code, namespace)
    return namespace['run_challenge']

if __name__ == "__main__":
    challenge = load_challenge()
    challenge()
