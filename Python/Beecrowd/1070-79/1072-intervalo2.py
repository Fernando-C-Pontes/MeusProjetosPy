def main():
    N = int(input())
    dentro = fora = 0

    for _ in range(N):
        valor = int(input())
        if valor >= 10 and valor <= 20:
            dentro += 1
        else:
            fora += 1
    
    print(f"{dentro} in")
    print(f"{fora} out")

if __name__ == "__main__":
    main()