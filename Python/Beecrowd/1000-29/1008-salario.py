def main():
    n = int(input())
    quatHoras = int(input())
    valor = float(input())

    salario = (quatHoras * valor)

    print("NUMBER =", n)
    print(f"SALARY = U$ {salario:.2f}")

if __name__ =="__main__":
    main()