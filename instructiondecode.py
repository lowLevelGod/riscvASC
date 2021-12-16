import instructionexecute


def instruction_decode(inst, memory, registers):
    opcode = inst and 0x1111111
    
    if opcode == 0x0110111:  #lui
        rd = inst and (0x11111 << 7)
        imm = inst and ((not 0x0) >> 12)
        
    