from operacao import Operacao

class Menu:
    def __init__(self):
        self.opcao= -1
        self.opera = Operacao()
        self.num1 = 0
        self.num2 = 0
        self.num3 = 0
        self.num4 = 0

    def mostrarMenu(self):
        print('\n------- MENU -------\n\n'      +
              "Escolha uma das opções abaixo: " +
              '\n0. Sair'                       +
              '\n1. Somar'                      +
              '\n2. Subtrair'                   +
              '\n3. Dividir'                    +
              '\n4. Multiplicar'                +
              '\n5. Potência'                   +
              '\n6. Raiz'                       +
              '\n7. Tabuada'                    +
              '\n8. exercício 01'               +
              '\n9. exercício 02'               +
              '\n10. exercício 03'              +
              '\n11. exercício 04'              +
              '\n12. exercício 05'              +
              '\n13. exercício 06'              +
              '\n14. exercício 08'              +
              '\n15. exercício 09'              +
              '\n16. exercício 10'              +
              '\n17. exercício 11'              +
              '\n18. exercício 12'              +
              '\n19. exercício 13'              +
              '\n20. exercício 14'              +
              '\n21. exercício 15'              +
              '\n22. exercício 16'              +
              '\n23. exercício 17'              +
              '\n24. exercício 18'              +
              '\n25. exercício 19'              +
              '\n26. exercício 20'              +
              '\n27. Lista 2 exercício 1'               +
              '\n28. Lista 2 exercício 2'               +
              '\n29. Lista 2 exercício 3'               +
              '\n30. Lista 2 exercício 4'               +
              '\n31. Lista 2 exercicio 5'               +
              '\n32. Lista 2 exercicio 6'               +
              '\n33. Lista 2 exercicio 7'               +
              '\n34. Lista 2 exercicio 8'               +
              '\n35. Lista 2 exercicio 9'               +
              '\n36. Lista 2 exercicio 10'               +
              '\n37. Lista 2 exercicio 11'               +
              '\n38. Lista 2 exercicio 12'               +
              '\n39. Lista 2 exercicio 13'               +
              '\n40. Lista 2 exercicio 14'               +
              '\n41. Lista 2 exercicio 15'               +
              '\n42. Lista 2 exercicio 16'               +
              '\n43. Lista 2 exercicio 17'               +
              '\n44. Lista 2 exercicio 18'               +
              '\n45. Lista 2 exercicio 19'               +
              '\n46. Lista 2 exercicio 20'               )

    def coletar(self):
         self.num1 = int(input("Informe o primeiro número: "))
         self.num2 = int(input("Informe o segundo número: "))

    def coletar1(self):
        self.num1 = int(input("Informe o primeiro número: "))

    def coletar2(self):
        self.num1 = int(input("Informe a base: "))
        self.num2 = int(input("Informe a altura: "))

    def coletar3(self):
        self.num1 = int(input("Informe sua idade em anos: "))
        self.num2 = int(input("Informe sua idade em meses: "))
        self.num3 = int(input("Informe sua idade em dias: "))

    def votos(self):
        self.num1 = int(input("Informe quantos votos no total: "))
        self.num2 = int(input("Informe quantos votos em branco: "))
        self.num3 = int(input("Informe quantos votos em nulo: "))
        self.num4 = int(input("Informe quantos votos válidos: "))

    def valores(self):
        self.num1 = int(input("Informe o primeiro número: "))
        self.num2 = int(input("Informe o segundo número: "))
        self.num3 = int(input("Informe o terceiro número: "))
        self.num4 = int(input("Informe o quarto número: "))
        self.num5 = int(input("Informe o quinto número: "))
        self.num6 = int(input("Informe o sexto número: "))
        self.num7 = int(input("Informe o sétimo número: "))
        self.num8 = int(input("Informe o oitavo número: "))
        self.num9 = int(input("Informe o nono número: "))
        self.num10 = int(input("Informe o décimo número: "))

    def neg(self):
        self.num1 = int(input("Informe o primeiro número: "))
        self.num2 = int(input("Informe o segundo número: "))
        self.num3 = int(input("Informe o terceiro número: "))
        self.num4 = int(input("Informe o quarto número: "))
        self.num5 = int(input("Informe o quinto número: "))
        self.num6 = int(input("Informe o sexto número: "))
        self.num7 = int(input("Informe o sétimo número: "))
        self.num8 = int(input("Informe o oitavo número: "))
        self.num9 = int(input("Informe o nono número: "))
        self.num10 = int(input("Informe o décimo número: "))

    def quanti(self):
        self.num1 = int(input("Informe a quantidade de números: "))

    def numeros(self):
        self.num1 = int(input("Informe o primeiro número: "))
        self.num2 = int(input("Informe o segundo número: "))
        self.num3 = int(input("Informe o terceiro número: "))
        self.num4 = int(input("Informe o quarto número: "))
        self.num5 = int(input("Informe o quinto número: "))
        self.num6 = int(input("Informe o sexto número: "))
        self.num7 = int(input("Informe o sétimo número: "))
        self.num8 = int(input("Informe o oitavo número: "))
        self.num9 = int(input("Informe o nono número: "))
        self.num10 = int(input("Informe o décimo número: "))
        self.num11 = int(input("Informe o décimo primeiro número: "))
        self.num12 = int(input("Informe o décimo segundo número: "))
        self.num13 = int(input("Informe o décimo terceiro número: "))
        self.num14 = int(input("Informe o décimo quarto número: "))
        self.num15 = int(input("Informe o décimo quinto número: "))
        self.num16 = int(input("Informe o décimo sexto número: "))
        self.num17 = int(input("Informe o décimo sétimo número: "))
        self.num18 = int(input("Informe o décimo oitavo número: "))
        self.num19 = int(input("Informe o décimo nono número: "))
        self.num20 = int(input("Informe o vigéssimo número: "))

    def operacao(self):
        while self.opcao != 0:
            self.mostrarMenu()  # chamar opções
            self.opcao = int(input('Escolha uma opção acima: '))

            if self.opcao == 0:
                print('Obrigada!!!')
            if self.opcao == 1:
                self.coletar() #chamar o input por meio do coletar
                print(f'\nA soma dos números é: {self.opera.somar(self.num1,self.num2)}')

            elif self.opcao == 2:
                self.coletar()
                print(f'\nA subtração dos números é: {self.opera.subtrair(self.num1, self.num2)}')

            elif self.opcao == 3:
                self.coletar()
                print(f'\nA divisão dos números é: {self.opera.dividir(self.num1, self.num2)}')

            elif self.opcao == 4:
                self.coletar()
                print(f'\nA multiplicação dos números é: {self.opera.multiplicar(self.num1, self.num2)}')

            elif self.opcao == 5:
                self.coletar()
                print(f'\nA potência do número é: {self.opera.potencia(self.num1, self.num2)}')

            elif self.opcao == 6:
                self.coletar()
                print(f'\nA raiz de {self.num1}  é: {self.opera.raiz(self.num1)}')
                print(f'\nA raiz de {self.num2}  é: {self.opera.raiz1(self.num2)}')

            elif self.opcao == 7:
                self.coletar()
                print(f'\nA tabuada do {self.num1} é: {self.opera.raiz(self.num1)}')
                print(f'\nA tabuada do  {self.num2} número é: {self.opera.raiz(self.num1)}')

            elif self.opcao == 8:
               print(f'\n Os valores de 1 ate 10 é: {self.opera.exercicio01()}')

            elif self.opcao == 9:
               print(f'\n Os valores pares de 1 ate 20 é: {self.opera.exercicio02()}')

            elif self.opcao == 10:
               print(f'\n O da soma de 1 ate 100 é: {self.opera.exercicio03()}')

            elif self.opcao == 11:
               print(f'\n Os multiplos de 5 de 1 ate 50 é: {self.opera.exercicio04()}')

            elif self.opcao == 12:
               self.coletar1()
               print(f'\n O número digitado é: {self.opera.exercicio05(self.num1)}')

            elif self.opcao == 13:
               self.coletar1()
               print(f'\n O número digitado é: {self.opera.exercicio06(self.num1)}')

            elif self.opcao == 14:
               self.coletar1()
               print(f'\n  {self.opera.exercicio08(self.num1)}')

            elif self.opcao == 15:
               self.coletar1()
               print(f'\n  {self.opera.exercicio09(self.num1)}')

            elif self.opcao == 16:
               print(self.opera.exercicio10())

            elif self.opcao == 17:
               self.coletar1()
               print(f'\n  {self.opera.exercicio11(self.num1)}')


            elif self.opcao == 18:
                self.coletar1()
                print(f'\n :  {self.opera.exercicio12(self.num1)}')

            elif self.opcao == 19:
                self.coletar1()
                print(f'\n :  {self.opera.exercicio13()}')

            elif self.opcao == 20:
                self.coletar1()
                print(f'\n{self.opera.exercicio14(self.num1)}\n')

            elif self.opcao == 21:
                self.coletar1()
                print(f'\n A soma dos digitos é:  {self.opera.exercicio15(self.num1)}')

            elif self.opcao == 22:
                self.coletar1()
                print(f'\n  {self.opera.exercicio16(self.num1)}')

            elif self.opcao == 23:
                self.coletar1()
                print(f'\n  {self.opera.exercicio17(self.num1)}')

            elif self.opcao == 24:
                self.coletar1()
                print(f'\n  {self.opera.exercicio18(self.num1)}')

            elif self.opcao == 25:
                self.coletar1()
                print(f'\n{self.opera.exercicio19(self.num1)}\n')

            elif self.opcao == 26:
                self.coletar1()
                print(f'\n  {self.opera.exercicio20(self.num1)}')

            #lista 2

            elif self.opcao == 27:
                self.coletar()
                print('Variável A:', {self.num2}, 'Variável B:', {self.num1})

            elif self.opcao == 28:
                self.coletar1()
                print(f'\n {self.opera.exercicio2(self.num1)}')

            elif self.opcao == 29:
                self.coletar2()
                print(f'\n  A área do retângulo é de {self.opera.exercicio3(self.num1, self.num2)}')

            elif self.opcao == 30:
                self.coletar3()
                print(f' A idade em dias é {self.opera.exercicio4(self.num1, self.num2,self.num3)}')

            elif self.opcao == 31:
                self.votos()
                print(f'\n  {self.opera.exercicio5(self.num1, self.num2, self.num3, self.num4)}')


            elif self.opcao == 33:
                self.num1  = int(input('Informe o custo de fábrica do carro: '))
                print(f'O custo do carro para o consumidor é de: {self.opera.exercicio7(self.num1)}')

            elif self.opcao == 34:
                self.num1 = int(input("Informe a primeira nota: "))
                self.num2 = int(input("Informe a segunda nota: "))
                self.num3 = int(input("Informe a terceira nota: "))
                print(f' A média do aluno é de {self.opera.exercicio8(self.num1,self.num2,self.num3)}')

            elif self.opcao == 35:
                self.num1 = int(input("Informe o número de maças: "))
                print(f' O valor que tem que ser pago será de {self.opera.exercicio9(self.num1)}')


            elif self.opcao == 36:
                self.valores()
                print(
                    f'\n  {self.opera.exercicio010(self.num1, self.num2, self.num3, self.num4, self.num5, self.num6, self.num7, self.num8, self.num9, self.num10)}')


            elif self.opcao == 37:
                self.num1 = int(input("Informe o valor da comissão: "))
                self.num2 = int(input("Informe o valor do salario: "))
                print(f'O valor que o funcionario deverá receber é de: {self.opera.exercicio011(self.num1, self.num2)}')

            elif self.opcao == 38:
                self.num1 = int(input("Informe o saldo da conta: "))
                self.num2 = int(input("Informe o débito: "))
                self.num3 = int(input("Informe o crédito: "))
                print(self.opera.exercicio012(self.num1,self.num2,self.num3,self.num4))




            elif self.opcao == 40:
                self.num1 = int(input("Informe um número: "))
                print(self.opera.exercicio014(self.num1))

            elif self.opcao == 41:
                self.neg()
                print(
                    f'\n  {self.opera.exercicio015(self.num1, self.num2, self.num3, self.num4, self.num5, self.num6, self.num7, self.num8, self.num9, self.num10)}')

            elif self.opcao == 42:
                self.neg()
                print(
                    f'A soma dos numeros menores que 40 é: \n  {self.opera.exercicio016(self.num1, self.num2, self.num3, self.num4, self.num5, self.num6, self.num7, self.num8, self.num9, self.num10)}')


            elif self.opcao == 43:
                print(f'\n  {self.opera.exercicio017()}')

            elif self.opcao == 44:
                self.quanti()
                print(f'\n  {self.opera.exercicio018(self.num1)}')


            elif self.opcao == 45:
                self.numeros()
                print(
                    f'\n  {self.opera.exercicio019(self.num1, self.num2, self.num3, self.num4, self.num5, self.num6, self.num7, self.num8, self.num9, self.num10, self.num11, self.num12, self.num13, self.num14, self.num15, self.num16, self.num17, self.num18, self.num19, self.num20)}')


            elif self.opcao == 46:
                print(f'\n  {self.opera.exercicio020()}')
