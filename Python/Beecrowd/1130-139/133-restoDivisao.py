def main():
    X, Y = int(input()), int(input())
    
    if X > Y:
        X, Y = Y, X

    for i in range(X + 1, Y):
        if i % 5 == 3 or i % 5 == 2:
            print(i)
    
if __name__ == "__main__":
    main()  