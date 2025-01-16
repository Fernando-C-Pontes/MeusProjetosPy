def main():
    X, Y = map(int,input().split())

    while X != 0 and Y != 0:
        if X > 0:
            quadrante = "primeiro" if Y > 0 else "quarto"
        else:
            quadrante = "segundo" if Y > 0 else "terceiro"
        
        print(quadrante)
        X, Y = map(int,input().split())

if __name__ == "__main__":
    main()