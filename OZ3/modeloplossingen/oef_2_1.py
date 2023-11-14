import random

LENGTH_MAP = 10
WIDTH_MAP = 10
PROB_STONE = .25

game_map = []

for i in range(LENGTH_MAP):
    game_map_row = []
    for j in range(WIDTH_MAP):
        # Kijk of de buur lang gras is
        prob_long_gras = .25
        if j > 0:
            if game_map_row[-1] == ':':
                prob_long_gras = .5
        if i > 0:
            if game_map[-1][i] == ':':
                prob_long_gras = .5
            
            # Bij uitbereiding ook de diagonalen:
            
            # if i > 0 and game_map[-1][i-1] == ':':
            #     prob_long_gras = .5
            # if i < LENGTH_MAP-1 and game_map[-1][i] == ':':
            #     prob_long_gras = .5
                
        dice = random.random()
        if dice < PROB_STONE:
            game_map_row.append("#")
        elif dice < prob_long_gras + PROB_STONE:
            game_map_row.append(":")
        else:
            game_map_row.append(".")
    
    game_map.append(game_map_row)

game_map_str = ""
for i in range(LENGTH_MAP):
    # Aan elkaar plakken van lijst van strings kan met join.
    game_map_str += "".join(game_map[i]) + "\n"
    
print(game_map_str)