     goto main 
     wb 0        
    
a    ww 0      
b    ww 64
c    ww 64     
d    ww 0

main mult x, b 
     mult x, c 
     mov x, a 
     mov x, d
     halt 