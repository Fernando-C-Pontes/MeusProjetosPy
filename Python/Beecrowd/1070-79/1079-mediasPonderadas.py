def main():
    N = int(input())

    for _ in range(N):
        A, B, C = map(float, input().split())
        R = (A*2+B*3+C*5)/10
        print(f"{R:.1f}")

if __name__ == "__main__":
    main()