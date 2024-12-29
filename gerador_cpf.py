import random

nove_digitos = ''

for i in range(9):  
    nove_digitos += str(random.randint(0, 9))

contagem_regressiva = 10
hd_soma = 0
for numero in nove_digitos:
   hd_soma += int(numero) * contagem_regressiva
   contagem_regressiva -= 1
resto_div = (hd_soma * 10) % 11
resultado = resto_div if resto_div <= 9 else 0

dez_digitos = nove_digitos + str(resultado)
contagem_regressiva2 = 11
hd_soma2 = 0
for numero2 in dez_digitos:
   hd_soma2 += int(numero2) * contagem_regressiva2
   contagem_regressiva2 -= 1
resto_div2 = (hd_soma2 * 10) % 11
resultado2 = resto_div2 if resto_div2 <= 9 else 0

novo_cpf = f'{nove_digitos}{resultado}{resultado2}'
print(novo_cpf)

# Edson Copque | https://linktr.ee/edsoncopque
