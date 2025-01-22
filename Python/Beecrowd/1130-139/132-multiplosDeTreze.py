def main():
    X, Y = int(input()), int(input())
    soma = 0
    
    if X > Y:
        X, Y = Y, X

    soma = sum(i for i in range(X, Y+1) if i % 13 != 0)

    print(soma)

if __name__ == "__main__":
    main()