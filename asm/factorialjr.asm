         goto main 
     wb 0        
    
r    ww 0      
c    ww 12
u    ww 1     

main add x, c
    jz x, finalmain # Se N igual a 0, finaliza o programa e retorna r = 1       
    sub x, u
    jz x, finalmain # verificao se é 1
    add x, u    
    mov x, r
    add y, r
    goto loop
loop sub x, u
    jz x, final
    mov x, r
    mult y, r
    goto loop
final mov y, r 
    halt 

finalmain add y, r
          jz y, caso1
          mov y, r 
          halt  
caso1 add y, u
      mov y, r
      halt