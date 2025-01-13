def main():
    valor = int(input())

    if valor % 2 == 0:
        valor += 1
    
    print (valor)

    for _ in range(5):
        valor += 2
        print(valor)
    
if __name__ == "__main__":
    main()