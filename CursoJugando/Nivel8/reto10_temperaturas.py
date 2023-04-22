temperaturas = [19,20,21,24,23,27,21,20,19,18,21,20]

for i in temperaturas:
    if 17 < i < 26:
        print(f"Temperatura {i}  OK")
    else:
        print(f"La temperatura {i} se encuentra fuera de rango ")
        break