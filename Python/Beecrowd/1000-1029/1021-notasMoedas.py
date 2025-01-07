def main():
    N = float(input())

    if N < 0:
        return
    Ncentavos = N*100
    notas =[100, 50, 20, 10, 5, 2]
    resultadoN = []

    print("NOTAS:")
    for n in notas:
        quant = Ncentavos//(n*100)
        print(f"{quant:.0f} nota(s) de R$ {n:.2f}")
        Ncentavos %= (n * 100)
    
    moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]
    resultadoM = []

    print("MOEDAS:")
    for m in moedas:
        quant = Ncentavos//(m*100)
        print(f"{quant:.0f} moeda(s) de R$ {m:.2f}")
        Ncentavos %= (m * 100)

if __name__ =="__main__":
    main()