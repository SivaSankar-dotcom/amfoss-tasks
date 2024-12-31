k=int(input())
sett=list(map(int,input().split()))
set1=set()
set2=set()
for i in sett:
    if i not in set1:
        set1.add(i)
        set2.add(i)
    else:
        set2.discard(i)
set2=list(set2)
print(set2[0])
