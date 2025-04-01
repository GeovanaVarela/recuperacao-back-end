# Dado um array de números inteiros, conte quantos são pares e quantos são ímpares
def contar_pares_ímpares(array)
pares =0
ímpares =0

for num in array:
    if num % 2 == 0:
        pares += 1
        else:
            ímpares += 1
             
             return pares,ímpares
