```python
class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Person: {self.name}"


class Insasse(Person):
    def __init__(self, name, straftat):
        super().__init__(name)
        self.straftat = straftat

    def __str__(self):
        return f"Insasse: {self.name} – Straftat: {self.straftat}"


class Wache(Person):
    def __init__(self, name, personalnummer):
        super().__init__(name)
        self.personalnummer = personalnummer

    def __str__(self):
        return f"Wache: {self.name} – Personalnummer: {self.personalnummer}"


class Zelle:
    def __init__(self, max_belegung):
        self.max_belegung = max_belegung
        self.insassen = []
        self.wache = None

    def inhaftieren(self, person):
        if not isinstance(person, Insasse):
            print(f"❌ {person.name} ist kein Insasse und kann nicht inhaftiert werden.")
            return
        if len(self.insassen) >= self.max_belegung:
            print(f"❌ Zelle ist voll! Kein Platz für {person.name}.")
            return
        self.insassen.append(person)
        print(f"✅ {person.name} wurde inhaftiert.")

    def wachwechsel(self, person):
        if not isinstance(person, Wache):
            print(f"❌ {person.name} ist kein Wachpersonal!")
            return
        self.wache = person
        print(f"🔁 Wachwechsel: {person.name} ist jetzt zuständig.")

    def belegung(self):
        print("\n🔐 Zellenbelegung:")
        if self.insassen:
            for i, insasse in enumerate(self.insassen, 1):
                print(f"  {i}. {insasse}")
        else:
            print("  Keine Insassen.")
        if self.wache:
            print(f"🛡️ Zuständige Wache: {self.wache}")
        else:
            print("🛡️ Keine Wache zugewiesen.")


class Einzelzelle(Zelle):
    def __init__(self):
        super().__init__(max_belegung=1)


class Paarzelle(Zelle):
    def __init__(self):
        super().__init__(max_belegung=2)


class Gemeinschaftszelle(Zelle):
    def __init__(self, betten):
        if betten < 4 or betten > 8:
            raise ValueError("Gemeinschaftszelle muss zwischen 4 und 8 Betten haben.")
        super().__init__(max_belegung=betten)
```