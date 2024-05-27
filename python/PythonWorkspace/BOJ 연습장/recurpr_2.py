
def GCD(A, B): 
    if A%B == 0: # 15 3
        return B # 3
    elif B == 0: 
        return A
    else:
        return GCD(B, A%B) # 15. 12
        # 12,  3
        # GCD(12, 3)
        # 3


print(GCD(20, 50))


