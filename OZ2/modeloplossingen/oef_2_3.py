# Print een maand kalender

dagen = ['Ma', 'Di', 'Woe', 'Do', 'Vr', 'Za', 'Zo']

eerste_dag = input(f"Geef de eerste dag van de maand in [{','.join(dagen)}]: ")
dagen_in_maand = int(input("Geef het aantal dagen in de maand in: "))

dag_in_week = dagen.index(eerste_dag)

kalender = ''

for dag in dagen:
    # Aligneer rechts in in een string van 4 lang de dag
    kalender += f'{dag:>4}'

kalender += '\n'
kalender_rij = ' '*4*dag_in_week

for i in range(1, dagen_in_maand+1):
    # Aligneer rechts in in een string van 4 lang de index van de dag
    kalender_rij += f'{i:>4}'
    dag_in_week += 1
    
    if dag_in_week % 7 == 0:
        kalender_rij += '\n'
        kalender += kalender_rij
        kalender_rij = ''

kalender += kalender_rij

print(kalender)