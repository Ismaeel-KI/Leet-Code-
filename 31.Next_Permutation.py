from sympy import elliptic_k

nums = [1, 2, 3]

def permutation(element):

    ans, sols = [], []
    n = len(element)

    def backtrack():
        if len(sols) == n:
            ans.append(sols[:])
            return

        for x in element:
            if x not in sols:
                sols.append(x)
                backtrack()
                sols.pop()

    backtrack()
    return ans



list1 = [1, 2, 3]
next_of_this = [2, 3, 1]
perm = permutation(element=list1)
print(perm)