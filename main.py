fita1 = []
fita2 = []
cabecote1 = 0
cabecote2 = 1  # Comeca em 1 porque eu preciso do primeiro espaço em branco
resultado = "REJEITA"


def inicializaFita():
    global fita1, fita2
    fita1 = list(input())
    fita1.append('\0')
    fita2.append('\0')
    fita2.append('\0')


def q0():
    global fita1, fita2, cabecote1, cabecote2
    # Garante que nao ocorra o erro de acessar um indice fora da lista
    while fita1[cabecote1] == '1' and fita2[cabecote2] == '\0':
        fita2[cabecote2] = '1'
        cabecote1 += 1
        cabecote2 += 1
        fita2.append('\0')
    if fita1[cabecote1] == '#' and fita2[cabecote2] == '\0':
        cabecote2 -= 1
        q1()
    return


def q1():
    global fita1, fita2, cabecote1, cabecote2
    while fita1[cabecote1] == '#' and fita2[cabecote2] == '1':
        cabecote2 -= 1
    if fita1[cabecote1] == '#' and fita2[cabecote2] == '\0':
        cabecote1 += 1
        cabecote2 += 1
        q2()
    return


def q2():
    global fita1, fita2, cabecote1, cabecote2
    while fita1[cabecote1] == '1' and fita2[cabecote2] == '1':
        cabecote1 += 1
        cabecote2 += 1
    if fita1[cabecote1] == '\0' and fita2[cabecote2] == '1':
        fita2[cabecote2] = '#'
        cabecote2 += 1
        q3()
    elif fita1[cabecote1] == '1' and fita2[cabecote2] == '\0':
        cabecote1 -= 1
        cabecote2 -= 1
        q6()
    elif fita1[cabecote1] == '\0' and fita2[cabecote2] == '\0':
        fita2[cabecote2] = '#'
        q6()
    return


def q3():
    global fita1, fita2, cabecote1, cabecote2
    while fita1[cabecote1] == '\0' and fita2[cabecote2] == '1':
        cabecote2 += 1
    if fita1[cabecote1] == '\0' and fita2[cabecote2] == '\0':
        fita2[cabecote2] = '1'
        fita2.append('\0')
        cabecote1 -= 1
        q4()
    return


def q4():
    global fita1, fita2, cabecote1, cabecote2
    while fita1[cabecote1] == '1' and fita2[cabecote2] == '1':
        cabecote1 -= 1
    if fita1[cabecote1] == '#' and fita2[cabecote2] == '1':
        cabecote1 += 1
        q5()
    return


def q5():
    global fita1, fita2, cabecote1, cabecote2
    while fita1[cabecote1] == '1' and fita2[cabecote2] == '1':
        cabecote2 -= 1
    if fita1[cabecote1] == '1' and fita2[cabecote2] == '#':
        cabecote2 += 1
        q2()
    return



def q6():
    global fita1, fita2, cabecote1, cabecote2
    while ((fita1[cabecote1] == '1' and fita2[cabecote2] == '1') or
           (fita1[cabecote1] == '1' and fita2[cabecote2] == '#')):
        cabecote1 -= 1
    if ((fita1[cabecote1] == '#' and fita2[cabecote2] == '1') or
            (fita1[cabecote1] == '#' and fita2[cabecote2] == '#')):
        cabecote1 += 1
        q7()
    elif fita1[cabecote1] == "#" and fita2[cabecote2] == '\0':
        cabecote1 += 1
        q8()
    return


def q7():
    global fita1, fita2, cabecote1, cabecote2
    while fita1[cabecote1] == '1' and fita2[cabecote2] == '1':
        cabecote2 -= 1
    if (fita1[cabecote1] == '1' and (fita2[cabecote2] == '\0' or
                                     fita2[cabecote2] == '#')):
        cabecote2 += 1
        q8()
    return


def q8():
    global fita1, fita2, cabecote1, cabecote2
    while (fita1[cabecote1] == '1' and (fita2[cabecote2] == '1' or
                                        fita2[cabecote2] == '\0')):
        cabecote1 += 1
    if (fita1[cabecote1] == '\0' and (fita2[cabecote2] == '1' or
                                      fita2[cabecote2] == '\0')):
        fita1[cabecote1] = '='
        fita1.append('\0')
        cabecote1 += 1
        q9()
    return


def q9():
    global fita1, fita2, cabecote1, cabecote2
    while fita1[cabecote1] == '\0' and fita2[cabecote2] == '1':
        fita1[cabecote1] = '1'
        cabecote1 += 1
        fita1.append('\0')
        cabecote2 += 1
    if fita1[cabecote1] == '\0' and fita2[cabecote2] == '\0':
        cabecote1 += 1
        fita1.pop()
        q10aq16()
    return


def q10aq16():
    global resultado
    resultado = "ACEITA"
    return


def imprimirResultado():
    global fita1
    for char in fita1:
        print(char, end="")
    print(" ", end="")
    print(resultado)


def main():
    inicializaFita()
    q0()
    imprimirResultado()


main()
