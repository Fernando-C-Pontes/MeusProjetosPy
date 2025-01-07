def main():
    horaInicial, horaFinal = map(int, input().split())

    if horaInicial == horaFinal:
        tempo = 24
    elif horaInicial < horaFinal:
        tempo = horaFinal - horaInicial
    else:
        tempo = horaFinal + 24 - horaInicial

    print(f"O JOGO DUROU {tempo} HORA(S)")

if __name__ =="__main__":
    main()