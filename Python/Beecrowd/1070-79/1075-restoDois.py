def main():
    N = int(input())

    for i in range(10001):
        if i % N == 2:
            print(i)

if __name__ == "__main__":
    main()