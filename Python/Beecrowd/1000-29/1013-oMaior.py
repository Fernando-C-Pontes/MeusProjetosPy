#1013
def main():
    a, b, c = map(int, input().split())

    maiorAB = (a + b + abs(a - b)) // 2
    maior = (maiorAB + c + abs(maiorAB - c)) // 2
    print(maior, "eh o maior")

if __name__ =="__main__":
    main()