import random

def werpDobbelsteen(param):
    worpen = []
    for i in range(param):
        worpen.append(random.randint(1, 6))
    return worpen

def zoekLangsteLijst(worpen):
    start_idx = 0
    lengte = 0
    lokale_start_idx = 0
    lokale_lengte = 0
    vorige_worp = None
    for idx, worp in enumerate(worpen):
        if worp == vorige_worp:
            lokale_lengte += 1
        else:
            if lokale_lengte > lengte:
                lengte = lokale_lengte
                start_idx = lokale_start_idx
            
            lokale_start_idx = idx
            lokale_lengte = 1
            vorige_worp = worp
            
    if lokale_lengte > lengte:
        lengte = lokale_lengte
        start_idx = lokale_start_idx
    
    return start_idx, lengte


def genereerLangsteLijstOutput(worpen, start_idx, lengte):
    output_str = ""
    for idx, worp in enumerate(worpen):
        if idx == start_idx:
            if lengte == 1:
                output_str += f"({worp}) "
            else:
                output_str += f"({worp} "
        elif idx == start_idx + lengte-1:
            output_str += f"{worp}) "
        else:
            output_str += f"{worp} "
    return output_str

if __name__ == '__main__':
    
    worpen = werpDobbelsteen(20)
    start_idx, lengte = zoekLangsteLijst(worpen)
    print(genereerLangsteLijstOutput(worpen, start_idx, lengte))


