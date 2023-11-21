

def nieuweVeelterm(coef, deg):
    """
    Creeer een nieuwe veelterm, geef als input de coeficient en graad van een term
    Parameters
    ----------
    coef : float
        Coeficient van een term
    deg : int
        De graad van een term
    Returns
    -------
    dict :
        dictionary dat de veelterm voorstelt
    """
    veelterm = dict()
    veelterm[deg] = coef
    return veelterm

def addTerm(poly, coef, deg):
    """
    Toevoegen van een extra term aan een veelterm
    Parameters
    ----------
    poly
    coef : float
        Coeficient van de toe te voegen term
    deg : int
        De graad van de toe te voegen term

    Returns
    -------

    """
    poly[deg] = coef

def vermenigvuldig(linker_factor, rechter_factor):
    """
    Vermenigvuldigen van twee veeltermen
    Parameters
    ----------
    linker_factor : dict
        Eerste factor in de vermenigvuldiging
    rechter_factor : dict
        Tweede factor in de vermenigvuldiging
    Returns
    -------
    dict
        Het product van de twee termen
    """
    product = dict()
    for ldeg in linker_factor:
        for rdeg in rechter_factor:
            if (ldeg+rdeg) in product:
                product[ldeg+rdeg] += linker_factor[ldeg]*rechter_factor[rdeg]
            else:
                product[ldeg+rdeg] = linker_factor[ldeg]*rechter_factor[rdeg]
    return product

def printVeelterm(poly):
    """
    Functie voor het printen van een veelterm
    Parameters
    ----------
    poly : dict
        Veelterm dat geprint moet worden
    Returns
    -------
    None
    """
    out_str = "p(x) = "
    sorted_deg = sorted(poly, reverse=True)
    for idx, deg in enumerate(sorted_deg):
        if idx != 0:
            out_str += f"+ "
        
        if deg != 0:
            out_str += f"{poly[deg]}x^{deg} "
        else:
            out_str += f"{poly[deg]} "

    print(out_str)
    
if __name__ == '__main__':
    p = nieuweVeelterm(-10, 0)
    addTerm(p, -1, 1)
    addTerm(p, 9, 7)
    addTerm(p, 5, 10)
    q = vermenigvuldig(p, p)
    printVeelterm(q)