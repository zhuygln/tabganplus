import time
import random
import multiprocessing

def generate_data(queue, num_iterations):
    for i in range(num_iterations):
        # Generate some output data
        data = [random.random() for _ in range(10000)]
        
        # Put the data in the queue for the other function to use
        queue.put(data)
        
        # Wait for 5 seconds before generating more data
        time.sleep(5)

def process_data(queue, num_iterations):
    for i in range(num_iterations):
        # Get the latest data from the queue
        data = queue.get()
        
        # Perform some CPU-bound calculations on the data
        result = sum(x * x for x in data)
        
        # Print the result
        print("Result: {}".format(result))

def main(num_iterations):
    start_time = time.perf_counter()
    
    # Create a multiprocessing queue to share data between the two functions
    queue = multiprocessing.Queue()
    
    # Start the two functions as separate processes
    data_process = multiprocessing.Process(target=generate_data, args=(queue, num_iterations))
    calculation_process = multiprocessing.Process(target=process_data, args=(queue, num_iterations))
    data_process.start()
    calculation_process.start()
    
    # Wait for the processes to finish
    data_process.join()
    calculation_process.join()
    
    end_time = time.perf_counter()
    print("Elapsed time: {:.2f} seconds".format(end_time - start_time))

if __name__ == '__main__':
    # Run the program for 30 iterations
    main(30)
# Elapsed time: 150.21 seconds