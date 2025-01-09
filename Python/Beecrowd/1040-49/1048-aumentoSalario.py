def main():
    salario = float(input())
    faixa = [0, 400.00, 800.00, 1200.00, 2000.00]
    reajuste = [1.15, 1.12, 1.10, 1.07, 1.04]

    for n in range(4, -1, -1):
        if salario > faixa[n]:
            novoSalario = salario * reajuste[n]
            reajusteGanho = novoSalario - salario
            percentual = (reajuste[n] - 1) * 100
            break
    
    print(f"Novo salario: {novoSalario:.2f}")
    print(f"Reajuste ganho: {reajusteGanho:.2f}")
    print(f"Em percentual: {percentual:.0f} %")

if __name__ =="__main__":
    main()