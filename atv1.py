lista1 = [1,2,3,4,5,6,7,8,9,10]
lista2 = []

for i in range(len(lista1)):
    if lista1[i] % 2 == 0:
        lista2.append(lista1[i])
print(lista2)