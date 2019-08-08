'''
Genetic Algorithm

 - How does it work?
    self approach aim to solve the problem of find weights that best fit the objective function,
    for exemple, to find the best set of parameters in a Machine Learning algorithm, or maybe a 
    set of items which maximize the total value of a bin packing.
    There are many exemples and we will find a lot of them on the folders in self repository. Let's
    go practicing.
 - GA Dictionary
    Gene: A single component of the answer
    Cromossome: A set of genes which determine a answer
    Population: A set of cromossomes
    Cross Over: Cross validation between cromossomes, result a new cromossome
    Mutation: Changes on gene of the cromossome, it will affect the fitness
    
'''

from random import *

class GeneticAlgorithm:
    def __init__(
        self, # The class itself 
        population_size, # Number of results is going to be generated at once
        range_, # Still undefined
        selection_score, # Number of candidates to pass through round
        selection_num, # Number of parents candidates to be chosen
        mute_ratio, # Mutation Ratio, to descide who stayes or who get out
        # Caracteristics is a dictionary that seems like this:
        # caracteristics: {
        #   result_block_size: Number of genes to be generated
        #   result_item_range: Tuple with the initial and final value each gene may get
        # }
        caracteristics, # Written above
        fitness # Function to calculate the efficiency of a single result
    ):
        self.generations = generations
        self.population_size = population_size
        self.range = range_
        self.selection_score = selection_score
        self.selection_num = selection_num
        self.mute_ratio = mute_ratio

        self.caracteristics = caracteristics
        self.fitness = fitness

        '''
        results is a dictionary with the following elements
        results = {
            weights: list of genes
            efficiency: efficiency of the wheights applicable to the fitness function
        }
        '''
        self.result = dict() # Written above

    def __efficiency(self, result):
        return self.fitness(result)

    '''
    This fuction get the abstract elements and produce a random result, could not be the best
    one but surely works. The aproach used here will be random genes.
    '''
    def __population_initializer(self):
        population = list()
        start, end = self.caracteristics.result_item_range
        for i in range(self.population_size):
            result = {
                'weights': [],
                'efficiency': 0
            }
            for j in range(self.caracteristics.result_block_size):
                result.weights.append(randrange(start, end+1))
            result.efficiency = __efficiency(result)
            population.append(result)

        return population


def __main__():
    print('Under Construction')