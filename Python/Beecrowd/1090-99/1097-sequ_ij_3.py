def main():

    for i in range(1, 10, 2):
        for j in range(7 + (i -1), 4 + (i - 1), -1):
            print(f"I={i} J={j}")

if __name__ == "__main__":
    main()