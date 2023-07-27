import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time


# fig, ax = plt.subplots()
# successful_completions = [0]  # Initial value for successful completions
# timestamps = [time.time()]    # Initial timestamp


# def update(frame):
#     # Calculate the number of successful completions and current timestamp
#     success_count = successful_completions[-1] + 1
#     timestamp = time.time()

#     # Append the new data to the lists
#     successful_completions.append(success_count)
#     timestamps.append(timestamp)

#     # Limit the data shown on the graph to the last 60 seconds (adjust as needed)
#     cutoff_time = timestamp - 60

#     while timestamps[0] < cutoff_time:
#         del timestamps[0]
#         del successful_completions[0]

#     # Clear the current plot and plot the updated data
#     ax.clear()
#     ax.plot(timestamps, successful_completions)
#     ax.set_xlabel("Time")
#     ax.set_ylabel("Successful Completions")
#     ax.set_title("Real-Time Successful Completions vs. Time")


# ani = animation.FuncAnimation(fig, update, interval=1000)  # 1000ms (1 second) update interval
# plt.show()













def factor_list(list):
    # Your loop logic here
    i = 1
    for num in random_list:
        print(f"[{i}]\tFactors of {num}: {factorize_brute_force(num)}")
        i+=1
        # successful_completions[-1] += 1



def generate_random_numbers(lower_limit, upper_limit, num_integers):
	random_list = random.sample(range(lower_limit, upper_limit + 1), num_integers)

	return random_list


def factorize_brute_force(n):
    factors = []
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 1:
        factors.append(n)
    return factors





random_list = generate_random_numbers(2,1000000, 100000)


start_time = time.time()
factor_list(random_list)
total_time = time.time() - start_time

print("Total time: " + str(total_time))
