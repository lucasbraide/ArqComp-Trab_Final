 goto main
 wb 0
 
r ww 0 
b ww 2
c ww 3
u ww 1

main add y, c      # if c=0 goto final
     jz y, final   
     
     sub y, u      # c = c - 1
     mov y, c
     sub y, c
     
     add y, r      # r = r + b
     add y, b
     mov y, r
     sub y, r
     
     goto main
     
final halt
     
     
     
