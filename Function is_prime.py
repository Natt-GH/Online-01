def is_prime(n):
    if n == 1: return False
    for k in range(2, n):
            if n%k == 0:
                    return True
    return True
            
print(is_prime(187))

