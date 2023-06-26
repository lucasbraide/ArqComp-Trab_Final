goto main
wb 0

r ww 0
a ww 32
b ww 32

main add y, b
     jz y, teste
     mov y, a
teste mov y, r
     halt
     