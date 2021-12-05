naprej = 0
globina = 0
aim = 0

for x in open("input.txt"):
    ukaz = x.split()
    if(ukaz[0] == "forward"):
        naprej += int(ukaz[1])
        globina += aim * int(ukaz[1])
    elif(ukaz[0] == "down"):
        aim += int(ukaz[1])
    else:
        aim -= int(ukaz[1])

print(naprej * globina)