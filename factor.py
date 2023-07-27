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
#	- Elliptic Curve Factorization
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

# Checks a list of numbers and determines if each number is prime or not
def check_if_numslist_prime(method, num_list):
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
    
    prime_results = [(num, test_function(num)) for num in num_list]
    for num, is_prime in prime_results:
        print(f"{num} is prime: {is_prime}")


# Checks one number and determines if it is prime or not
def check_if_num_prime(method, num):
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
    
    print(f"{num} is prime: {test_function(num)}")

def factor_num(method, num):
	if method == 1:
		method_name = "Brute Force Factorization"
		test_function = factorize_brute_force
	elif method == 2:
		method_name = "Pollards Rho Algorithm"
		test_function = pollards_rho_factorize
	elif method == 3:
		method_name = "Elliptic Curve Factorization"
		test_function = ecm_factorize
	else:
	    print("Invalid method selected.")
	    return

	print(method_name + ":")

	print(f"{num} is prime: {test_function(num)}")


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
# SECTION 2C: Elliptic Curve Factoring
# =============================================================================

def ecm_factorize(n, max_steps=10000):
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def elliptic_curve_point_addition(p, a, b, x1, y1, x2, y2):
        if x1 == x2 and y1 == y2:
            m = (3 * x1**2 + a) * pow(2 * y1, -1, p)
        else:
            m = (y2 - y1) * pow(x2 - x1, -1, p)
        x3 = (m**2 - x1 - x2) % p
        y3 = (m * (x1 - x3) - y1) % p
        return x3, y3

    def elliptic_curve_scalar_multiplication(p, a, b, x, y, scalar):
        result_x, result_y = x, y
        scalar -= 1
        while scalar:
            if scalar & 1:
                result_x, result_y = elliptic_curve_point_addition(p, a, b, result_x, result_y, x, y)
            x, y = elliptic_curve_point_addition(p, a, b, x, y, x, y)
            scalar >>= 1
        return result_x, result_y

    # ECM parameters
    a, b = 0, 7

    # Random starting point
    x, y = random.randint(1, n - 1), random.randint(1, n - 1)

    for _ in range(max_steps):
        x, y = elliptic_curve_scalar_multiplication(n, a, b, x, y, random.randint(1, n - 1))
        factor = gcd(abs(x - x), n)
        if factor > 1 and factor < n:
            return [factor, n // factor]

    return [n]

# Example usage:
# number = 1234567891011
# print(f"Factors of {number}: {ecm_factorize(number)}")


# =============================================================================
# MAIN EXECUTION
# =============================================================================

# Select the method
#	1: Miller-Rabin
#	2: Baillie-PSW
#	3: AKS)
method = 1
num = 53
# test each algorithm for determining prime number
check_if_num_prime(method, num)

# read from file of large prime numbers to test



# generates a random list of numbers
random_list = generate_random_numbers(2,1000, 100)

# need to determine if each number is prime or not using a test method
factor_num(method, num)


#random_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 7919]

# check_if_nums_prime(method, random_list)





# debug / print statements in factoring functions