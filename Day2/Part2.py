import copy

def intcodeComputer(mem):
    i = 0
    while(mem[i] != 99):
        if(mem[i] == 1):
            mem[mem[i+3]] = mem[mem[i+1]] + mem[mem[i+2]]
            i += 4
        elif(mem[i] == 2):
            mem[mem[i+3]] = mem[mem[i+1]] * mem[mem[i+2]]
            i += 4
        elif(mem[i] == 99):
            return mem[0]
        else:
            print("Invalid opcode. I: %d, output: %d\r\n" % (i, mem[i]))
            print(type(mem[i]))
            return -1
    
    return mem[0]

def main():
    inputFile = open("puzzleinput.txt", "r")
    program = list(map(int, inputFile.readline().split(",")))
    inputFile.close()
    output = 0
    noun = 0
    verb = 0
    
    for noun in range(100):
        for verb in range(100):
            memory = copy.copy(program)
            memory[1] = int(noun)
            memory[2] = int(verb)
            output = intcodeComputer(memory)

            if(output == 19690720):
                print("SOLUTION FOUND! Noun: %d, verb: %d. Produced output is %d.\r\n" % (noun, verb, output))
                solution = 100 * noun + verb
                print("100 * noun * verb = %d\r\n" % solution )
                break
            elif(output == -1):
                print("Invalid opcode. Noun: %d, verb: %d.\r\n" % (noun, verb))
            else:
                print("Noun: %d, verb: %d, output: %d.\r\n" % (noun, verb, output))
                
                
        if(output == 19690720):
                break
    
if __name__== "__main__":
  main()