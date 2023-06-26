         goto main 
     wb 0        
    
r    ww 0      
c    ww 12
u    ww 1     

main add x, c
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
