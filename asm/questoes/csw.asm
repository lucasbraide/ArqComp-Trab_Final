    goto main   # Questão 3 - CSW(a,b,c)
    wb 0

r ww 1          # Resultado - Retorno da função
a ww 1000        # Argumento da função CSW
b ww 250        # Operando da funcao CSW
c ww 99999        # Argumento da funcao CSW


main add x, a   # Se a != c; a <- c; return 1 // x recebe o valor de a (x = x + a)
     sub x, c   # x = x - c
     jz x, else # se x = 0 (a == c) vai para a linha else
     add y, c   # y = y + c
     mov y, a   # passa o y (que possui o valor de c) para a - memory[a] = y
     halt       # finaliza


else mov x, r   # a == c; c <- b; return 0 // x = 0 -> passa o 0 para o r (retorna 0)
     add x, b   # x = x + b
     mov x, c   # passa o x para o c 
     halt       # finaliza