if __name__ == '__main__':
    N = int(input())
    List=[]
    for i in range(N):
        c=input().split()
        if c[0]=="insert":
            List.insert(int(c[1]),int(c[2]))
        elif c[0]=="append":
            List.append(int(c[1]))
        elif c[0]=="pop":
            List.pop()
        elif c[0]=="print":
            print(List)
        elif c[0]=="remove":
            List.remove(int(c[1]))
        elif c[0]=="sort":
            List.sort()
        else:
            List.reverse()
