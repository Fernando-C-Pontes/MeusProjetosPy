def main():
    nome = str(input())
    salarioFixo = float(input())
    totalVEndas = float(input())

    bonus = totalVEndas*0.15

    total = salarioFixo + bonus

    print(f"TOTAL = R$ {total:.2f}")

if __name__ =="__main__":
    main()