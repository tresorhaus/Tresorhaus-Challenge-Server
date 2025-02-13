#!/bin/bash
set -e

USER_ID=$1
USERNAME="challenger_${USER_ID}"
BASE_PORT=2222
CONTAINER_PORT=$((BASE_PORT + USER_ID))

# Logging-Funktion
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Prüfen ob User-ID übergeben wurde
if [ -z "$USER_ID" ]; then
    log "Error: No user ID provided"
    exit 1
fi

# Container erstellen
log "Creating container for $USERNAME"
docker run -d \
    --name "$USERNAME" \
    --hostname "challenge_env" \
    --network challenge_net \
    -p "${CONTAINER_PORT}:22" \
    --memory="512m" \
    --cpus="0.5" \
    challenge-env

# User Setup
log "Setting up user environment"
docker exec "$USERNAME" useradd -m -s /bin/bash "$USERNAME"
docker exec "$USERNAME" bash -c "echo '$USERNAME:ILoveBiometrics2025' | chpasswd"

# Challenge Files kopieren
log "Copying challenge files"
docker cp /app/src/challenge.py "$USERNAME:/home/$USERNAME/"
docker exec "$USERNAME" chown "$USERNAME:$USERNAME" "/home/$USERNAME/challenge.py"
docker exec "$USERNAME" chmod +x "/home/$USERNAME/challenge.py"

# Cleanup nach 24h
(
    sleep 86400
    log "Cleaning up container $USERNAME after 24h"
    docker rm -f "$USERNAME"
) &

log "Challenge environment ready for $USERNAME on port $CONTAINER_PORT"
