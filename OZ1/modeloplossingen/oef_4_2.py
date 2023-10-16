# De hoogte en de breedte van het formaat in inch
breedteInInch = 8.5
hoogteInInch = 11

# Een constante die 1 inch in mm weergeeft
INCH_TO_MM = 25.4

# Bereken de afmetingen in mm
breedteInMm = breedteInInch * INCH_TO_MM
hoogteInMm = hoogteInInch * INCH_TO_MM

# Print het resultaat
print("Het formaat is %.2f op %.2f mm." % (breedteInMm,hoogteInMm))
# Let op de manier waarop de floats geformat worden in de string
# (Doen we dit niet, dan komen er teveel cijfers na de komma!)
# Lees het boek na over string formatting.