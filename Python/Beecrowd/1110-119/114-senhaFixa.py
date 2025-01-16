def main():
    senha = 2002
    senhaEntrada = int(input())
    while senhaEntrada != senha:
        print("Senha Invalida")
        senhaEntrada = int(input())
    
    print("Acesso Permitido")

if __name__ == "__main__":
    main()