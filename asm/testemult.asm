     goto main 
     wb 0        
    
a    ww 0      
b    ww 64
c    ww 64     
d    ww 0

main add y, b 
     mult y, c
     mov y, a 
     mov y, d
     halt
