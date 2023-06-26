import memory
from array import array

firmware = array('Q', [0]) * 512 # Cria a memória do firmware - trocamos o L pelo Q para adaptar a nova arquitetura de 64 bits para adicionar o novo barramento A

# main: PC <- PC + 1; MBR <- read_byte(PC); goto MBR
firmware[0] =   0b000000000_100_00110101_001000_001_000001

# HALT
firmware[255] = 0b000000000_000_00000000_000000_000_000000

# Operações com X

# X = X + memory[address] (add x, )

## 2: PC <- PC + 1; MBR <- read_byte(PC) - fetch; goto 3
firmware[2] =   0b000000011_000_00110101_001000_001_000001

## 3: MAR <- MBR; read_word(MAR); goto 4
firmware[3] =   0b000000100_000_00010100_100000_010_000010

## 4: X <- MDR + X; goto 0
firmware[4] =   0b000000000_000_00111100_000100_000_000011


# X = X - memory[address] (sub x, )

## 5: PC <- PC + 1; fetch; goto 6
firmware[5] =   0b000000110_000_00110101_001000_001_000001

## 6: MAR <- MBR; MDR <- read_word(MAR); goto 7
firmware[6] =   0b000000111_000_00010100_100000_010_000010

## 7: X <- X - MDR; goto 0
firmware[7] =   0b000000000_000_00111111_000100_000_000011

# memory[address] = X (mov x, )

## 8: PC <- PC + 1; fetch; goto 9
firmware[8] =    0b00001001_000_00110101_001000_001_000001

## 9: MAR <- MBR; goto 10
firmware[9] =    0b00001010_000_00010100_100000_000_000010

## 10: MDR <- X; write; goto 0
firmware[10] =   0b00000000_000_00010100_010000_100_000011

# goto address (goto)

## 11: PC <- PC + 1; PC + 1; MBR <- read_byte(PC) - fetch; goto 12
firmware[11] =   0b00001100_000_00110101_001000_001_000001

## 12: PC <- MBR; fetch; goto MBR
firmware[12] =   0b00000000_100_00010100_001000_001_000010

# if X == 0 goto address (jz x, )

## 13: X <- X; if alu = 0 goto 270 else goto 14
firmware[13] =   0b00001110_001_00010100_000100_000_000011

## 14: PC <- PC + 1; goto 0
firmware[14] =   0b00000000_000_00110101_001000_000_000001

## 270: goto 11
firmware[270]=   0b00001011_000_00000000_000000_000_000000

# 15: X <- X << 1 (X * 2); goto 0
firmware[15] =   0b00000000_000_00101010_000100_000_000011

# 16: X <- X >> 1 (X / 2); goto 0
firmware[16] =   0b00000000_000_10010100_000100_000_000011

# 17: X <- X - 1
firmware[17] =   0b00000000_000_00110110_000100_000_000011

# X = X * memory[address] (mult x, )

## 18: PC <- PC + 1; MBR <- read_byte(PC) - fetch; goto 19
firmware[18] =   0b00010011_000_00110101_001000_001_000001

## 19: MAR <- MBR; MDR <- read_word(MAR); goto 20
firmware[19] =   0b00010100_000_00010100_100000_010_000010

## 20: X <- X * MDR; goto 0
firmware[20] =   0b00000000_000_00100000_000100_000_000011

# X = X // memory[address] (div x, )

## 21: PC <- PC + 1; MBR <- read_byte(PC) - fetch; goto 22
firmware[21] =   0b00010110_000_00110101_001000_001_000001

## 22: MAR <- MBR; read_word(MAR); goto 23
firmware[22] =   0b00010111_000_00010100_100000_010_000010

## 23: X <- X // MDR; goto 0 
firmware[23] =   0b00000000_000_00100001_000100_000_000011

# X = X % memory[address]

## 24: PC <- PC + 1; MBR <- read_byte(PC) - fetch; goto 25
firmware[24] =   0b00011001_000_00100010_001000_001_000001

## 25: MAR <- MBR; MDR <- read_word(MAR); goto 26
firmware[25] =   0b00011010_000_00010100_100000_010_000010

## 26: X <- X % MDR; goto 0
firmware[26] =   0b00000000_000_00100010_000100_000_000011

