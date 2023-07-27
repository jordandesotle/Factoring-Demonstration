# =============================================================================
# FILE: factor.py
#
# DESCRIPTION: This script demonstrates different methods of determining whether
#              a large number is prime or not. There are three methods implemented
#			   in this program:
#
# SECTION 1: PRIMALITY TESTS
#	- Miller-Rabin Primality Test
#	- Baillie-PSW Test
#	- AKS Primality Test
# SECTION 2: FACTORING METHODS
#	- Brute Force
#	- Pollards Rho Algorithm
#
#	- Difference of squares
#	- Pollards p -1
#
#
#
# AUTHOR: Jordan De Sotle
# DATE CREATED: July 27, 2023
# LAST MODIFIED: July 27, 2023
#
# USAGE: python factor.py
# =============================================================================

# Imports
import math
import random
import sympy

# ============================== Helper Functions =============================

# Generates a list of random numbers to test
# Takes in a lower limit, an upper limit, and the number of numbers to be generated
def generate_random_numbers(lower_limit, upper_limit, num_integers):
	random_list = random.sample(range(lower_limit, upper_limit + 1), num_integers)

	return random_list

# Returns the method of factoring
def get_factor_method(method):
    if method == 1:
        method_name = "Brute Force Factorization"
        test_function = factorize_brute_force
    elif method == 2:
        method_name = "Pollards Rho Algorithm"
        test_function = pollards_rho_factorize
    else:
        print("Invalid method selected.")
        return
    
    print(method_name + ":")
    
    return test_function

# Returns the method of checking whether a number is prime or not
def get_prime_check_method(method):
    if method == 1:
        test_name = "Miller-Rabin Primality Test"
        test_function = miller_rabin_test
    elif method == 2:
        test_name = "Baillie-PSW Test"
        test_function = is_prime_baillie_psw
    elif method == 3:
        test_name = "AKS Primality Test"
        test_function = is_prime_aks
    else:
        print("Invalid method selected.")
        return

    print(test_name + ":")

    return test_function

# Checks a list of numbers and determines if each number is prime or not
def check_if_numslist_prime(method, num_list):
    
    test_func = get_prime_check_method(method)
    
    prime_results = [(num, test_func(num)) for num in num_list]
    for num, is_prime in prime_results:
        print(f"{num} is prime: {is_prime}")

# Checks one number and determines if it is prime or not
def check_if_num_prime(method, num):
    
    test_func = get_prime_check_method(method)
    
    print(f"{num} is prime: {test_func(num)}")

# Factors a list of numbers
def factor_nums(method, num_list):

    test_func = get_factor_method(method)

    factor_results = [(num, test_func(num)) for num in num_list]
    for num, result in factor_results:
        print(f"Factors of {num}: {result}")

# Factors a number
def factor_num(method, num):

    test_func = get_factor_method(method)
    print(f"Factors of {num}: {test_func(num)}\n")


# =============================================================================
# SECTION 1A: Miller-Rabin Primality Test
# =============================================================================

def miller_rabin_test(n, k=5):
    
    if n <= 1:
        return False
    if n <= 3:
        return True

    # Write n as 2^r * d + 1, where d is odd
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    def is_witness(a):
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            return False
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                return False
        return True

    for _ in range(k):
        a = random.randint(2, n - 2)
        if is_witness(a):
            return False

    return True

# =============================================================================
# SECTION 1B: Baillie-PSW Test
# =============================================================================

def is_perfect_square(n):
    sqrt_n = int(math.isqrt(n))
    return sqrt_n * sqrt_n == n

def is_prime_trial_division(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    # Trial division for factors up to sqrt(n)
    max_divisor = int(math.sqrt(n))
    divisor = 5
    while divisor <= max_divisor:
        if n % divisor == 0 or n % (divisor + 2) == 0:
            return False
        divisor += 6

    return True

def is_prime_baillie_psw(n):
    if n < 2:
        return False
    if n == 2 or n == 3 or n == 5:
        return True

    if n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
        return False

    if is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4):
        return False

    return is_prime_trial_division(n)

# =============================================================================
# SECTION 1C: AKS Primality Test
# =============================================================================

def is_prime_aks(n):
    return sympy.isprime(n)
        
# =============================================================================
# SECTION 2A: Brute Force Factoring
# =============================================================================

