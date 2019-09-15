#!/usr/bin/env python3

from typing import List, Tuple
from functools import reduce

primes: List[int] = []
non_primes: List[int] = []


def get_factors(n: int) -> List[int]:
	"""
	Gets the factors of n.
	"""
	return [i for i in range(1, n + 1) if n % i == 0]


def is_prime(n: int) -> bool:
	"""
	Returns True if n is prime.
	"""
	if n in non_primes:
		return False
	if n in primes:
		return True
	factors: List[int] = get_factors(n)
	output: bool = len(factors) <= 2
	if output:
		primes.append(n)
	else:
		non_primes.append(n)
	return output


def get_prime_factors(n: int) -> List[int]:
	"""
	Gets the prime factors of n.
	"""
	factors: List[int] = get_factors(n)

	if is_prime(n):
		return factors[-1:]

	larger_primes = get_prime_factors(factors[-2])

	smaller_primes = get_prime_factors(factors[1])

	return larger_primes + smaller_primes


def check_prime_factors(prime_factors: List[int]) -> int:
	"""
	Returns the product of the provided prime factors.
	"""
	return reduce(lambda x, y: x * y, prime_factors)


def main():
	user_input: int = int(input("Input a positive integer: "))
	prime_factors: List[int] = get_prime_factors(user_input)
	print(f"Prime Factors of {user_input}: ")
	print(prime_factors)

	print("")
	print("Checking to see if that's correct...")
	test_output: int = check_prime_factors(prime_factors)
	print(f"The test output was {test_output}.")
	print(f"Is that the same as the inputted number? {test_output == user_input}")

	print("")
	print("Primes discovered along the way: ")
	print(primes)

	print("Non Primes discovered along the way: ")
	print(non_primes)


if __name__ == "__main__":
	main()
