import sys
sys.setrecursionlimit(10**9)
N = int(input())
def getMoo(n, moo):
    n -= 1
    if n == 0:
        return "moo"

    moo = getMoo(n-1, moo) + "m"+"o"*(n+2) + getMoo(n-1, moo)
    return moo

moo = getMoo(N, "")
print(moo[N])