def factorize_brute_force(n):
    factors = []
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 1:
        factors.append(n)
    return factors

# Example usage:
# number = 123456
# print(f"Factors of {number}: {factorize_brute_force(number)}")


# =============================================================================
# SECTION 2B: Pollards Rho Algorithm
# =============================================================================

def pollards_rho_factorize(n):
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def pollard_rho(n):
        x, y, d = 2, 2, 1
        f = lambda x: (x**2 + 1) % n
        while d == 1:
            x = f(x)
            y = f(f(y))
            d = gcd(abs(x - y), n)
        return d

    factors = []
    while n > 1:
        factor = pollard_rho(n)
        factors.append(factor)
        n //= factor
    return factors

# Example usage:
# number = 987654321
# print(f"Factors of {number}: {pollards_rho_factorize(number)}")

# =============================================================================
# MAIN EXECUTION
# =============================================================================

# Select the method
#   Checking Primality      Factoring
#	1: Miller-Rabin         1: Brute Force
#	2: Baillie-PSW          2: Pollards
#	3: AKS


method = 1
num = 1065240411651033974542969

# increasingly large prime numbers
test_arr_1 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157]
test_arr_2 = [3, 5, 11, 17, 31, 41, 59, 67, 83, 109, 127, 157, 179, 191, 211, 241, 277, 283, 331, 353, 367, 401, 431, 461, 509, 547, 563, 587, 599, 617, 709, 739, 773, 797]
test_arr_3 = [5, 11, 31, 59, 127, 179, 277, 331, 431, 599, 709, 919, 1063, 1153, 1297, 1523, 1787, 1847, 2221, 2381, 2477, 2749, 3001, 3259, 3637, 3943, 4091, 4273, 4397]
test_arr_4 = [11, 31, 127, 277, 709, 1063, 1787, 2221, 3001, 4397, 5381, 7193, 8527, 9319, 10631, 12763, 15299, 15823, 19577, 21179, 22093, 24859, 27457, 30133, 33967]
test_arr_5 = [31, 127, 709, 1787, 5381, 8527, 15299, 19577, 27457, 42043, 52711, 72727, 87803, 96797, 112129, 137077, 167449, 173867, 219613, 239489, 250751, 285191]
test_arr_6 = [127, 709, 5381, 15299, 52711, 87803, 167449, 219613, 318211, 506683, 648391, 919913, 1128889, 1254739, 1471343, 1828669, 2269733, 2364361, 3042161]
test_arr_7 = [709, 5381, 52711, 167449, 648391, 1128889, 2269733, 3042161, 4535189, 7474967, 9737333, 14161729, 17624813, 19734581, 23391799, 29499439, 37139213]
test_arr_8 = [5381, 52711, 648391, 2269733, 9737333, 17624813, 37139213, 50728129, 77557187, 131807699, 174440041, 259336153, 326851121, 368345293, 440817757]
test_arr_9 = [52711, 648391, 9737333, 37139213, 174440041, 326851121, 718064159, 997525853, 1559861749, 2724711961, 3657500101, 5545806481, 7069067389]
test_arr_10 = [648391, 9737333, 174440041, 718064159, 3657500101, 7069067389, 16123689073, 22742734291, 36294260117, 64988430769, 88362852307, 136395369829]
test_arr_11 = [9737333, 174440041, 3657500101, 16123689073, 88362852307, 175650481151, 414507281407, 592821132889, 963726515729, 1765037224331, 2428095424619]
test_arr_12 = [174440041, 3657500101, 88362852307, 414507281407, 2428095424619, 4952019383323, 12055296811267, 17461204521323, 28871271685163, 53982894593057]

# test each algorithm for determining prime number
# check_if_num_prime(method, num)

# read from file of large prime numbers to test



# generates a random list of numbers
random_list = generate_random_numbers(2,1000, 100)

# need to determine if each number is prime or not using a test method
# factor_num(method, num)

# factor_nums(method, random_list)
factor_num(method, 10403)


#random_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 7919]

# check_if_nums_prime(method, random_list)

print(88362852307 * 12055296811267)


# debug / print statements in factoring functions


# check_if_numslist_prime(1, random_list)
# factor_nums(1, random_list)


check_if_num_prime(1, num)


factor_num(2, num)