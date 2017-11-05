def satisfiesF(L):
    clone = L[:]
    for string in clone:
        if not f(string):
            L.remove(string)
    return len(L)

def f(s):
    return 'a' in s
      
L = ['c', 'b']
print satisfiesF(L)
print L
