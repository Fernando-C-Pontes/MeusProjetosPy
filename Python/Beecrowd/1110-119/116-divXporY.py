def main():
    N = int(input())

    for _ in range(N):
        X, Y = map(int, input().split())
        
        if Y == 0:
            print("divisao impossivel")
        else:
            print(f"{X/Y:.1f}")

if __name__ == "__main__":
    main()