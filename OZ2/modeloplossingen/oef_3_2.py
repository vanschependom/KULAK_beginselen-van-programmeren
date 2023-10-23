
# We blijven de while lus zo lang uitvoeren tot we ze stoppen met break
while True:
    # We tranformeren de input naar float pas later want kunnen een 'q' verwachten
    graden_celsius = input("Geef de temperatuur in farenheit op: ")
    if graden_celsius.lower() == "q":
        break
    
    graden_farenheit = 1.8 * float(graden_celsius) + 32
    print(f"{graden_celsius} C = {graden_farenheit} F")
    