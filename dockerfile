FROM python:3.9-slim

# System dependencies
RUN apt-get update && apt-get install -y \
    docker.io \
    openssh-server \
    && rm -rf /var/lib/apt/lists/*

# Setup SSH
RUN mkdir /run/sshd
RUN echo 'PermitRootLogin no' >> /etc/ssh/sshd_config

# Setup challenge environment
WORKDIR /app
COPY src/ /app/
RUN chmod +x /app/*.py

# Setup Docker-in-Docker
VOLUME /var/run/docker.sock

# Expose ports
EXPOSE 2222

# Start script
COPY scripts/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
