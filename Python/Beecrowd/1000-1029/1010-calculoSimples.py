#1010
def main():
    codigo1, quantidade1, valor1 = input().split()
    codigo2, quantidade2, valor2 = input().split()
    codigo1, quantidade1, codigo2, quantidade2 = map(int, [codigo1, quantidade1, codigo2, quantidade2])
    valor1, valor2 = map(float, [valor1, valor2])

    valor_pagar = quantidade1 * valor1 + quantidade2 * valor2

    print(f"VALOR A PAGAR: R$ {valor_pagar:.2f}")

if __name__ =="__main__":
    main()