def digfre(s):
    frequency = [0] * 10
    for i in range(10):
        frequency[i] = s.count(str(i))
    return frequency

s = input()
result = digfre(s)
print(" ".join(map(str, result)))
