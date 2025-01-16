def main():
    contNotas = somaNotas = 0

    while True:
        nota = float(input())
        if 0 <= nota <= 10:
            somaNotas += nota
            contNotas += 1
        else:
            print("nota invalida")
        
        if contNotas == 2:
            print(f"media = {somaNotas/2:.2f}")

            while (repetir := int(input("novo calculo (1-sim 2-nao)\n"))) not in (1, 2):
                pass
                
            if repetir == 1:
                contNotas = somaNotas = 0
            elif repetir == 2:
                break

if __name__ == "__main__":
    main()