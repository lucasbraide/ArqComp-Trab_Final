goto main
wb 0

r ww 0
a ww 1
b ww 0

main add x, b
     jz x, teste
     mov x, a
teste mov x, r
     halt
     