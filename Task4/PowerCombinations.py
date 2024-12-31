def powerSum(X, N):
    def finds(total, power, num):
        val = total - num**power
        if val == 0:
            return 1
        if val < 0:
            return 0

        return finds(val, power, num+1) + finds(total, power, num+1)

    return helper(X, N, 1)

X=int(input())
N=int(input())

print(powerSum(X,N))
