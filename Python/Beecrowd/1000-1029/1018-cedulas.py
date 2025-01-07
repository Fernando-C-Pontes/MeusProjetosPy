def main():
    valor = int(input())
    notas = [100, 50, 20, 10, 5, 2, 1]

    if valor < 0:
        return
    
    print(valor)

    for n in notas:
        quant = valor//n
        print(f"{quant} nota(s) de R$ {n},00")
        valor %= n

if __name__ =="__main__":
    main()