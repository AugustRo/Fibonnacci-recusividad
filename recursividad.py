def Fibonnacci(n):
    if n == 1 or n == 0:
        return 1
    return Fibonnacci(n-1) + Fibonnacci(n-2)

n= int(input("Escribe el numero que desea:"))
print(f'El número Fibonnacci para {n} es {Fibonnacci(n)}')