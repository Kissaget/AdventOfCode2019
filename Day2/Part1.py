def main():
    inputFile = open("puzzleinput.txt", "r")
    program = list(map(int, inputFile.readline().split(",")))
    program[1] = 12 #initialize
    program[2] = 2  #initialize
    
    i = 0
    opcode = program[0]
    
    while(opcode != 99):
        if(opcode == 1):
            inputpos1 = program[i+1]
            inputpos2 = program[i+2]
            outputpos = program[i+3]
            program[outputpos] = program[inputpos1] + program[inputpos2]
        elif(opcode == 2):
            inputpos1 = program[i+1]
            inputpos2 = program[i+2]
            outputpos = program[i+3]
            program[outputpos] = program[inputpos1] * program[inputpos2]
        else:
            print("Invalid opcode, terminating.")
            opcode = 99
            break
        
        i += 4
        opcode = program[i]

    print("SOLUTION: Value at position 0 is %d\r\n" % program[0])
        
if __name__== "__main__":
  main()