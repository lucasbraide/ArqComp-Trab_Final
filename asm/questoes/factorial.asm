    goto main # Questão 4 - Fatorial de um número
     wb 0        
    
r    ww 0           # Retorno da função - resultado do fatorial
c    ww 5          # Paramtro que terá seu fatorial calculado
u    ww 1           # Auxiliar que servirá para decrementar o número e multiplicar

main add x, c       # Bota o valor de c em x (x = x + c)
    jz x, finalmain # Se N igual a 0, finaliza o programa e retorna r = 1       
    sub x, u
    jz x, finalmain # Verificao se é 1
    add x, u        # Volta o x no estado anterior
    mov x, r        # Bota o valor de x em r (memory[r] = x)
    add y, r        # Bota o valor de r em y (y = y + r)
    goto loop       # Entra no loop de fatorial
loop sub x, u       # Subtrai 1 de x (x = x - u)
    jz x, final     # Se x == 0 -> vai pro final e termina o programa
    mov x, r        # Bota o valor de x (decrementado) em r (memory[r] = x)
    mult y, r       # Multiplica y com r (y = y * r)
    goto loop       # Volta para o loop
final mov y, r      # Ao final -> move o valor de y para o r (memory[r] = y)
    halt            # Comando de parada

finalmain add y, r  # Usa o Y para verificar se o valor inserido é 0
          jz y, caso1 # Se for 0 vai para Caso 1
          mov y, r  # Y para o retorno
          halt      # Fim
caso1 add y, u
      mov y, r      # Y para o retorno
      halt          # Fim