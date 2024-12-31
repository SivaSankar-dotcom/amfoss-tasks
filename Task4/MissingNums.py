from collections import Counter
def missnum(a,b):
    c1=Counter(a)
    c2=Counter(b)
    c=c2-c1
    d=sorted(c.keys())
    o=" ".join(map(str, d))
    print(o)
    
a=[]
n=int(input())
a = list(map(int, input().split()))

b=[]    
m=int(input())
b = list(map(int, input().split()))
missnum(a,b)
