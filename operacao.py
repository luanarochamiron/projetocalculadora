import math

class Operacao:
    def __init__(self):
        self.num = 0
        self.num1 = 0
        self.num2 = 0
        self.num3 = 0
        self.num4 = 0

    def coletar(self,num1, num2):
        self.num1 = num1
        self.num2 = num2

    def somar(self,num1,num2):
        self.coletar(num1,num2) #Utilizando o método coletar
        return self.num1 + self.num2

    def subtrair(self,num1,num2):
        self.coletar(num1,num2)
        return self.num1 - self.num2

    def multiplicar(self,num1,num2):
        self.coletar(num1,num2)
        return self.num1 * self.num2

    def dividir(self,num1,num2):
        self.coletar(num1,num2)
        if self.num2 <= 0:
            return 'impossível dividir'
        else:
           return self.num1 / self.num2

    def tabuada(self,num1):
        resultado = ""
        for i in range(0,11,1):
            resultado += f'\n{num1} * {i} = {num1 * i}'
        return resultado

    def tabuada2(self,num2):
        resultado = ""
        for i in range(0,11,1):
            resultado += f'\n{num2} * {i} = {num2 * i}'
        return resultado

    def potencia(self, base, expoente):
        return pow(base, expoente)

    def raiz(self,num1):
        return math.sqrt(num1)

    def raiz1(self,num2):
        return math.sqrt(num2)

    def exercicio01(self):
        resultado = ""
        for i in range(1, 11, 1):
            resultado += f'\n{i}'
        return resultado

    def exercicio02(self):
        par = ""
        for i in range(1, 21, 1):
            if i % 2 == 0:
               par += f'\n{i}'
        return par

    def exercicio03(self):
        soma = sum(range(1, 101, 1))
        return soma

    def exercicio04(self):
        multi = ""
        for i in range(1, 51, 1):
            if i % 5 == 0:
               multi += f'\n{i}'
        return multi

    def exercicio05(self,num1):
        if num1 % 2 == 0:
         return f'O número é par'
        else:
            return f'O número é impar'

    def exercicio06(self,num1):
        if num1 % 2 == 0:
         return f'O número é par'
        elif num1 < 0:
            return f'O número é negativo'
        else:
            return f'O número é impar'

    def exercicio08(self,num1):
        multi = ""
        for i in range(1, num1 + 1, 1):
                multi += f'\n{i}'
        return multi

    def exercicio09(self,num1):
        soma = sum(range(1, num1 + 1, 1))
        return soma

    def exercicio10(self):
        primo = "1\n2\n3\n5"
        for i in range(5, 21, 1):
            if i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
                primo += f'\n{i}'
        return primo

    def exercicio11(self, num1):
        if num1 == 2 or num1 == 3 or num1 == 5:
            return f'O{num1} é primo!'
        elif num1 % 2 != 0 and num1 % 3 != 0 and num1 % 5 != 0:
            return f'O {num1} é primo!'
        return f'O {num1} não é primo!'

    def exercicio12(self, num1):
        resultado = 1
        if num1 < 0:
            return  ValueError("O fatorial não está definido para números negativos")
        for i in range(1, num1 + 1):
            resultado *= i
        return resultado

    def exercicio13(self):
        numero = 1
        numero_anterior = 0
        for _ in range(10):
            print(numero)
            aux = numero
            numero += numero_anterior
            numero_anterior = aux

    def é_quadrado_perfeito(self, num):
        if num < 0:
            return f'não existe'
        raiz = int(math.sqrt(num))
        return raiz * raiz == num

    def exercicio14(self, num1):
        if self.é_quadrado_perfeito(5 * (num1 * num1) + 4) or self.é_quadrado_perfeito(5 * (num1 * num1) - 4):
            return f'O {num1} faz parte da sequência de Fibonacci!'
        else:
            return f'O {num1} não faz parte da sequência de Fibonacci.'

    def exercicio15(self, num1):
        s = 0
        while num1:
            s += num1 % 10
            num1 //= 10
        return 's'

    def exercicio16(self, num1):
        pares = ""
        impar = ""
        for i in range(1, num1 + 1):
            if i % 2 == 0:
                pares += f'\n{i}'
            else:
                impar += f'\n{i}'
        resultado = (f'Números pares:{pares}\nNúmeros ímpares:{impar}')
        return resultado

    def exercicio17(self,num1):
        primo = "1\n2\n3\n5"
        for i in range(5, num1 + 1, 1):
            if i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
                primo += f'\n{i}'
        return primo


    def exercicio18(self,num1):
        sequence = []
        while num1 != 1:
            sequence.append(num1)
            if num1 % 2 == 0:
                num1 = num1 // 2
            else:
                num1 = num1 * 3 + 1
        sequence.append(1)
        return sequence

    def exercicio19(self, num1):
        soma_pares = 0
        soma_impares = 0

        for i in range(1, num1 + 1):
            if i % 2 == 0:
                soma_pares += i
            else:
                soma_impares += i

        resultado = (f'A soma dos números pares é: {soma_pares}\n'
                     f'A soma dos números ímpares é: {soma_impares}')
        return resultado

    def exercicio20(self, num1):
        perfeito = 0
        for i in range(1,num1):
            if num1 % i == 0:
                perfeito += i
        if perfeito == num1:
            return "é um número perfeito"
        else:
            return "não é um número perfeito"

        #lista 2

    def exercicio1(self):
        troca = num1
        num1 = num2
        num2 = troca

    def exercicio2(self, num1):
        ant = num1 - 1
        return ant

    def exercicio3(self, num1, num2):
        return num1 * num2

    def exercicio5(self, num1, num2, num3, num4):
        branco = (100 * num2) / num1
        nulo = (100 * num3) / num1
        valido = (100 * num4) / num1

        return (f'O percentual dos votos brancos :{branco}\n'
                f'O percentual dos votos nulos   :{nulo}\n'
                f'O percentual dos votos valido  :{valido}\n')


    def exercicio4(self, num1, num2,num3):
        idade = (num1 * 365) + (num2 * 30) + num3
        return idade

    # exercicio 5 lista 2

    def exercicio7(self, num1):
        num2 = num1 * 0.28
        num3 = num1 * 0.45
        soma = num2 + num3
        return soma

    def exercicio8(self, num1,num2,num3):
        soma = num1 + num2 + num3
        media = soma / 3
        return media

    def exercicio9(self, num1):
        if num1 <= 12:
            valor = num1 * 1.30
        else:
            valor = num1 * 1
        return valor

    def exercicio010(self, num1, num2, num3, num4, num5, num6, num7, num8, num9, num10):
        valores = [num1, num2, num3, num4, num5, num6, num7, num8, num9, num10]
        valores_unicos = list(set(valores))
        valores_unicos.sort()

        return valores_unicos
    def exercicio012(self, num1,num2,num3,num4):
        num4 = (num1 - num2) + num3
        if num4 < 0:
            return f'Saldo negativo'
        else:
            return f'Saldo Positivo'

    def exercicio011(self, num1,num2):
        if num1 <= 1500:
            num1 * 0.03
        else:
            num1 > 1500 * 0.05
        soma = num1 + num2
        return soma


    def exercicio014(self,num1):
        lista = []
        for i in range (1, num1 + 1):
            lista.append(i)
        return lista

    def exercicio015(self, num1, num2, num3, num4, num5, num6, num7, num8, num9, num10):
        neg = 0
        for num in [num1, num2, num3, num4, num5, num6, num7, num8, num9, num10]:
            if num < 0:
                neg += 1
        return f'{neg} números negativos'

    def exercicio016(self, num1, num2, num3, num4, num5, num6, num7, num8, num9, num10):
        numeros = [num1, num2, num3, num4, num5, num6, num7, num8, num9, num10]

        soma = sum(numero for numero in numeros if numero < 40)

        return soma

    def exercicio017(self):
        soma = sum(range(15, 100 + 1))
        quantidade = 100 - 15 + 1
        media = soma / quantidade
        return f"A média aritmética dos números  entre 15 e 101 é {media}"

    def exercicio018(self, num1):
        quant = num1
        soma = 0
        maior = float('-inf')

        for i in range(quant):
            num = int(input("Informe um número: "))
            if num > maior:
                maior = num
            soma += num

        media = soma / quant

        return (f'O maior número: {maior}\n'
                f'A média dos números é: {media:.2f}\n')

    def exercicio019(self, num1, num2, num3, num4, num5, num6, num7, num8, num9, num10, num11, num12, num13, num14,
                    num15, num16, num17, num18, num19, num20):

        notas = [num1, num2, num3, num4, num5, num6, num7, num8, num9, num10,
                 num11, num12, num13, num14, num15, num16, num17, num18, num19, num20]

        soma = sum(notas)

        media = soma / len(notas)

        acimaMedia = sum(1 for nota in notas if nota > media)

        return (f'A média da turma: {media:.2f}\n'
                f'Quantidade de alunos com nota acima da média: {acimaMedia}')

    def exercicio020(self):
        soma_salarios = 0
        soma_filhos = 0
        maior_salario = float('-inf')
        contagem = 0
        contagem_salario_baixo = 0

        while True:
            salario = float(input("Digite o salário: "))

            if salario < 0:
                break

            filhos = int(input("Digite a quantidade de filhos: "))

            soma_salarios += salario
            soma_filhos += filhos
            contagem += 1

        if salario > maior_salario:
            maior_salario = salario

        if salario < 150:
            contagem_salario_baixo += 1

        if contagem > 0:
            media_salarios = soma_salarios / contagem
            media_filhos = soma_filhos / contagem
            percentual_salario_baixo = (contagem_salario_baixo / contagem) * 100
        else:
            media_salarios = 0
            media_filhos = 0
            percentual_salario_baixo = 0

        return (f"Média do salário: R$ {media_salarios:.2f}\n"
                f"Média  de filhos: {media_filhos:.2f}\n"
                f"Maior salário dos habitantes: R$ {maior_salario:.2f}\ns"
                f"Percentual de pessoas com salário menor que R$ 150,00: {percentual_salario_baixo:.2f}%")