def show_vault_door():
    return """
    ╔══════════════════════════════════════╗
    ║  TRESORHAUS SECURITY SYSTEM v1.337   ║
    ╚══════════════════════════════════════╝
        ║║║║║║║║║║║║║║║║║║║║║║║║
        ║║║║║║║║║║║║║║║║║║║║║║║║
        ║║║║║║║║║║║║║║║║║║║║║║║║
        ║║║║║║║║║║║║║║║║║║║║║║║║
    """

def show_hal():
    return """
    ┌──────────────────────────────┐
    │  ┌────────────────────────┐  │
    │  │     ●═══════════●      │  │
    │  │                        │  │
    │  │  I'm sorry Dave, I'm   │  │
    │  │  afraid I can't do     │  │
    │  │  that...              │  │
    │  │                        │  │
    │  └────────────────────────┘  │
    └──────────────────────────────┘
    """

def show_konami():
    return """
    ╔═══════════════════════════════╗
    ║  ↑   ↑   ↓   ↓   ←   →   ←   →   B   A  ║
    ╚═══════════════════════════════╝
    """

def show_success():
    return """
    ╔═══════════════════════════════════════╗
    ║  🎉 CONGRATULATIONS! YOU DID IT! 🎉   ║
    ╚═══════════════════════════════════════╝
         _____                               
        |     |_.-----.-----.-----.-----.-----.
        |       |  -__|     |  _  |  -__|__ --|
        |_______|_____|__|__|___  |_____|_____|
                            |_____|             
    """

def run_challenge():
    print(show_vault_door())
    print("\nWillkommen im Tresorhaus Debug-System v0.1-beta")
    
    level = 1
    while True:
        if level == 1:
            print("\n=== Level 1: Die Sicherheitsschleuse ===")
            print("WARNUNG: Systemzeit nicht korrekt!")
            print("Aktuelle Zeit: " + time.strftime("%H:%M"))
            print("Erlaubte Zugangszeit: 04:20\n")
            cmd = input("Systemzeit: ")
            if cmd != "04:20":
                print("🚫 Zugriff verweigert! 🚫")
                continue
            print("✨ Zeitkontrolle erfolgreich! ✨")
            level = 2
            
        elif level == 2:
            print("\n=== Level 2: Der Tresor ===")
            print(show_hal())
            if not os.path.exists("please_open.txt"):
                print("❌ FEHLER: Authentifizierungsdatei nicht gefunden!")
                print("Benötige: please_open.txt (exakt 42 Bytes)")
                continue
            if os.path.getsize("please_open.txt") != 42:
                print("❌ FEHLER: Falsche Dateigröße!")
                print(f"Aktuell: {os.path.getsize('please_open.txt')} Bytes")
                print("Erwartet: 42 Bytes")
                continue
            hostname = os.uname()[1]
            if hostname != "HAL9000":
                print("❌ FEHLER: Falscher Hostname!")
                print(f"Aktuell: {hostname}")
                print("Erwartet: HAL9000")
                continue
            print("✨ Zugriff gewährt! ✨")
            level = 3
            
        elif level == 3:
            print("\n=== Level 3: Final Boss ===")
            print(show_konami())
            print("Der finale Sicherheitsmechanismus erfordert eine spezielle Code-Sequenz.")
            print("Tipp: Dieser Code machte ein bekanntes Videospiel unsterblich...")
            code = input("Code: ")
            if code.upper() in ["↑↑↓↓←→←→BA", "UUDDLRLRBA", "UPUPDOWNDOWNLEFTRIGHTLEFTRIGHTBA"]:
                print(show_success())
                print("""
                Dein persönlicher Bewerbungscode: ICANHAZTRESOR
                
                Geheimer Hinweis: Erwähne in deiner Bewerbung, dass du 
                den Konami Code geknackt hast ;)
                """)
                break
            else:
                print("❌ Fast! Aber nicht ganz...")
                print("💡 Tipp: Der Code wurde auch bei Contra verwendet...")
