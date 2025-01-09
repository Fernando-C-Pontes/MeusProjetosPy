def main():
    renda = float(input())
    if renda <= 2000:
        imposto = 0
    elif renda <= 3000:
        imposto = (renda - 2000) * 0.08
    elif renda <= 4500:
        imposto = (1000 * 0.08) + ((renda - 3000) * 0.18)
    else:
        imposto = (1000 * 0.08) + (1500 * 0.18) + ((renda - 4500) * 0.28)

    if imposto == 0:
        print("Isento")
    else:
        print(f"R$ {imposto:.2f}")

if __name__ == "__main__":
    main()