# Lees een lange string in
s = input("Geef een lange string: ")

# Zoek de index van het laatste character (tellen vanaf 0!)
last = len(s) - 1

# Print de juiste zaken af (verschillende manieren)
print(s[0] + s[1] + s[2] + "..." + s[last-2] + s[last-1] + s[last])
print(s[0] + s[1] + s[2] + "..." + s[-3] + s[-2] + s[-1])

# Deze manier met behulp van de slice operator is de beste (NIET HARDGECODEERD):
print(s[:3] + "..." + s[-3:])