prijzen = {"aardbei": 3, "vanille": 4, "chocolade": 5}
aanbieding = prijzen["aardbei"] * 0.8
reclame_tekst = f"Vandaag in de aanbieding: aardbeienijs, 1 liter – slechts € {aanbieding}"
reclame_tekst2 = reclame_tekst[:64]
reclame_tekst3 = reclame_tekst2.lower()
reclame_tekst4 = reclame_tekst3.split()

for el in reclame_tekst4:
    if len(el) >= 5:
        print(el.upper())
    else:
        print(el)
# Dictionaries in Python: Je moet de dictionary definiëren met accolades {} en de sleutel-waarde paren scheiden met dubbele punten :. Dus {"aardbei": 3, "vanille": 4, "chocolade": 5} in plaats van losse variabelen.
# Toegang tot Dictionary Elementen: Om de waarde van "aardbei" te krijgen, gebruik je prijzen["aardbei"].
# Berekening van de Aanbiedingsprijs: Je moet de vermenigvuldiging uitvoeren op de waarde uit de dictionary, niet op een string.
# f-strings: De f-string functie kan niet met <aanbieding> werken, maar wel met {aanbieding}.
# Formattering van de Aanbiedingsprijs: Met ":.2f" zorg je ervoor dat de prijs wordt weergegeven met twee decimalen.
# Print de Uitkomst: Als je de reclame tekst in de console wil zien, moet je het printen met de functie print().
