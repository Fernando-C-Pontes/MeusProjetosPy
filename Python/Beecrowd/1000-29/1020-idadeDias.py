def main():
    N = int(input())

    divisores =[365, 30, 1]
    resultado = []

    for n in divisores:
        resultado.append(N // n)
        N %= n
    
    ano, mes, dias = resultado
    print(f"{ano} ano(s)")
    print(f"{mes} mes(es)")
    print(f"{dias} dia(s)")

if __name__ =="__main__":
    main()