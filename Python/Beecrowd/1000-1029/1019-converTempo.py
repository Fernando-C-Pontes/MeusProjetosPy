def main():
    N = int(input())
    divisores = [3600, 60, 1]
    resultado = []

    for n in divisores:
        resultado.append(N // n)
        N %= n
    
    h, m, s = resultado
    print(f"{h}:{m}:{s}")
    

if __name__ =="__main__":
    main()