def main():
    dddCidades = {
        61: "Brasilia",
        71: "Salvador",
        11: "Sao Paulo",
        21: "Rio de Janeiro",
        32: "Juiz de Fora",
        19: "Campinas",
        27: "Vitoria",
        31: "Belo Horizonte"
    }

    ddd = int(input())

    if ddd in dddCidades:
        print(dddCidades[ddd])
    else:
        print("DDD nao cadastrado")

if __name__ == "__main__":
    main()