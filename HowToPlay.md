# Tresorhaus Security Challenge - Spielanleitung 🎮

## 🚀 Übersicht
Eine spielerische Security Challenge für angehende Solution Architects. Knacke unseren Tresor und zeig uns deine Skills!

## 🎯 Ziel
Durchlaufe drei Level und beweise, dass du das Zeug zum Tresorhaus Solution Architect hast.

## 🕹️ Spielablauf

### 🔑 Level 0: Der erste Kontakt
1. Verbinde dich zum Server:
```bash
ssh challenge.tresorhaus-sec.de -p 2222
```

2. Du siehst dieses coole ASCII-Banner:
```
████████╗██████╗ ███████╗███████╗ ██████╗ ██████╗ ██╗  ██╗ █████╗ ██╗   ██╗███████╗
╚══██╔══╝██╔══██╗██╔════╝██╔════╝██╔═══██╗██╔══██╗██║  ██║██╔══██╗██║   ██║██╔════╝
   ██║   ██████╔╝█████╗  ███████╗██║   ██║██████╔╝███████║███████║██║   ██║███████╗
   ██║   ██╔══██╗██╔══╝  ╚════██║██║   ██║██╔══██╗██╔══██║██╔══██║██║   ██║╚════██║
   ██║   ██║  ██║███████╗███████║╚██████╔╝██║  ██║██║  ██║██║  ██║╚██████╔╝███████║
   ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝
```

3. Erste Challenge: Finde die versteckten Login-Daten
   - Tipp: Manchmal lassen Entwickler Kommentare im Code...
   - Credentials: batman/nanapwd

4. Nach erfolgreichem Login erscheint Batman und du bekommst deine persönliche Challenge-Umgebung!

### 🏰 Level 1: Die Sicherheitsschleuse
**Ziel**: Zeitbasierte Authentifizierung überwinden

1. Starte die Challenge:
```bash
./challenge.py
```

2. Problem: Die Sicherheitsschleuse akzeptiert nur Zugang um 04:20
3. Lösung: Systemzeit anpassen
```bash
date -s "04:20"
```

### 🔒 Level 2: Der Tresor
**Ziel**: HAL9000 überlisten

Du musst drei Bedingungen erfüllen:
1. Erstelle die Datei "please_open.txt"
```bash
echo -n "Diese Datei hat exakt zweiundvierzig Bytes!" > please_open.txt
```

2. Die Datei muss EXAKT 42 Bytes haben
```bash
ls -l please_open.txt  # Überprüfe die Größe
```

3. Ändere den Hostnamen zu "HAL9000"
```bash
hostname HAL9000
```

### 🎮 Level 3: Der Final Boss
**Ziel**: Den legendären Konami Code eingeben

Der Code kann auf verschiedene Arten eingegeben werden:
- `↑↑↓↓←→←→BA`
- `UUDDLRLRBA`
- `uuddlrlrba`
- `upupdowndownleftrightleftrightba`

## 🏆 Erfolgreicher Abschluss

Nach Eingabe des korrekten Codes erscheint:
```
    ╔═══════════════════════════════════════╗
    ║  🎉 CONGRATULATIONS! YOU DID IT! 🎉   ║
    ╚═══════════════════════════════════════╝
         _____                               
        |     |_.-----.-----.-----.-----.-----.
        |       |  -__|     |  _  |  -__|__ --|
        |_______|_____|__|__|___  |_____|_____|
                            |_____|             
```

Du erhältst:
1. Deinen persönlichen Bewerbungscode: ICANHAZTRESOR
2. Einen geheimen Hinweis für deine Bewerbung

## ⏰ Wichtige Informationen

- Zeitlimit: 24 Stunden
- Jeder Teilnehmer bekommt eine eigene, isolierte Umgebung
- Alle benötigten Tools sind vorinstalliert
- Die Challenge kann in beliebiger Reihenfolge gelöst werden

## 🎁 Easter Eggs

Es gibt verschiedene versteckte Easter Eggs in der Challenge:
- Referenzen zu klassischen Spielen
- Versteckte Kommentare im Code
- Special ASCII Art

## 🆘 Support

Bei technischen Problemen (nicht für Lösungshilfen!):
- Email: challenge@tresorhaus-sec.de
- Status-Updates: @TresorhausChallenge

## 🎓 Lernziele

Die Challenge testet Fähigkeiten in:
- System Administration
- Linux Command Line
- Problem-Solving
- Aufmerksamkeit für Details
- Security Awareness

## 🚫 Nicht erlaubt

- Container-Escape Versuche
- Angriffe auf andere Teilnehmer
- Brute-Force Attacken
- Teilen der Lösungen

Viel Erfolg bei der Challenge! 🎮🔐
