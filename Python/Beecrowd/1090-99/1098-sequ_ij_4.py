def main():
    i = 0

    while i < 2:
        for j in range(1, 4):
            print(f"I={i:.0f} J={j+i:.0f}" if (j + i) % 1 == 0 else f"I={i:.1f} J={j + i:.1f}")
        i += 0.2

if __name__ == "__main__":
    main()