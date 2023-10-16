
# Input van gebruiker:
dagen_sinds_training = int(input("Hoeveel dagen geleden was de vorige training: "))
duurtijd_vorige_training = int(input("Hoelang duurde de vorige training (in aantal minuten): "))
gemiddelde_hartslag_vorige_training = float(input("Geef de gemiddelde hartslag van vorige training: "))

# Beslissingsboom voor ons sportprogramma
if duurtijd_vorige_training < 30:
    print("Je mag gaan sporten!")
else:
    # Maken een nieuwe variabele aan voor de aantal dagen rust die noodzakelijk zijn
    if gemiddelde_hartslag_vorige_training > 180 and duurtijd_vorige_training > 30:
        dagen_rust = 3
    else:
        dagen_rust = 2
    
    if dagen_sinds_training <= dagen_rust:
        print(f"Je rust best nog {dagen_sinds_training-dagen_rust} dag(en).")
        
    else:
        print("Je mag gaan sporten!")
        
        
    