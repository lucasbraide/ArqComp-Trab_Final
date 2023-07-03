goto main           # Questao 1 - funcao potencia
 wb 0

r ww 0              # Retorno da funcao potencia
m ww 5              # Argumento da potencia: base
n ww 3              # Argumento da potencia: expoente
a ww 0              # Argumento da funcao multiplicacao
b ww 0              # Argumento da funcao multiplicacao
z ww 0              # Retorno da funcao multiplicacao
u ww 1              # +1 or -1

main add x, m       # Bota x em m
     jz x, caso1    # Se for 0, vai para caso 1
     sub x, u       # Subtrai 1 de x
     jz x, caso2    # Se for 0, vai para caso 2

     add y, n       # Adiciona n em y: expoente para o Y
     jz y, caso3    # Se y (n) for 0, vai para caso 3
     sub y, u       # Subtrai 1 de Y
     jz y, caso4    # Se for 0 depois (n era 1), vai para caso 4

     mov y, n       # Bota n (expoente) para o Y novamente
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
