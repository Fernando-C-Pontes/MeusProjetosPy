def main():
    numero = float(input())

    if numero < 0 or numero > 100:
        print("Fora de intervalo")
    elif numero <= 25:
        print("Intervalo [0,25]")
    elif numero <= 50:
        print("Intervalo (25,50]")
    elif numero <= 75:
        print("Intervalo (50,75]")
    else:
        print("Intervalo (75,100]")

if __name__ =="__main__":
    main()