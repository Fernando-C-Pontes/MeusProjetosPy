def main():
    n, m = map(int, input().split())

    adjTr = [[] for _ in range(n)]

    for _ in range(m):
        u, v = map(int, input().split())
        adjTr[v].append(u)

    for lista in adjTr:
        lista.sort()
    
    for i in range(n):
        print(f"{i}: {' '.join(map(str, adjTr[i]))}")
    
if __name__ == "__main__":
    main()