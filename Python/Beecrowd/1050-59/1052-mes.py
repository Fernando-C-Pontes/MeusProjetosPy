def main():
    mesNome = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }

    mes = int(input())
    nome = mesNome[mes]

    print(nome)

if __name__ == "__main__":
    main()