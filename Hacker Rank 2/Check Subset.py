testcase = int(input())
for i in range(testcase):
    aSize = int(input())
    a = set(input().split())
    bSize = int(input())
    b=set(input().split())
    print(a.issubset(b))
