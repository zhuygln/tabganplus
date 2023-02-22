import time
import random
import concurrent.futures

def generate_data(num_iterations):
    for i in range(num_iterations):
        # Generate some output data
        data = [random.random() for _ in range(10000)]
        
        # Yield the data for the other function to use
        yield data
        
        # Wait for 5 seconds before generating more data
        time.sleep(5)

def process_data(data):
    # Perform some CPU-bound calculations on the data
    result = sum(x * x for x in data)
    
    # Print the result
    print("Result: {}".format(result))

def main(num_iterations):
    start_time = time.perf_counter()
    
    # Start the two functions using concurrent.futures
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        # Create a future for the data generator function
        data_future = executor.submit(generate_data, num_iterations)
        
        # Process the data as it becomes available
        for data in data_future.result():
            # Submit a new future for each data item to be processed
            executor.submit(process_data, data)
    
    end_time = time.perf_counter()
    print("Elapsed time: {:.2f} seconds".format(end_time - start_time))

if __name__ == '__main__':
    # Run the program for 30 iterations
    main(30)
# Elapsed time: 150.15 seconds
