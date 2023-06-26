import ufc2x as cpu
import sys
import memory as mem
import clock as clk 
import disk

disk.read(str(sys.argv[1]))

clk.start([cpu])

print("Depois: ", mem.read_word(1)) # Padronização do retorno da função para o end 1