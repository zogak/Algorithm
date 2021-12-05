'''
46. permutations
'''

results = []
prev_elements=[]

def dfs(elements):
    print('in', elements)
    if len(elements) == 0:
        results.append(prev_elements[:])
        print('results:' ,results)

    for e in elements:
        print('e:', e)
        next_elements = elements[:]
        print('next1: ', next_elements)
        next_elements.remove(e)
        print('next2: ', next_elements)

        prev_elements.append(e)
        print('prev1: ', prev_elements)
        dfs(next_elements)
        print('dfs finish')
        prev_elements.pop()
        print('prev2: ', prev_elements)


dfs([1, 2])
print(results)