import random



jobs = []
for i in range(50):
    deadline = random.randint(1, 40)
    profit = random.randint(1, 40)
    jobs.append((deadline, profit))


def sortByprofit(arr):
    return arr[1]

def sortByDeadline(arr):
    return arr[0]

# We sort all jobs by profit
# In descending order. This is the Greedy Algorithm
jobs.sort(key = sortByprofit, reverse = True)

# We irrigate through all our jobs, we then check if the current job that is being looked at,
# has the same deadline as
# any of the jobs, in the accepted jobs list.
def jobScheduling(arr):
    sequence= []
    sequence.append(arr.pop(0))
    for i in range(len(arr)):
        # Vi går fra 0 til hvor mange jobs vi har, minus 1.
        # Vi starter på 0 som betyr at den sjekker den første jobben. Også ser vi på den mest profitable i listen
        # accepted jobs har feks 3.
        if arr[i][0] not in [x[0]for x in sequence]:
            sequence.append(arr[i])
    return sequence

sequence = jobScheduling(jobs)
sequence.sort(key=sortByDeadline)

for i in range(len(sequence)):                   # formatet = job, Seq [i][1] for profit Seq [i][0] for deadline.
    print("Job nr: {}, Profit: {}, Deadline: {}".format(1+i, sequence[i][1], sequence[i][0]))