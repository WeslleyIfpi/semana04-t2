valor1 = float(input('Digite um número Real: '))
valor2 = int(input('Digite um número inteiro'))

soma = valor1 + valor2
concat = str(valor1) + str(valor2)
mult = valor1 * valor2
multStr = str(valor1) * valor2
divisao = valor1 / valor2
divisaoInt = valor1 // valor2
expo = valor1 ** valor2
modulo = valor1 % valor2

print(f'A soma entre os números é: {soma}')
print(f'A concatenação dos numeros é: {concat}')
print(f'A multiplicação entre os números é: {mult}')
print(f'A multiplicação de string é : {multStr}')
print(f'A divisão entre os números é: {divisao}')
print(f'A divisão inteira dos números é: {divisaoInt}')
print(f'A exponenciação dos números é: {expo}')
print(f'O resto da divisão entre os números é: {modulo}')
