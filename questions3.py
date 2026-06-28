import time
import threading

#Factorial Big O
def calculate_factorial(n):
    if n == 0 or n == 1:
        return 1

    result = 1
    for i in range(2,n+1):
        result *= i
    return result

#without multi threading
def run_sequential():
    print("Sequential Processing")

    total_time_all_rounds = 0

    for round_num in range(1,11):
        start_time = time.perf_counter_ns()

        calculate_factorial(50)
        calculate_factorial(100)
        calculate_factorial(200)

        end_time = time.perf_counter_ns()

        time_elapsed = end_time - start_time
        total_time_all_rounds += time_elapsed
        print(f"Round {round_num:<2}: {time_elapsed:>10} ns")

    average_time = total_time_all_rounds / 10

    print(f"Average Time: {average_time:.0f} ns\n")

#multithreading  processing
def run_multithreading():
    print("Multithreading Processing")
    total_time_all_rounds = 0

    for round_num in range(1,11):
        start_time = time.perf_counter_ns()
        thread_50 =  threading.Thread(target=calculate_factorial, args=(50,))
        thread_100 = threading.Thread(target=calculate_factorial, args=(100,))
        thread_200 = threading.Thread(target=calculate_factorial, args=(200,))

        start_time = time.perf_counter_ns()

        thread_50.start()
        thread_100.start()
        thread_200.start()

        thread_50.join()
        thread_100.join()
        thread_200.join()

        end_time = time.perf_counter_ns()
        time_elapsed = end_time - start_time
        total_time_all_rounds += time_elapsed
        print(f"Round {round_num:<2}: {time_elapsed:>10} ns")

    average_time = total_time_all_rounds / 10
    print(f"Average Time: {average_time:.0f} ns\n")





if __name__ == "__main__":
    run_sequential()
    run_multithreading()

