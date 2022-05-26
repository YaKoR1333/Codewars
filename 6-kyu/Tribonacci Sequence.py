def tribonacci(signature, n):
    if n == 0:
        signature = []
        return signature
    elif n == 1:
        signature = [signature[0]]
        return signature
    elif n == 2:
        signature = [signature[0], signature[1]]
    else:
        for i in range(n-3):
            SumNumbers = sum([signature[i]+signature[i+1]+signature[i+2]])
            signature.append(SumNumbers)
    return signature
