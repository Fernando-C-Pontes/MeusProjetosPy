def main():
    horaInicial, minutoInicial, horaFinal, minutoFinal = map(int, input().split())
    
    if minutoInicial > minutoFinal:
        tempoM = minutoFinal - minutoInicial + 60
        tempoH = -1
    else:
        tempoM = minutoFinal - minutoInicial
        tempoH = 0
    
    if horaInicial == horaFinal:
        if tempoM == 0:
            tempoH = 24
        elif minutoInicial > minutoFinal:
            tempoH += 24
        else:
            tempoH = 0
    elif horaInicial < horaFinal:
        tempoH += horaFinal - horaInicial
    else:
        tempoH += horaFinal + 24 - horaInicial

    print(f"O JOGO DUROU {tempoH} HORA(S) E {tempoM} MINUTO(S)")

if __name__ =="__main__":
    main()