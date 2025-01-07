#1015
def main():
    x1, y1 = map(float, input().split())
    x2, y2 = map(float, input().split())

    distancia = (((x2 - x1)**2)+((y2 - y1)**2))**0.5

    print(f"{distancia:.4f}")

if __name__ =="__main__":
    main()