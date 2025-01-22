def main():
    contNotas = somaNotas = 0
    while contNotas < 2:
        nota = float(input())
        if nota < 0 or nota > 10:
            print("nota invalida")
        else:
            somaNotas += nota
            contNotas += 1
    
    print(f"media = {somaNotas/2:.2f}")

if __name__ == "__main__":
    main()