def main():
    N = int(input())

    for i in range(1, N+1):
        if i % 2 == 0:
            print(f"{i}^2 = {i ** 2 :.0f}")

if __name__ == "__main__":
    main()