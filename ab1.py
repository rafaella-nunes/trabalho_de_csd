class Node:
    data = None
    next = None

    def __init__(self, item):
        self.item = item


class Stack:
    def __init__(self):
        self.top = None
        self._size = 0

    def isEmpty(self):
        return self._size == 0

    def push(self, elem):
        # insere um elemento na pilha
        node = Node(elem)
        node.next = self.top
        self.top = node
        self._size = self._size + 1

    def pop(self):
        # remove o elemento do topo da pilha
        if self._size > 0:
            node = self.top
            self.top = self.top.next
            self._size = self._size - 1
            return node.data
        raise IndexError("The stack is empty")

    def peek(self):
        # retorna o topo sem remover
        if self._size > 0:
            return self.top.data
        raise IndexError("The stack is empty")

    def __len__(self):
        """Retorna o tamanho da lista"""
        return self._size

    def __repr__(self):
        r = ""
        pointer = self.top
        while (pointer):
            r = r + str(pointer.data) + "\n"
            pointer = pointer.next
        return r

    def __str__(self):
        return self.__repr__()


def medidas_de_inf():
    print('Digite 1 para converter byte para outra unidade.')
    print('Digite 2 para converter kilobyte para outra unidade.')
    print('Digite 3 para converter megabyte para outra unidade.')
    print('Digite 4 para converter gigabyte para outra unidade.')
    print('Digite 5 para converter terabyte para outra unidade.')
    opc = int(input('Digite a opcao: '))

    if opc == 1:
        # byte = float(input('Digite a medida em byte; '))
        print('Digite 1 para converter para kilobyte.')
        print('Digite 2 para converter para megabyte.')
        print('Digite 3 para converter para gigabyte.')
        print('Digite 4 para converter para terabyte.')
        unid = int(input('Digite a opcao: '))
        if unid == 1:
            byte = float(input('Digite a medida em byte; '))
            kb = byte / 1000
            print('O valor em kilobytes eh: ', kb)
        elif unid == 2:
            byte = float(input('Digite a medida em byte; '))
            mb = byte / 1000000
            print('O valor em megabytes eh: ', mb)
        elif unid == 3:
            byte = float(input('Digite a medida em byte; '))
            gb = byte / 1000000000
            print('O valor em gigabytes eh: ', gb)
        elif unid == 4:
            byte = float(input('Digite a medida em byte; '))
            tb = byte / 1000000000000
            print('O valor em terabytes eh: ', tb)
        else:
            print('Valor invalido')

    elif opc == 2:
        # byte = float(input('Digite a medida em byte; '))
        print('Digite 1 para converter para byte.')
        print('Digite 2 para converter para megabyte.')
        print('Digite 3 para converter para gigabyte.')
        print('Digite 4 para converter para terabyte.')
        unid = int(input('Digite a opcao: '))
        if unid == 1:
            kb = float(input('Digite a medida em kilobyte; '))
            byte = kb * 1000
            print('O valor em bytes eh: ', byte)
        elif unid == 2:
            kb = float(input('Digite a medida em kilobyte; '))
            mb = kb / 1000
            print('O valor em megabytes eh: ', mb)
        elif unid == 3:
            kb = float(input('Digite a medida em kilobyte; '))
            gb = kb / 1000000
            print('O valor em gigabytes eh: ', gb)
        elif unid == 4:
            kb = float(input('Digite a medida em kilobyte; '))
            tb = kb / 1000000000
            print('O valor em terabytes eh: ', tb)
        else:
            print('Valor invalido')

    elif opc == 3:
        print('Digite 1 para converter para byte.')
        print('Digite 2 para converter para kilobyte.')
        print('Digite 3 para converter para gigabyte.')
        print('Digite 4 para converter para terabyte.')
        unid = int(input('Digite a opcao: '))
        if unid == 1:
            mb = float(input('Digite a medida em megabyte; '))
            byte = mb * 1000000
            print('O valor em bytes eh: ', byte)
        elif unid == 2:
            mb = float(input('Digite a medida em megabyte; '))
            kb = mb * 1000
            print('O valor em kilobytes eh: ', kb)
        elif unid == 3:
            mb = float(input('Digite a medida em megabyte; '))
            gb = mb / 1000
            print('O valor em gigabytes eh: ', gb)
        elif unid == 4:
            mb = float(input('Digite a medida em megabyte; '))
            tb = mb * 1000000
            print('O valor em terabytes eh: ', tb)
        else:
            print('Valor invalido')

    elif opc == 4:
        print('Digite 1 para converter para byte.')
        print('Digite 2 para converter para kilobyte.')
        print('Digite 3 para converter para megabyte.')
        print('Digite 4 para converter para terabyte.')
        unid = int(input('Digite a opcao: '))
        if unid == 1:
            gb = float(input('Digite a medida em gigabyte; '))
            byte = gb * 1000000000
            print('O valor em bytes eh: ', byte)
        elif unid == 2:
            gb = float(input('Digite a medida em gigabyte; '))
            kb = gb * 1000000
            print('O valor em kilobytes eh: ', kb)
        elif unid == 3:
            gb = float(input('Digite a medida em gigabyte; '))
            mb = gb * 1000
            print('O valor em megabytes eh: ', mb)
        elif unid == 4:
            gb = float(input('Digite a medida em gigabyte; '))
            tb = gb / 1000
            print('O valor em terabytes eh: ', tb)
        else:
            print('Valor invalido')

    elif opc == 5:
        print('Digite 1 para converter para byte.')
        print('Digite 2 para converter para kilobyte.')
        print('Digite 3 para converter para megabyte.')
        print('Digite 4 para converter para gigabyte.')
        unid = int(input('Digite a opcao: '))
        if unid == 1:
            tb = float(input('Digite a medida em terabyte; '))
            byte = tb * 1000000000000
            print('O valor em bytes eh: ', byte)
        elif unid == 2:
            tb = float(input('Digite a medida em terabyte; '))
            kb = tb * 1000000000
            print('O valor em kilobytes eh: ', kb)
        elif unid == 3:
            tb = float(input('Digite a medida em terabyte; '))
            mb = tb * 1000000
            print('O valor em bytes eh: ', mb)
        elif unid == 4:
            tb = float(input('Digite a medida em terabyte; '))
            gb = tb * 1000
            print('O valor em bytes eh: ', gb)
        else:
            print('Valor invalido')


