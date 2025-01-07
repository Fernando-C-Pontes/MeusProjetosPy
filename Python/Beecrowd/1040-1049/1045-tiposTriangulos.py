def main():
    A, B, C = map(float, input().split())

    A, B, C = sorted([A, B, C], reverse=True)

    if A >= B + C:
        print("NAO FORMA TRIANGULO")
    else:
        if A**2 == B**2 + C**2:
            print("TRIANGULO RETANGULO")
        elif A**2 > B**2 + C**2:
            print("TRIANGULO OBTUSANGULO")
        else: #A**2 < B**2 + C**2:
            print("TRIANGULO ACUTANGULO")

        if A == B == C:
            print("TRIANGULO EQUILATERO")
        elif A == B or A == C or B == C:
            print("TRIANGULO ISOSCELES")
    
if __name__ =="__main__":
    main()