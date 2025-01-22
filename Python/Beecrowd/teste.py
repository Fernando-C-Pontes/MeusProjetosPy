def main():
    nomeCompleto = {"Nome" : "Fernando", "Sobrenome" : "Pontes"}

    for i in range(len(nomeCompleto["Nome"])):
        print(nomeCompleto["Nome"][i])
    
    for chave, nome in nomeCompleto.items():
        print(f"{chave}: {nome}")

    print(15, "julho", 1991)

if __name__ == "__main__":
    main() 