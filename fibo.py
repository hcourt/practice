def nacci(a, b, n):
    if n == 0: return []
    c = a + b
    return [c] + nacci(b, c, n - 1)

def fibonacci_sequence(seed1, seed2, n):
    if n > 1:
        return [seed1, seed2] + nacci(seed1, seed2, n - 2)
    elif n == 1:
        return [seed1]
    else: return []

def fibonacci_number(seed1, seed2, n):
    return fibonacci_sequence(seed1, seed2, n) [-1]

def fast_fibo(seed1, seed2, n):
    def matpow(m, n):
        if (n > 1):
            m = matpow(m, n/2)
            m = m * m
        elif (n % 2 == 1):
            m = m * [[1,1],[1,0]]
    matrix = [[1, 0],[0, 1]]
    matrix = matpow(matrix, n-1)
    return matrix[0][0]

#print fibonacci_sequence(0, 1, 25)
print fibonacci_number(0, 1, 45)
print fast_fibo(0, 1, 45)
