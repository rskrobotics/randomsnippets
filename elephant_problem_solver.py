łfrom
sys
import stdin

'''The unused imports are for the functionality that is commented out in "main"
part of the code which is not part of the task, but for plotting the time
complexity'''
import datetime
import os
from matplotlib import pyplot as plt
from operator import itemgetter


class Elephant_Problem:
    def __init__(self, N, masses, start_order, final_order):
        self.N = int(N.strip("\n"))
        self.masses = [int(i) for i in masses.strip("\n").split(" ")]
        self.start_order = [int(i) for i in start_order.strip("\n").split(" ")]
        self.final_order = [int(i) for i in final_order.strip("\n").split(" ")]
        permutation = [None] * self.N
        for i in range(self.N):
            permutation[self.final_order[i] - 1] = self.start_order[i]
        self.permutation_function = permutation
        self.minimal_weight = min(self.masses)

    def get_simple_cycles(self):
        '''Returns the permutation cycles of elephant problem based on
         permutation function'''
        processed = [False] * self.N
        cycles = []
        for i in range(1, self.N + 1):
            if not processed[i - 1]:
                current_cycle = [i]
                elephant_processed = i
                processed[i - 1] = True
                while self.permutation_function[elephant_processed - 1] != i:
                    elephant_processed = self.permutation_function[
                        elephant_processed - 1]
                    current_cycle.append(elephant_processed)
                    processed[elephant_processed - 1] = True
                cycles.append(current_cycle)
        return cycles

    def solve(self):
        '''Turn our permutation function into cycles'''

        cycles = self.get_simple_cycles()
        total_effort = 0
        for cycle in cycles:
            cycle_weight_sum = sum(
                [self.masses[elephant - 1] for elephant in cycle])
            amount_of_processed_elephants = len(cycle)
            min_cycle_weight = min(
                [self.masses[elephant - 1] for elephant in cycle])

            total_effort += min(
                cycle_weight_sum + (
                        amount_of_processed_elephants - 2) * min_cycle_weight,
                cycle_weight_sum + min_cycle_weight + (
                        amount_of_processed_elephants + 1) * self.minimal_weight)

        return total_effort


if __name__ == '__main__':
    # '''Task functionality'''
    # problem = Elephant_Problem(stdin.readline(), stdin.readline(),
    #                            stdin.readline(), stdin.readline())
    #
    # print(problem.solve())

    '''Added code for solving the problem for the "in" files in current dir
    and comparing to "out", plotting the time complexity on a graph. Just
    comment out the code in main and uncomment underneath and the relevant
    imports at top of the file'''
    folder_results = []
    for filename in os.listdir('.'):
        if filename.split(".")[-1] == "in":
            begin_time = datetime.datetime.now()
            with open(filename, 'r', encoding='utf-8') as f:
                problem = Elephant_Problem(f.readline(), f.readline(),
                                           f.readline(), f.readline())
                result = problem.solve()
                with open(filename.split(".")[0] + ".out", 'r',
                          encoding='utf-8') as o:
                    output_result = int(o.readline().strip("\n"))

                    print(
                        f"Data set: {filename}, output: {result}, {output_result}")
                    folder_results.append((
                        True if result == output_result else False,
                        problem.N,
                        (
                                datetime.datetime.now() - begin_time).total_seconds()))

    print(f"Folder results: {folder_results}")
    ss = sorted(folder_results, key=itemgetter(1))
    plt.plot([iteration[1] for iteration in ss],
             [iteration[2] for iteration in ss], '-*', color="green")
    plt.xlabel('Input Size [1]')
    plt.ylabel('Time of computation in [s]')
    plt.show()
