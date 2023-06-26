goto tubias
wb 0

r ww 0 
b ww 0
t ww 0
c ww 5
u ww 1

tubias add x, c
    mov x, r
    sub x, u
    mov x, c
    sub x, c

    goto princ

princ add x, c
    jz x, final

    mov x, t
    sub x, u
    mov x, c
    sub x, c

    add x, r
    mov x, b
    sub x, b
    mov x, r

    goto mult

mult add x, t
    jz x, princ

    sub x, u
    mov x, t
    sub x, t

    add x, r
    add x, b
    mov x, r 
    sub x, r

    goto mult

final halt