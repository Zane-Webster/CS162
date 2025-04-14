# create queues
premium = []
standard = []
economy = []

# fill queues based on input txt fie
with open("input queue-1.txt", "r") as file:
    for line in file:
        # sort names based on class
        if line[0] == "P":
            premium.append(line)
        elif line[0] == "S":
            standard.append(line)
        elif line[0] == "E":
            economy.append(line)

# prints value of queue, then pops it
def print_and_pop(queue, weight):
    for i in range(weight):
        # if queue is not empty (non-zero)
        if queue:
            print(queue[0])
            queue.pop(0)

# while there are still names in queues, print and pop first value of queues
while premium or standard or economy:
    print_and_pop(premium, 3)
    print_and_pop(standard, 2)
    print_and_pop(economy, 1)