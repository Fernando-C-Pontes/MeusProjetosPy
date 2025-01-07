def main():
    tempo = int(input())
    velMedia = int(input())

    rendimento = 12 #Km/L
    distancia = velMedia * tempo
    litros = distancia/rendimento

    print(f"{litros:.3f}")

if __name__ =="__main__":
    main()