
def instruction_fetch(memory, pc):
    inst = 0
    for i in range(pc, pc + 4):
        inst = inst * 256 + memory[i]
    return (inst, pc + 4)
    