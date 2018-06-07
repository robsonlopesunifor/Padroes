lista = ['a',2,'bb',8,'cc']

lista = [['a','b','c'],[1,2,3],[]]

lista = ['a',2,'bb',8,'cc']

lista[0] # primeiro elemento
lista[-1] # ultimo elemento

lista = lista + [11] # ou lista += [11] adiciona no final 
lista = [0] + lista # adiciona no começo


# percorrendo lista ------------------------------------------------
lista_nums = [100,200,300,400]
for item in lista_nums:
    print(item)

# percorrendo lista por indece -------------------------------------------------
lista_nums = [100,200,300,400]
for idx,item in enumerate(lista_nums):
    lista_nums[idx] += 1000
print(lista_nums)

# Fatiano lista ----------------------------------------------------

lista = "python" # ou ['p','y','t','h','o','n']
lista[0] # p
lista[:2] # py
lista[2:] # thon
lista[::2] # pto
lista[2::2] # to
lista[::-1] # nohtyp

# Incluindo, alterando e excluindo elementos  ----------------------

lista = ['p','y','t','h','o','n']
lista.append('!') # ['p','y','t','h','o','n','!']
lista.insert(0,'$') # ['$','p','y','t','h','o','n','!']
lista[0] = '%' # ['%','p','y','t','h','o','n','!']
lista.clear() # []
lista = ['p','y','t','h','o','n']
lista.pop() # 'n' # ['p','y','t','h','o']
lista.pop(0) # 'p' # ['y','t','h','o'] 
del(lista[1::1]) # ['y','o']

# ordenamento de lista

lista.reverse() # inverter a ordem dos elementos;
lista.sort() # ordenar por valor; sort(reverse=True) ordena ao contrario 
lista.extend(lista) # concatenar com outra lista;
lista.index(elemento) # descobrir a posição de um elemento;
lista.clear() # apagar todos os elementos da lista.
list(set(a)) # [5,5,5,6,6,6] >>> [5,6]

# quantidade de elemento

lista = ['p','y','t','h','o','n']
lista.count('p') # 1

# IN e NOT IN

2 in (1,2,3,4,5) # True
2 not in (1,2,3,4,5) # False

if 2 in range(1, 6): 
    print("contido")
else:
    print("nao contido")

# conjunto de valores estam contidos AND OR e IN

(3 and 5) in range(1, 6) # true
(2 or 10) in range(1, 6) # true
(10 or 2) in range(1, 6) # false















