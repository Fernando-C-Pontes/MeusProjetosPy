def main():

    numPares = numImpar = numPosit = numNegat = 0

    for _ in range(5):
        valor = float(input().strip())
        if valor % 2 == 0:
            numPares += 1
        else:
            numImpar += 1
        
        if valor > 0:
            numPosit += 1
        elif valor < 0:
            numNegat += 1

    print(f"{numPares} valor(es) par(es)")
    print(f"{numImpar} valor(es) impar(es)")
    print(f"{numPosit} valor(es) positivo(s)")
    print(f"{numNegat} valor(es) negativo(s)")

if __name__ == "__main__":
    main()