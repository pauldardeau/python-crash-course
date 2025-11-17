# NOTE: this is more advanced python code

import threading
import math


class PrimeNumberAnalyzer(threading.Thread):
    def __init__(self, starting_num, ending_num):
        super(PrimeNumberAnalyzer,self).__init__()
        self.starting_num = starting_num
        self.ending_num = ending_num
        self.primes_found = []

    def run(self):
        num_range = self.ending_num - self.starting_num + 1

        for i in range(num_range):
            eval_number = self.starting_num + i
            # we already know that prime numbers are not divisible by 2
            # if the current number is even (divisible by 2), skip it
            if eval_number % 2 != 0:
                eval_num_sqrt = math.floor(math.sqrt(eval_number))
                j = 3
                evaluating = True
                while evaluating:
                    if j <= eval_num_sqrt:
                        if eval_number % j == 0:
                            self.primes_found.append(eval_number)
                            evaluating = False
                        else:
                            j += 2
                    else:
                        evaluating = False



num_thread_workers = 3
thread_workers = []

starting_num = 1000000
worker_range = 100000

print("creating thread workers... ")

# create thread workers
for i in range(num_thread_workers):
    thread_worker = PrimeNumberAnalyzer(starting_num, starting_num + worker_range)
    thread_workers.append(thread_worker)
    starting_num = starting_num + worker_range + 1

print("starting thread workers ...")

# start the thread workers
for thread_worker in thread_workers:
    thread_worker.start()

print("all thread workers started. waiting for them to complete ...")

# wait for them to complete
j = 0
for thread_worker in thread_workers:
    thread_worker.join()
    j += 1
    print("thread worker %d complete" % j)


tot_primes_found = 0

# retrieve the number of prime numbers found by each worker
for thread_worker in thread_workers:
    tot_primes_found += len(thread_worker.primes_found)

print("total number of prime numbers found: %d" % tot_primes_found)