def bases():
    num_original = str(input('Digite o numero que sera convertido: '))
    base_original = int(input('Digite a base original: '))
    base_final = int(input('Digite a base para qual sera convertido: '))
    caracteres = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                  'K', 'L',
                  'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    decimal = 0
    aux = list(num_original)
    aux.reverse()
    for x, i in enumerate(aux):
        decimal += caracteres.index(i) * base_original ** x
    if base_final == 10:
        print('O numero em decimal e: ', decimal)
    else:
        aux1 = []
        numero_final = ''
        while True:
            temp = decimal % base_final
            aux1.append(temp)
            if int(decimal / base_final) == 0:
                break
            decimal = int(decimal / base_final)
        aux1.reverse()
        for i in aux1:
            numero_final += caracteres[i]
        print('O numero final convertido e: ', numero_final)


def somabinarios():
    a = str(input('Digite o primeiro numero: '))
    b = str(input('Digite o segundo numero: '))
    for i in a:
        assert i in {'0', '1'}, 'caractere invalido: ' + i
    for i in b:
        assert i in {'0', '1'}, 'caractere invalido: ' + i
    soma = int(a, 2) + int(b, 2)
    print(bin(soma)[2:])


def portas():
    print('Selecione a porta que deseja usar\n'
          '1) NOT\n'
          '2) AND\n'
          '3) OR\n'
          '4) XOR\n'
          '5) NAND\n'
          '6) NOR\n')
    opc = int(input('Digite a opcao: '))
    entrada = str(input('Digite a entrada: '))
    saida = -1
    if opc == 1:
        if entrada == '1':
            saida = 0
            print('A saida e: ', saida)
        elif entrada == '0':
            saida = 1
            print('A saida e: ', saida)
        else:
            print('entrada invalida')
    elif opc == 2:
        for i in range(len(entrada)):
            if entrada[i] == '0':
                saida = 0
            else:
                saida = 1
        print('A saida e: ', saida)
    elif opc == 3:
        for i in range(len(entrada)):
            if entrada[i] == '1':
                saida = 1
        print('A saida e: ', saida)
    elif opc == 4:
        for i in range(len(entrada)):
            if entrada[0] != entrada[i]:
                saida = 1
        print('A saida e: ', saida)
    elif opc == 5:
        for i in range(len(entrada)):
            if entrada[i] == '0':
                saida = 0
            else:
                saida = 1
        print('A saida e: ', saida)
    elif opc == 6:
        for i in range(len(entrada)):
            if entrada[i] == '1':
                saida = 1
        print('A saida e: ', saida)
    else:
        print('opcao invalida')


