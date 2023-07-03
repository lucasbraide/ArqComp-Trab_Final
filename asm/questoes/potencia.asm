goto main           # Questao 1 - funcao potencia
 wb 0

r ww 0              # Retorno da funcao potencia
m ww 6              # Argumento da potencia: base
n ww 2              # Argumento da potencia: expoente
a ww 0              # Argumento da funcao multiplicacao
b ww 0              # Argumento da funcao multiplicacao
z ww 0              # Retorno da funcao multiplicacao
u ww 1              # +1 or -1

main add x, m       #
     jz x, caso1
     sub x, u
     jz x, caso2

     add y, n
     jz y, caso3
     sub y, u
     jz y, caso4

     mov y, n
     sub y, n

     add x, u
     mov x, a
     sub x, a

     goto potencia

caso1 halt
caso2 add x, m
     mov x, r
     halt
caso3 add y, u
     mov y, r
     halt
caso4 add y, m
     mov y, r
     halt

potencia add x, m
     add y, n
     mov x, r
     goto loop

loop jz y, final
     mult x, r
     sub y, u
     goto loop

final mov x, r
     halt
