def main():
    A, B, C = map(float, input().split())

    det = (B**2)-4*A*C
    if (det) < 0 or A == 0:
        print("Impossivel calcular")
        return
    
    R1 = (-B+(det)**0.5)/(2*A)
    R2 = (-B-(det)**0.5)/(2*A)

    print(f"R1 = {R1:.5f}")
    print(f"R2 = {R2:.5f}")

if __name__ =="__main__":
    main()