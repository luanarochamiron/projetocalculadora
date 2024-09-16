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

    def exercicio4(self, num1, num2,num3):
        idade = (num1 * 365) + (num2 * 30) + num3
        return idade

    # exercicio 5 lista 2
    def transformar(self, num, num4):
        percentual = (num / num4) * 100
        return percentual

    def exercicio5(self, num1, num2, num3, num4):
        # Verificar se o total é igual a brancos, validos e nulos
        if ((num1 + num2 + num3) == num4):
            transformar(num1, num4) == self.brancos
            transformar(num2, num4) == self.nulos
            transformar(num3, num4) == self.validos
            return 'Votos Brancos: {}%\nVotos Nulos: {}%\nVotos Validos: {}%'.format(self.brancos, self.nulos, self.validos)


