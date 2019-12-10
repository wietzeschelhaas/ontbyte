import random
problemList = list(range(1, 146));

while (len(problemList) > 0):
    rng = random.randrange(len(problemList));
    print(problemList.pop(rng));
