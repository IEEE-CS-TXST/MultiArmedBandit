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


