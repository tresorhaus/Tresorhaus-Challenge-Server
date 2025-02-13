# Tresorhaus Challenge Server 🔒

Ein automatisiertes Setup für den Tresorhaus Tech-Challenge Server. Der Server bietet eine spielerische Coding Challenge für potenzielle Solution Architects.

## 📁 Repository Struktur

```
tresorhaus-challenge/
├── ansible/
│   ├── inventory.yml
│   ├── playbook.yml
│   └── roles/
│       └── challenge-server/
│           ├── tasks/
│           ├── templates/
│           └── vars/
├── src/
│   ├── landing_server.py
│   ├── challenge.py
│   └── obfuscator.py
├── scripts/
│   ├── create_challenger.sh
│   └── monitor_challenges.sh
├── README.md
└── docker-compose.yml
```

## 🚀 Schnellstart

### Manuelle Installation (Debian 12)

1. System vorbereiten:
```bash
apt update && apt upgrade -y
apt install -y python3 python3-pip docker.io docker-compose git
```

2. Repository klonen:
```bash
git clone https://github.com/yourusername/tresorhaus-challenge.git
cd tresorhaus-challenge
```

3. Server starten:
```bash
docker-compose up -d
```

### 🤖 Automatische Installation mit Ansible

1. Ansible installieren:
```bash
apt install -y ansible
```

2. Playbook ausführen:
```bash
cd ansible
ansible-playbook -i inventory.yml playbook.yml
```

## 🎮 Die Challenge

Der Challenge-Server bietet ein mehrstufiges Puzzle:

1. Initial Login (Port 2222)
   - Finde die versteckten Credentials
   - Ein Batman wartet auf dich!

2. Individuelle Challenge
   - Jeder Teilnehmer bekommt einen eigenen Container
   - 24 Stunden Zeit zum Lösen
   - Drei knifflige Level

## 🛠 Administration

### Monitoring

Aktive Challenges überwachen:
```bash
./scripts/monitor_challenges.sh
```

### Container Management

Neue Challenge-Instanz erstellen:
```bash
./scripts/create_challenger.sh <user_id>
```

## 📋 Technische Details

- Basis: Debian 12
- Docker für Container-Isolation
- Python 3.9+
- Automatische Container-Bereinigung nach 24h
- Dynamische Port-Zuweisung (2222 + user_id)

## 🔐 Sicherheitshinweise

- Alle Dienste laufen in isolierten Containern
- Rate-Limiting aktiviert
- Regelmäßige Security-Updates
- Verschleierter Challenge-Code

## 🎯 Challenge Solution

Die Lösung wird natürlich nicht verraten! Aber hier ein kleiner Tipp:
> "Sometimes the most obvious solution is a red herring..."

## 📜 License

MIT License - siehe [LICENSE](LICENSE) Datei

---

## Ansible Installation

Das komplette Setup kann auch via Ansible automatisiert werden. Hier ist ein Beispiel-Playbook:

```yaml
# ansible/playbook.yml
---
- hosts: challenge_servers
  become: yes
  roles:
    - role: challenge-server
  vars:
    challenge_port: 2222
    docker_network: "challenge_net"
    cleanup_interval: "24h"
```

```yaml
# ansible/inventory.yml
---
challenge_servers:
  hosts:
    challenge.tresorhaus-sec.de:
      ansible_user: root
```

## 🤝 Contributing

1. Fork it
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -am 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Create a new Pull Request

## 💬 Support

Bei Fragen oder Problemen eröffne ein Issue oder kontaktiere das Tresorhaus Tech-Team.

---

Made with ❤️ by Tresorhaus Tech Team
