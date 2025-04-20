# Benutzername abfragen
name = input("🔐 Benutzername: ").strip()

# Ist der Benutzer bekannt?
if name == "Anna":
  korrektes_passwort = "Aquamarin"
elif name == "Beate":
  korrektes_passwort = "Beige"
elif name == "Clara":
  korrektes_passwort = "Cyan"
else:
    print("❌ Unbekannter Benutzer. Zugriff verweigert.")
    exit()

max_versuche = 3
versuche = 0

# Passwortversuche
while versuche < max_versuche:
    eingabe_passwort = input("🔑 Passwort: ").strip()
    if eingabe_passwort == korrektes_passwort:
        print(f"✅ Willkommen, {name}!")
        break
    else:
        versuche += 1
        verbleibend = max_versuche - versuche
        print(f"❌ Falsches Passwort. {verbleibend} Versuch(e) verbleiben.")

if versuche == max_versuche:
    print("🔒 Zu viele Fehlversuche. Zugang gesperrt.")