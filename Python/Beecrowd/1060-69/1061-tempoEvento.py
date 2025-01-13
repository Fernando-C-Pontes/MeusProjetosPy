def calcularDiferenca(inicial, final):
    limites = [24, 60, 60]
    diferenca = [0] * len(inicial)

    for i in range(len(inicial) - 1, -1, -1):
        if final[i] < inicial[i]:
            final[i - 1] -= 1
            final[i] += limites[i]

        diferenca[i] = final[i] - inicial[i]

    return diferenca

def ajusteDia(inicial, final):
    for i in range(len(inicial)):
        if final[i] < inicial[i]:
            return 1
        elif final[i] > inicial[i]:
            return 0
    return 0

def main():
    diaInicio = int(input().split()[1])
    momentoInicio = [int(x) for x in input().split(":")]
    diaFim = int(input().split()[1])
    momentoFim = [int(x) for x in input().split(":")]

    W = diaFim - diaInicio
    W -= ajusteDia(momentoInicio, momentoFim)

    tempoEvento = calcularDiferenca(momentoInicio, momentoFim)

    print(f"{W} dia(s)")
    print(f"{tempoEvento[0]} hora(s)")
    print(f"{tempoEvento[1]} minuto(s)")
    print(f"{tempoEvento[2]} segundo(s)")

if __name__ == "__main__":
    main()