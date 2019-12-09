def main():
    totalFuel = 0
    inputFile = open("puzzleinput.txt", "r")

    for line in inputFile:
        mass = int(line)
        moduleFuel = int(mass/3)-2
        fuel = int(moduleFuel/3)-2
        while(fuel > 0):
            moduleFuel += fuel
            fuel = int(fuel/3)-2
            
        totalFuel += moduleFuel
    
    inputFile.close()
    print("Total fuel needed: %d\r\n" % totalFuel)

if __name__== "__main__":
  main()