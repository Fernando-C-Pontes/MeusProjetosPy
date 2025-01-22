def main():
    nGrenais = 0
    vitorias = {"Inter" : 0, "Gremio" : 0, "Empates" : 0}
    
    while True:
        gInter, gGremio = map(int, input().split())
        nGrenais += 1

        if gInter > gGremio:
            vitorias["Inter"] += 1
        elif gInter < gGremio:
            vitorias["Gremio"] += 1
        else:
            vitorias["Empates"] +=1

        if (int(input("Novo grenal (1-sim 2-nao)\n"))) == 2:
            break

    print(f"{nGrenais} grenais")
    for chave, valor in vitorias.items():
        print(f"{chave}:{valor}")
    
    if vitorias["Inter"] == vitorias["Gremio"]:
        print("Nao houve vencedor")
    else:
        print("Inter venceu mais" if vitorias["Inter"] > vitorias["Gremio"] else "Gremio venceu mais")

if __name__ == "__main__":
    main()