import sys
import instructionfetch

base = 0x80000000

def parse_mc(file):
    memory = bytearray()
    start = 0
    for line in open(file, "r").readlines():
        if any(x.isdigit() for x in line):
            if "<" in line:
                if "_start" in line:
                    start = int(line.split()[0], 16)
            else:
                address, value = line.split(":")
                address = int(address, 16) - base
                if address >= len(memory):
                    for i in range(4 * (address - len(memory) + 1)):
                        memory.append(0)
                value = value.strip()
                for i in range(4):
                    memory[address + i] = int(value[2*i:2*(i + 1)], 16)
    return (memory, start - base)
                           

if __name__ == "__main__":
    registers = [0] * 32
    memory, pc = parse_mc(sys.argv[1])
    print(memory[:4], pc)
    inst, pc = instructionfetch.instruction_fetch(memory, pc)
    print(inst, pc)