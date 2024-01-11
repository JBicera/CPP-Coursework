import queue
import random
import os

# Job class to hold both the job's number and burst time
class Job:
    def __init__(self, name, burstTime):
        self.name = name
        self.burstTime = burstTime

# Generate random jobs for testing
def generateRandomJobs(numJobs, maxBurstTime):
    jobs = []
    for i in range(1, numJobs + 1): 
        jobName = f"Job{i}"
        burstTime = random.randint(1, maxBurstTime)
        jobs.append(Job(jobName, burstTime))
    return jobs

# FCFS Scheduling Algorithm
def fcfs(input,size):
    jobs = input.copy()
    totalTime = 0
    turnaroundTimes = []
    avgTurnAround = 0
    for job in jobs:
        totalTime += job.burstTime
        turnaroundTimes.append(totalTime)
    for i in turnaroundTimes:
        avgTurnAround += i
    return avgTurnAround/size, turnaroundTimes

# SJF Scheduling Algorithm
def sjf(input,size):
    jobs = input.copy()
    jobs.sort(key=lambda x: x.burstTime)
    totalTime = 0
    turnaroundTimes = []
    avgTurnAround = 0
    for job in jobs:
        totalTime += job.burstTime
        turnaroundTimes.append(totalTime)
    for i in turnaroundTimes:
        avgTurnAround += i
    return avgTurnAround/size, turnaroundTimes

# Round Robin Scheduling Function
def roundRobin(input, size, timeSlice):
    jobs = input.copy()
    totalTime = 0
    turnaroundTimes = []
    avgTurnAround = 0
    while jobs:
        currentJob = jobs.pop(0)
        if currentJob.burstTime > timeSlice:
            jobs.append(Job(currentJob.name, currentJob.burstTime - timeSlice))
            totalTime += timeSlice
        else:
            totalTime += currentJob.burstTime
        turnaroundTimes.append(totalTime)
    for i in turnaroundTimes:
        avgTurnAround += i
    return avgTurnAround/size, turnaroundTimes

# Gets jobs from jobs.txt file
def getJobsFromFile(filename):
    jobs = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        i = 0
        while i < len(lines):
            name = lines[i].strip()
            burst = int(lines[i + 1].strip())
            jobs.append(Job(name, burst))
            i += 2
    return jobs

# Round Robin Scheduling Function
def roundRobin(input, size, timeSlice):
    jobs = input.copy()
    totalTime = 0
    turnaroundTimes = []
    avgTurnAround = 0
    while jobs:
        currentJob = jobs.pop(0)
        if currentJob.burstTime > timeSlice: # If current job is greater than time slice 
            jobs.append(Job(currentJob.name, currentJob.burstTime - timeSlice)) # Process time slice then add remaining back to queue
            totalTime += timeSlice
        else:
            totalTime += currentJob.burstTime # If current job is already less than time slice
            turnaroundTimes.append(totalTime) # Process the rest
    for i in turnaroundTimes:
        avgTurnAround += i
    return avgTurnAround/size, turnaroundTimes

# Generate a random list of jobs and then return results of each algorithm
def testJobs(size, maxBurstTime, trials):
    fcfsResults, sjfResults, roundRobin2, roundRobin5 = 0,0,0,0
    for i in range(trials):
        jobs = generateRandomJobs(size, maxBurstTime)
        fcfsResults += fcfs(jobs,size)[0]
        sjfResults += sjf(jobs,size)[0]
        roundRobin2 += roundRobin(jobs,size,2)[0]
        roundRobin5 += roundRobin(jobs,size,5)[0]
    return round(fcfsResults/trials,2), round(sjfResults/trials,2), round(roundRobin2/trials,2), round(roundRobin5/trials,2)

def printTesting(numJobs,maxBurstTime, trials):
    # Print results with rounded values
    print()
    print(f"Average turnaround time for {numJobs} Jobs and {trials} trials:")
    print("----------------------------------------------------------------")
    fcfsResult, sjfResult, rr2Result, rr5Result = testJobs(numJobs, maxBurstTime, trials)
    print(f"First come first serve: {fcfsResult}")
    print(f"Shortest job first: {sjfResult}")
    print(f"Round-Robin with Time Slice = 2: {rr2Result}")
    print(f"Round-Robin with Time Slice = 5: {rr5Result}")
    print()

# Runs testing for part 2
def main():
    trials = 20
    maxBurstTime = 20.0 # Can adjust if needed
    printTesting(5, maxBurstTime, trials) # 5 Job Testing
    printTesting(10, maxBurstTime, trials) # 10 Job Testing
    printTesting(15, maxBurstTime, trials) # 15 Job Testing
    '''
    numJobs = 15
    filename = "jobs15.txt"
    filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)

    # Get jobs from jobs.txt
    txtJobs = getJobsFromFile(filename)
    # First come first serve
    fcfsResults = fcfs(txtJobs,numJobs)
    # Shortest Job First 
    sjfResults = sjf(txtJobs,numJobs)
    # Round-Robin with Time Slice = 2
    timeSlice2Results = roundRobin(txtJobs, numJobs, 2)
    # Round-Robin with Time Slice = 5
    timeSlice5Results = roundRobin(txtJobs, numJobs, 5)

    # Print results with rounded values
    print(f"Random Jobs: {[(job.name, job.burstTime) for job in txtJobs]}")
    print(f"First come first serve: {round(fcfsResults[0], 2)}, {fcfsResults[1]}")
    print(f"Shortest job first: {round(sjfResults[0], 2)}, {sjfResults[1]}")
    print(f"Round-Robin with Time Slice = 2: {round(timeSlice2Results[0], 2)}, {timeSlice2Results[1]}")
    print(f"Round-Robin with Time Slice = 5: {round(timeSlice5Results[0], 2)}, {timeSlice5Results[1]}")
    '''



if __name__ == "__main__":
    main()
