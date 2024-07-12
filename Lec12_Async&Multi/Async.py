import time


def count():
    print("One")
    time.sleep(1)
    print("Two")


start_time = time.perf_counter()
for i in range(3):
    count()
end_time = time.perf_counter()
time_passed = end_time - start_time

print(f"Using the normal synchronous approach the function count() will be executed in {time_passed:0.2f} seconds")
