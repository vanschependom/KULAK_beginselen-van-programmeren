def mergesort(lijst):
    """
    Sorteert een lijst met behulp van mergesort algorithme
    Parameters
    ----------
    lijst: list
        te sorteren lijst
    Returns
    -------
    list
        gesorteerde lijst
    """
    # Basisgeval
    if len(lijst) == 1:
        return lijst
    
    # Deel de lijst op in twee helften
    linkerhelft = lijst[: len(lijst)//2]
    rechterhelft = lijst[len(lijst)//2 :]
    
    # sorteer beide delen recursief
    links_gesorteerd = mergesort(linkerhelft)
    rechts_gesorteerd = mergesort(rechterhelft)
    
    # voeg de twee gestorteerde helften gesorteerd bij elkaar
    gesorteerd = []
    
    linker_idx = 0
    rechter_idx = 0
    
    while linker_idx < len(links_gesorteerd) and rechter_idx < len(rechts_gesorteerd):
        if links_gesorteerd[linker_idx] <= rechts_gesorteerd[rechter_idx]:
            gesorteerd.append(links_gesorteerd[linker_idx])
            linker_idx += 1
        else:
            gesorteerd.append(rechts_gesorteerd[rechter_idx])
            rechter_idx += 1
    while linker_idx < len(links_gesorteerd):
        gesorteerd.append(links_gesorteerd[linker_idx])
        linker_idx += 1
    while rechter_idx < len(rechts_gesorteerd):
        gesorteerd.append(rechts_gesorteerd[rechter_idx])
        rechter_idx += 1
    
    # Geef resultaat terug
    return gesorteerd

if __name__ == '__main__':
    lijst = [1,4,53,123,1,323,4442,21,231]
    print(mergesort(lijst))