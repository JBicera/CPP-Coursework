import random

#Represents individual solution
class Chromosome:
    def __init__(self,size):
        #Number of queens on chess board
        self.size = size 
        #Order of queen's row positions for each column in board (Represented as a string)
        self.genes = [random.randint(1, size) for _ in range(size)]
    
    #Define how strings are printed
    def __str__(self):
        return str(self.genes)
    
    #Function to mutate one column of the board to somethign else
    def mutate(self):
        size = len(self.genes)
        c = random.randint(0, size-1)
        m = random.randint(1,size)
        self.genes[c] = m
    
    #Fitness function for Steepest Ascent Hill-Climbing
    def fitnessHill(self):
        count = 0
        for i in range (self.size - 1):
            for j in range(i+1, self.size):
                if self.genes[i] != self.genes[j] and abs(self.genes[i] - self.genes[j]) != abs(i - j):
                    count += 1
        return count
    
    #Fitness function for Genetic Algorithm
    def fitnessGenetic(self):
        horizontalCollisions = sum(self.genes.count(queen) - 1 for queen in self.genes) / 2
        diagonalCollisions = 0

        #List of diagonals
        rightDiagonal = [0] * (2* self.size)
        leftDiagonal = [0] * (2* self.size)
        #Calculate the counts of queens down the diagonals
        for i in range(self.size):
            leftDiagonal[self.genes[i] + i - 1] += 1
            rightDiagonal[len(self.genes) - i + self.genes[i] - 2] += 1
        
        #Now calculate diagonal collisions
        for i in range(2 * self.size - 1):
            count = 0
            #If there are more than one queen in the diagonal
            if leftDiagonal[i] > 1:
                count += leftDiagonal[i] - 1
            if rightDiagonal[i] > 1:
                count += rightDiagonal[i] - 1
            diagonalCollisions += count / (self.size - abs(i - self.size + 1))
        #Get fitness value from max - collisions
        maxFit = (self.size * (self.size - 1)) / 2 #23
        return int(maxFit - horizontalCollisions - diagonalCollisions)

#Probability of chromosome being picked from population
def probability(chromosome, maxFitnessPop):
    return chromosome.fitnessGenetic()/maxFitnessPop

#Randomly selects a chromosome based on the probabilities
#Higher probability chromosomes are more likely to be selected and vice versa
def randomSelection(population, probabilities):
    #Uses roulette random selection
    cumulativeProb = 0
    #Make pair of chromosomes in population with their probability
    populationProbabilities = zip(population, probabilities)
    #Calculate total probability
    sumProb = sum(probability for chromosome, probability in populationProbabilities)
    randValue = random.uniform(0, sumProb)
    #Loop through population and its probabilities
    for chromosome, probability in zip(population, probabilities):
        #Add to cumulative
        cumulativeProb += probability
        if cumulativeProb >= randValue:
            return chromosome

#Combines genes of both parents
def reproduce(x,y):
    n = len(x.genes)
    #Random integer in between
    c = random.randint(0, n - 1)
    child = Chromosome(n) #New child of length n
    child.genes = x.genes[0:c] + y.genes[c:n] #New genes are combination of parents genes
    return child 

#Genetic Algorithm to evolve population of chromosomes
def geneticAlgorithm(population,fitnessGenetic):
    newPopulation = []
    #Calculate max fitness value in the population
    maxFitness = max([fitnessGenetic(chromosome) for chromosome in population])
    #Calculate probabilities for each chromosome in the population
    probabilities = [probability(chromosome,maxFitness) for chromosome in population]
    mutationProb = 0.03
    #Loop through population
    for _ in range (len(population)):
        #Selection: Select two parent chromosomes
        x = randomSelection(population, probabilities)
        y = randomSelection(population, probabilities)
        #Crossover: Create child chromosome 
        childChromosome = reproduce(x,y)
        #Mutation: Small chance child mutates
        if random.random() < mutationProb:
            childChromosome.mutate()
        #Accepting: Add child into the population
        newPopulation.append(childChromosome)
        #Test: If new condition is satisfied (Max fitness possible is found)
        if childChromosome.fitnessGenetic() == maxFitness:
            break
    #Replace: Send new generation back into algorithm
    return newPopulation

#Steepest-Ascent Hill Climbing Algorithm
def hillClimbAlgorithm(initChromosome, maxIterations):
    for _ in range(maxIterations):
        neighbors = []
        for i in range(initChromosome.size):
            for j in range(1,initChromosome.size + 1):
                #Generate new neighbors by moving queen position one column
                neighbor = Chromosome(initChromosome.size)
                neighbor.genes = initChromosome.genes.copy()
                neighbor.genes[i] = j
                neighbors.append(neighbor)
        #Get the highest valued neighbor
        highestChromosome = max(neighbors, key = lambda neighbor: neighbor.fitnessHill())
        #If neighbor is better than initial then local maxima found
        if highestChromosome.fitnessHill() <= initChromosome.fitnessHill():
            break
        else:
            #Move to best neighbor
            initChromosome = highestChromosome
    return initChromosome

#8-queen generator
def generate8Queen(size, num):
    instances = []
    for _ in range(num):
        #Create random boards and add them to list
        instance = Chromosome(size)
        instances.append(instance)
    #Return list
    return instances

#Prints Board
def printBoard(board):
    for row in board:
        print(" ".join("Q" if val == 1 else "x" for val in row))

def main():
    queenCount = 8
    populationSize = 100
    generation = 0
    maxFitnessVal = (queenCount * (queenCount - 1)) / 2
    maxIterations = 1000
    solvedCount = 0
    totalInstances = 100
    print("Project 2 CS 4200 by Joshua Bicera")
    print("8-Queen Problem - Steepest Ascent Hill Climbing ")
    print("-----------------------------------------------")
    #Generate 100 instances of an 8-queen board
    testInstances = generate8Queen(queenCount, totalInstances)
    for index, instance in enumerate(testInstances, 1):
        solution = hillClimbAlgorithm(instance, maxIterations)
        if solution.fitnessHill() == maxFitnessVal:
            print("Instance {}: Solution".format(index))
            board = [[1 if i + 1 == gene else 0 for i in range(queenCount)] for gene in solution.genes]
            printBoard(board)
            solvedCount += 1
        else:
            print("Instance {}: Not Solved".format(index))
    print("------------------------------")
    percentageSolved = (solvedCount/totalInstances) * 100
    print("Percentage of instances solved: {:.2f}%".format(percentageSolved))

    print("8-Queen Problem - Genetic Algorithm")
    print("------------------------------------")
    #Initialize population with some random chromosomes
    population = [Chromosome(queenCount) for _ in range (populationSize)]

    #Run genetic algorithm until perfect solution is found
    while not maxFitnessVal in [chromosome.fitnessGenetic() for chromosome in population]:
        population = geneticAlgorithm(population, Chromosome.fitnessGenetic)
        generation += 1
    for chromosome in population:
        if chromosome.fitnessGenetic() == maxFitnessVal:
            print("One of the solutions: ")
            board = [[1 if i + 1 == chromosome.genes[j] else 0 for i in range(queenCount)] for j in range(queenCount)]
            printBoard(board)
            break
    print(" Solved in generation: ", generation)
    
    
main()