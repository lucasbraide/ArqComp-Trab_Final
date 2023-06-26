import ufc2x as cpu
import sys
import memory as mem
import clock as clk 
import disk

disk.read(str("asm/testemult.bin"))


clk.start([cpu])

print("Depois: ", mem.read_word(1))