def main():
    A, B, C = map(float, input().split())

    if A+B > C and B+C > A and A+C > B:
        perimetro = A + B + C
        print(f"Perimetro = {perimetro:.1f}")
    else:
        area = ((A + B) * C) / 2
        print(f"Area = {area:.1f}")

if __name__ =="__main__":
    main()