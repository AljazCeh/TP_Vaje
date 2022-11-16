data = {"prices": [41970, 40721, 41197, 41137, 43033],
        "volume": [49135346712, 50768369805, 47472016405, 34809039137, 38700661463]}


def najvecja_vrednost(data):
    seznam = []

    for value in data.values():
        max_value = max(value)
        seznam.append(max_value)

    return seznam   


vrednost = najvecja_vrednost(data)
print(vrednost)