# Operações com Y

# Y <- Y + memory[address] (add y, )

## 27: PC <- PC + 1; MBR <- read_word(PC) - fetch; goto 28
firmware[27] =   0b00011100_000_00110101_001000_001_000001

## 28: MAR <- MBR; MDR <- read_word(MAR); goto 29
firmware[28] =   0b00011101_000_00010100_100000_010_000010

## 29: Y <- Y + MBR; goto 0
firmware[29] =   0b00000000_000_00111100_000010_000_000100

# Y <- Y - memory[address] (sub y, )

## 30: PC <- PC + 1; MBR <- read_word(PC) - fetch; goto 31
firmware[30] =   0b00011111_000_00110101_001000_001_000001

## 31: MAR <- MBR; MDR <- read_word(MAR) - read; goto 32
firmware[31] =   0b00100000_000_00010100_100000_010_000010

## 32: Y <- Y - MDR; goto 0
firmware[32] =   0b00000000_000_00111111_000010_000_000100

# memory[address] = Y (mov y, ) 

## 33: PC <- PC + 1; MBR <- read_word(PC) - fetch; goto 34
firmware[33] =   0b00100010_000_00110101_001000_001_000001

##34: MAR <- MBR; MDR <- read_word(MAR) - read; goto 35
firmware[34] =   0b00100011_000_00010100_100000_010_000010

##35: memory[address] = Y; goto 0
firmware[35] =   0b00000000_000_00010100_010000_100_000100

# if Y == 0 goto address (jz y, )

## 36: Y <- Y; if alu = 0 goto 292 else goto 37
firmware[36] =   0b00100101_001_00010100_000010_000_000100

## 292: goto 11
firmware[293] =  0b00001011_000_00000000_000000_000_000000

## 37: PC <- PC + 1; goto 0
firmware[37] =   0b00000000_000_00110101_001000_000_000001

# Y <- Y * memory[address] (mult y, )

## 38: PC <- PC + 1; MBR <- read_word(PC) - fetch; goto 39
firmware[38] =   0b00100111_000_00110101_001000_001_000001

## 39: MAR <- MBR; MDR <- read_word(MAR) - read; goto 40
firmware[39] =   0b00101000_000_00010100_100000_010_000010

## 40: Y <- Y * MDR; goto 0
firmware[40] =   0b00000000_000_00100000_000010_000_000100

# Y <- Y // memory[address] (div y, )

## 41: PC <- PC + 1; MBR <- read_byte(PC) - fetch; goto 42
firmware[41] =   0b00101010_000_00110101_001000_001_000001

## 42: MAR <- MBR; MDR <- read_word(MAR) - read; goto 43
firmware[42] =   0b00101011_000_00010100_100000_010_000010

## 43: Y <- Y // MDR; goto 0 
firmware[43] =   0b00000000_000_00100001_000010_000_000100


 
MPC = 0
MIR = 0

MAR = 0 # Armazena endereço de memória do Fetch/Write/Read -> recebe do MBR (responsável por receber as instruções de PC)
MDR = 0 # Sempre responsável por escrever ou receber dados da memória (no/do endereço armazenado em MAR)
PC  = 0
MBR = 0 # Sempre responsável receber o Read no endereço do PC (Pode receber um endereço, um comando, memória, etc -> depende da instrução)
X = 0
Y = 0
H = 0   

N = 0
Z = 1

BUS_A = 0
BUS_B = 0
BUS_C = 0

def read_regs(reg_num):
    global MDR, PC, MBR, X, Y, H, BUS_A, BUS_B

    reg_num_a = reg_num & 0b111_000 # Pega apenas o barramento A - seleciona o BUS_A
    reg_num_b = reg_num & 0b000_111 # Pega apenas o barramento B - seleciona o BUS_B

    if reg_num_a == 0:
        BUS_A = MDR
    elif reg_num_a == 1: #PC
        BUS_A = 0 # Na micro arquitetura o BUS_A não recebe o PC
    elif reg_num_a == 2:
        BUS_A = MBR
    elif reg_num_a == 3:
        BUS_A = X
    elif reg_num_a == 4:
        BUS_A = Y
    elif reg_num_a == 5:
        BUS_A = H
    else:
        BUS_A = 0
    
    if reg_num_b == 0:
        BUS_B = MDR
    elif reg_num_b == 1:
        BUS_B = PC
    elif reg_num_b == 2:
        BUS_B = MBR
    elif reg_num_b == 3:
        BUS_B = X
    elif reg_num_b == 4:
        BUS_B = Y
    else:
        BUS_B = 0
            
