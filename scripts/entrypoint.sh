#!/bin/bash
set -e

# Start SSH service
/usr/sbin/sshd

# Start the landing server
python3 /app/landing_server.py
