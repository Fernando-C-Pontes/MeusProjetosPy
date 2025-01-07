def main():
    A, B = map(int, input().split())

    if A == 0 and B == 0:
        print("Sao Multiplos")
    elif A == 0 or B == 0:
        print("Nao sao Multiplos")
    elif A % B == 0 or B % A == 0:
        print("Sao Multiplos")
    else:
        print("Nao sao Multiplos")

if __name__ =="__main__":
    main()