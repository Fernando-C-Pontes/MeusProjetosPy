def main():
    a, b, c = map(int, input().split())
    
    original = [a, b, c]
    ordenada = sorted(original)

    for n in ordenada:
        print(n)
    
    print()

    for n in original:
        print(n)

if __name__ =="__main__":
    main()