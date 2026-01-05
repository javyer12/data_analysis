# Generate a function that print infinity prime numbers
# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# def generate_infinite_primes():
#     num = 2
#     while True:
#         if is_prime(num):
#             yield num
#         num += 1

# print(is_prime(2769433))  # True
# for prime in generate_infinite_primes():
#     print(prime)
#     if prime > prime + 1:  
#         break


import time

class Timer:
    def __enter__(self):
        self.start_time = time.time()
        return self.start_time

    def __exit__(self):
        ended_time = time.time()
        elapsed_time = ended_time - self.start_time
        print(f"Elapsed time: {elapsed_time} seconds")

timer = Timer()
timer.__enter__()
for i in range(1000000):
    print(i)

timer.__exit__()