def validar():
    expressao = str(input('Digite a expressao a ser validada: '))
    pilha1 = Stack()
    operadores = ['AND', 'OR', 'XOR', 'NAND', 'NOR']

    # verificar se os parenteses est??o na ordem e quantidade correta
    for simbolo in expressao:
        if simbolo == '(':
            pilha1.push('(')
        elif simbolo == ')':
            if len(pilha1) > 0:
                pilha1.pop()
            else:
                pilha1.push(')')
                break

    # verificar sintaxe, nao conseguimos fazer funcionar
    expressao.upper()
    dividir = expressao.split('(')
    dividir = expressao.split(')')
    cont = 0
    validador = 0
    for i in dividir:
        if cont != 0:
            op_anterior = dividir[cont - 1]

            if i in operadores:
                if op_anterior in operadores or op_anterior == 'NOT':
                    print('Expressao invalida!')
                    break
                elif i in operadores and op_anterior in operadores:
                    print('Expressao invalida')
                    break
                elif i == 'NOT' and op_anterior not in operadores:
                    print('Expressao invalida')
                    break
            cont = cont + 1
    validador = 0

    if len(pilha1) == 0 and validador == 0:
        print('Expressao valida')
    else:
        print('Expressao invalida')


# main
menu = int(input('Digite 1 para converter medidas de informacao\n'
                 'Digite 2 para converter bases numericas\n'
                 'Digite 3 para somar numeros binarios\n'
                 'Digite 4 para simular portas logicas\n'
                 'Digite 5 para validar expressao\n'
                 'Digite 6 para sair: '))
while menu != 6:
    if menu == 1:
        medidas_de_inf()
        print('-----')
        menu = int(input('Digite 1 para converter medidas de informacao\n'
                         'Digite 2 para converter bases numericas\n'
                         'Digite 3 para somar numeros binarios\n'
                         'Digite 4 para simular portas logicas\n'
                         'Digite 5 para validar expressao\n'
                         'Digite 6 para sair: '))
    elif menu == 2:
        bases()
        print('-----')
        menu = int(input('Digite 1 para converter medidas de informacao\n'
                         'Digite 2 para converter bases numericas\n'
                         'Digite 3 para somar numeros binarios\n'
                         'Digite 4 para simular portas logicas\n'
                         'Digite 5 para validar expressao\n'
                         'Digite 6 para sair: '))
    elif menu == 3:
        somabinarios()
        print('-----')
        menu = int(input('Digite 1 para converter medidas de informacao\n'
                         'Digite 2 para converter bases numericas\n'
                         'Digite 3 para somar numeros binarios\n'
                         'Digite 4 para simular portas logicas\n'
                         'Digite 5 para validar expressao\n'
                         'Digite 6 para sair: '))
    elif menu == 4:
        portas()
        print('-----')
        menu = int(input('Digite 1 para converter medidas de informacao\n'
                         'Digite 2 para converter bases numericas\n'
                         'Digite 3 para somar numeros binarios\n'
                         'Digite 4 para simular portas logicas\n'
                         'Digite 5 para validar expressao\n'
                         'Digite 6 para sair: '))
    elif menu == 5:
        validar()
        print('-----')
        menu = int(input('Digite 1 para converter medidas de informacao\n'
                         'Digite 2 para converter bases numericas\n'
                         'Digite 3 para somar numeros binarios\n'
                         'Digite 4 para simular portas logicas\n'
                         'Digite 5 para validar expressao\n'
                         'Digite 6 para sair: '))
    elif menu == 6:
        break
    else:
        print('Valor invalido')
        print('-----')
        menu = int(input('Digite 1 para converter medidas de informacao\n'
                         'Digite 2 para converter bases numericas\n'
                         'Digite 3 para somar numeros binarios\n'
                         'Digite 4 para simular portas logicas\n'
                         'Digite 5 para validar expressao\n'
                         'Digite 6 para sair: '))