def write_regs(reg_bits):

    global MAR, BUS_C, MDR, PC, X, Y, H

    if reg_bits & 0b100000:
        MAR = BUS_C
        
    if reg_bits & 0b010000:
        MDR = BUS_C
        
    if reg_bits & 0b001000:
        PC = BUS_C
        
    if reg_bits & 0b000100:
        X = BUS_C
        
    if reg_bits & 0b000010:
        Y = BUS_C
        
    if reg_bits & 0b000001:
        H = BUS_C
        
            
def alu(control_bits):

    global BUS_A, BUS_B, BUS_C, N, Z
    
    a = BUS_A 
    b = BUS_B
    o = 0
    
    shift_bits = control_bits & 0b11000000
    shift_bits = shift_bits >> 6
    
    control_bits = control_bits & 0b00111111
    
    if control_bits == 0b011000:   #24  
        o = a
    elif control_bits == 0b010100: #20
        o = b
    elif control_bits == 0b011010: #26
        o = ~a
    elif control_bits == 0b101100: #44
        o = ~b
    elif control_bits == 0b111100: #60
        o = a + b    
    elif control_bits == 0b111101: #61
        o = a + b + 1
    elif control_bits == 0b111001: #57
        o = a + 1
    elif control_bits == 0b110101: #53
        o = b + 1
    elif control_bits == 0b111111: #63
        o = b - a
    elif control_bits == 0b110110: #54
        o = b - 1
    elif control_bits == 0b111011: #59
        o = -a
    elif control_bits == 0b001100: #12
        o = a & b
    elif control_bits == 0b011100: #28
        o = a | b
    elif control_bits == 0b010000: #16
        o = 0
    elif control_bits == 0b110001: #49
        o = 1
    elif control_bits == 0b110010: #50
        o = -1 
    elif control_bits == 0b100000: #32
        o = a * b
    elif control_bits == 0b100001: #33
        o = a // b
    elif control_bits == 0b100010: #34
        o = a % b

    

    
    
        
    if o == 0:
        N = 0
        Z = 1
    else:
        N = 1
        Z = 0
    
    #Mutiplica por 2
    if shift_bits == 0b01:
        o = o << 1
    #Divide por 2
    elif shift_bits == 0b10:
        o = o >> 1
    #Mutiplica por 8
    elif shift_bits == 0b11:
        o = o << 8
        
    BUS_C = o
 

def next_instruction(next, jam):

    global MPC, MBR, N, Z
    
    if jam == 0b000:
        MPC = next
        return
        
    if jam & 0b001:                 # JAMZ
        next = next | (Z << 8)
        
    if jam & 0b010:                 # JAMN
        next = next | (N << 8)

    if jam & 0b100:                 # JMPC
        next = next | MBR
        
    MPC = next


def memory_io(mem_bits):

    global PC, MBR, MDR, MAR
    
    if mem_bits & 0b001:                # FETCH
       MBR = memory.read_byte(PC)
       
    if mem_bits & 0b010:                # READ
       MDR = memory.read_word(MAR)
       
    if mem_bits & 0b100:                # WRITE
       memory.write_word(MAR, MDR)
       
def step():
   
    global MIR, MPC
    
    MIR = firmware[MPC]
    
    if MIR == 0:
        return False    
    
    read_regs        ( MIR & 0b00000000000000000000000000000111111)
    alu              ((MIR & 0b00000000000011111111000000000000000) >> 15)
    write_regs       ((MIR & 0b00000000000000000000111111000000000) >> 9)
    memory_io        ((MIR & 0b00000000000000000000000000111000000) >> 6)
    next_instruction ((MIR & 0b11111111100000000000000000000000000) >> 26,
                      (MIR & 0b00000000011100000000000000000000000) >> 23)
                     
    return True