import random

H = [7, 4, 10, 5]
D = [3, 10, 6, 2]

# initialize avg happiness lists
hv1 = []
hv2 = []
hv3 = []
hv4 = []


# finds average happiness of each cafe and them returns the one with the highest
def test_happy() -> int:
    happy = []
    count1 = 0
    for i in hv1:
        count1 += i
    happy.append(count1 / len(hv1))
    count2 = 0
    for i in hv2:
        count2 += i
    happy.append(count2 / len(hv2))
    count3 = 0
    for i in hv3:
        count3 += i
    happy.append(count3 / len(hv3))
    count4 = 0
    for i in hv4:
        count4 += i
    happy.append(count4 / len(hv4))
    return happy.index(max(happy))


def eGreedy(e=10):
    total = 0
    # initialize first 4 days
    hv1.append(random.normalvariate(H[0], D[0]))
    hv2.append(random.normalvariate(H[1], D[1]))
    hv3.append(random.normalvariate(H[2], D[2]))
    hv4.append(random.normalvariate(H[3], D[3]))
    # start going through rest of days
    for i in range(196):
        r = random.random()
        # goes to random
        if r < (e / 100):
            x = random.randint(0, 3)
            if x == 0:
                hv1.append(random.normalvariate(H[0], D[0]))
            elif x == 1:
                hv2.append(random.normalvariate(H[1], D[1]))
            elif x == 2:
                hv3.append(random.normalvariate(H[2], D[2]))
            else:
                hv4.append(random.normalvariate(H[3], D[3]))
        # goes to cafe with the highest average happiness
        else:
            if test_happy() == 0:
                hv1.append(random.normalvariate(H[0], D[0]))
            elif test_happy() == 1:
                hv2.append(random.normalvariate(H[1], D[1]))
            elif test_happy() == 2:
                hv3.append(random.normalvariate(H[2], D[2]))
            else:
                hv4.append(random.normalvariate(H[3], D[3]))

    # combines all happiness lists and adds up total
    final_list = hv1 + hv2 + hv3 + hv4
    for i in final_list:
        total += i
    return total


print(eGreedy())