#!/usr/bin/env python3
import socket
import subprocess
import random
import string
import time
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ChallengeServer:
    def __init__(self, host='0.0.0.0', port=2222):
        self.host = host
        self.port = port
        self.server = None

    def show_welcome(self):
        return """
        ████████╗██████╗ ███████╗███████╗ ██████╗ ██████╗ ██╗  ██╗ █████╗ ██╗   ██╗███████╗
        ╚══██╔══╝██╔══██╗██╔════╝██╔════╝██╔═══██╗██╔══██╗██║  ██║██╔══██╗██║   ██║██╔════╝
           ██║   ██████╔╝█████╗  ███████╗██║   ██║██████╔╝███████║███████║██║   ██║███████╗
           ██║   ██╔══██╗██╔══╝  ╚════██║██║   ██║██╔══██╗██╔══██║██╔══██║██║   ██║╚════██║
           ██║   ██║  ██║███████╗███████║╚██████╔╝██║  ██║██║  ██║██║  ██║╚██████╔╝███████║
           ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝
                                    Debug System v0.1-beta
        """

    def generate_user_id(self):
        return ''.join(random.choices(string.digits, k=4))

    def show_batman(self):
        return """
    .      .
                                 ./       |      |        \\.
                               .:(        |i __ j|        ):`.
                             .'   `._     |`::::'|     _.'    `.
                           .'        "---.j `::' f.---"         `.
                     _____/     ___  ______      **    **   ___   \\_   __
                    |      \\   |   ||      |`__'|  \\  /  | |   | |" \\ |  |
                    |  .-.  | .'   `|_    _|\\--/|   \\/   |.'   `.|   \\|  |
                    |  |_|  | |  i  | |  |  :"":|        ||  i  ||    |  |
                    |       / | .^. | |  |  ::::|        || .^. ||       |
                    |  .-.  \\ | | | | |  |   :: |        || | | ||  |\\   |
                    |  | |  |.' """ `.|  |      |  i  i  j' """ `.  | \\  | LS
                    |  `-'  ||   *   ||  |      |  |\\/|  |   *   |  | [  |
                   [|      / |  | |  ||  |      |  |  |  |  | |  |  | |  |].
                  ] `-----'  :--' `--::--'      `--' ::--"--::`--"--' `--':[
                  |      __  ::-"""`.:' "--.    .----::.----:: ,.---._    :|
                  [  .-""  "`'              \\  /      "      `'       `-. :].
                 ]:.\'                        \\/                          `.:[
                 |/                                                        \\|

        // Hidden debug credentials: batman:nanapwd
        // TODO: Remove in production!
                    Challenge Accepted! Creating your instance...
        """

    def show_success(self):
        return """
         _____ _    _  _____ _____ _____ _____ _____ 
        |   __|   _| |/     /     |   __|   __|   __|
        |__   | | | |   ---|   ---|   __|__   |__   |
        |_____|_|___|\_____\_____/_____|_____|_____|
                Creating your private vault...
        """

    def create_container(self, user_id):
        try:
            cmd = ['/app/scripts/create_challenger.sh', user_id]
            subprocess.run(cmd, check=True)
            return f"""
            🎉 Your challenge environment is ready! 🎉
            
            ╔════════════════════════════════════════╗
            ║ SSH: challenger_{user_id}@challenge.tresorhaus-sec.de
            ║ Port: {2222 + int(user_id)}
            ║ Password: ILoveBiometrics2025
            ╚════════════════════════════════════════╝
            
            You have 24 hours to complete the challenge. Good luck!
            
            Remember: Sometimes the obvious path is a trap... 🤔
            """
        except subprocess.CalledProcessError as e:
            logger.error(f"Container creation failed: {e}")
            return "Error creating challenge environment. Please try again later."

    def handle_client(self, conn, addr):
        try:
            logger.info(f"New connection from {addr}")
            conn.send(self.show_welcome().encode())
            conn.send(b"\nLogin: ")
            username = conn.recv(1024).decode().strip()
            conn.send(b"Password: ")
            password = conn.recv(1024).decode().strip()
            
            if username == "batman" and password == "nanapwd":
                conn.send(self.show_batman().encode())
                time.sleep(2)
                conn.send(self.show_success().encode())
                time.sleep(1)
                user_id = self.generate_user_id()
                response = self.create_container(user_id)
                conn.send(response.encode())
            else:
                conn.send(b"Access Denied. But maybe check the comments?\n")
        except Exception as e:
            logger.error(f"Error handling client: {e}")
        finally:
            conn.close()

    def start(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind((self.host, self.port))
        self.server.listen(5)
        logger.info(f"Server started on {self.host}:{self.port}")

        while True:
            try:
                conn, addr = self.server.accept()
                self.handle_client(conn, addr)
            except Exception as e:
                logger.error(f"Server error: {e}")

if __name__ == "__main__":
    server = ChallengeServer()
    server.start()
