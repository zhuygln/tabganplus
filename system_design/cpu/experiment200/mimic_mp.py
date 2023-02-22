import multiprocessing
import time
import shutil
import os
import random

filename = "data_gen.csv"
new_filename = "data_eval.csv"
random.seed(9468)

def trainning(i):
    # Generate a random wait time between 0 and 20 seconds
    wait_time = random.random() * 200
    time.sleep(wait_time)
    
    # Simulate a CPU-bound task by generating a large list of numbers
    numbers = [x * x for x in range(1000000)]
    
    with open(filename, "a") as file:
        file.write("New data row {}\n".format(i+1))

def evaluation():
    # Read the last line of the file and get the number at the end of the line
    with open(filename, "r") as file:
        lines = file.readlines()
        if len(lines) > 0:
            last_line = lines[-1]
            last_number = int(last_line.split()[-1])
        else:
            last_number = 0
    
    # Simulate a CPU-bound task by generating a large list of numbers using the last number in the file
    numbers = [x * x for x in range(last_number, last_number + 1000000)]
    
    shutil.copy2(filename, new_filename)
    if os.path.isfile(new_filename):
        print("New file created: {}".format(new_filename))

def main():
    start_time = time.perf_counter()
    with multiprocessing.Pool() as pool:
        write_results = []
        for i in range(5):
            write_result = pool.apply_async(trainning, (i,))
            write_results.append(write_result)
        
        for write_result in write_results:
            write_result.get()
            copy_result = pool.apply_async(evaluation)
            copy_result.get()

    end_time = time.perf_counter()
    print("Elapsed time: {:.2f} seconds".format(end_time - start_time))

if __name__ == '__main__':
    main()
#Elapsed time: 29.75 seconds