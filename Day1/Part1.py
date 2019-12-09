def main():
    totalFuel = 0
    inputFile = open("puzzleinput.txt", "r")

    for line in inputFile:
        mass = int(line)
        fuel = int(mass/3)-2
        totalFuel += fuel
    
    inputFile.close()
    print("Total fuel needed: %d\r\n" % totalFuel)

if __name__== "__main__":
  main()