import random as r

machines = [(.5, .5),
        (.7, .9),
        (.2, .3),
        (.2, 3),
        (1.5, 1),
        (3, 2),
        (2, .1),
        (.1, 15),
        (.4, .3),
        (.9, 1),
        (1.2, 1)]


def get_num_slot_machines():
    return len(machines)

def use_machine(machine, bet):
    machine = machines[machine]
    ret = int(bet * r.normalvariate(machine[0], machine[1]))
    if ret > 0:
        return ret
    else:
        return 0



def display(machines):
  for m in machines:
    print(str(m[0]) + " " + str(m[1]) + " " + str(m[2]))
  print('\n')




endPulls = 50

num_machines = get_num_slot_machines()

myMachines = []

for i in range(num_machines):
  # [machine #, pulls, average]
  myMachines.append([i, 0, 0])
  
money = 1000
totalPulls = 0
maxIndex = 0
maxAverage = 0

# Loops through once to get initial averages for machines
for i in range(num_machines):
  totalPulls += 1
  myMachines[i][1] += 1
  val = use_machine(i, 10)
  money += val - 10
  myMachines[i][2] = val
  if val > maxAverage:
    maxIndex = i
    maxAverage = val

print("First run")
display(myMachines)

# Sort machines in order of initial return
myMachines = sorted(myMachines, key=lambda m: m[2], reverse=True)

print("Sorted after first")
display(myMachines)






while (money > 0) and (totalPulls < endPulls):
  
  # Use best machine until next one is better
  while (myMachines[0][2] > myMachines[1][2]):
    print(totalPulls)
    
    mNum = myMachines[0][0]
    mPulls = myMachines[0][1]
    mAvg = myMachines[0][2]
    
    val = use_machine(0, 10)
    newAvg = (mAvg * mPulls + val)/(mPulls+1)
    myMachines[0][2] = newAvg
    myMachines[0][1] += 1
    totalPulls += 1
    
    money += val - 10
    print(money)
  
  myMachines = sorted(myMachines, key=lambda m: m[2], reverse=True)

  
  
  
  
  
  
  
  
  


display(myMachines)

print("Total pulls: " + str(totalPulls))
print("Money: " + str(money))






