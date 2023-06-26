   goto main 
   wb 0

r ww 0
a ww 21
b ww 32
c ww 10

main add x, a           
     jz x, nova         
     add x, b           
nova sub x, c           
     mov x, r
     halt

