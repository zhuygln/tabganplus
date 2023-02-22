import asyncio
import time
import random

async def generate_data():
    while True:
        # Generate some output data
        data = [random.random() for _ in range(10000)]
        
        # Yield the data for the other function to use
        yield data
        
        # Wait for 5 seconds before generating more data
        await asyncio.sleep(5)

async def process_data(data):
    # Perform some CPU-bound calculations on the data
    result = sum(x * x for x in data)
    
    # Print the result
    print("Result: {}".format(result))

async def main(num_iterations):
    start_time = time.perf_counter()
    
    # Create the async generators
    data_generator = generate_data()
    
    # Create a list to hold the tasks
    tasks = []
    
    # Process the data as it becomes available
    for i in range(num_iterations):
        # Get the next data item from the generator
        data = await data_generator.__anext__()
        
        # Create a new task to process the data item
        task = asyncio.create_task(process_data(data))
        tasks.append(task)
    
    # Wait for all tasks to complete
    await asyncio.gather(*tasks)
    
    end_time = time.perf_counter()
    print("Elapsed time: {:.2f} seconds".format(end_time - start_time))

if __name__ == '__main__':
    # Run the program for 30 iterations
    asyncio.run(main(30))
# Elapsed time: 145.08 seconds