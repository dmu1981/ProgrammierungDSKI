def get_twin_primes(numbers):
  """
  Returns a list of twin primes from the input list.
  Twin primes are pairs of primes that differ by 2 (e.g., 3,5 or 5,7).
  Only returns primes that have their twin also present in the list.
  """
  def is_prime(n):
    if n < 2:
      return False
    if n == 2:
      return True
    if n % 2 == 0:
      return False
    for i in range(3, int(n**0.5) + 1, 2):
      if n % i == 0:
        return False
    return True
  
  # Convert to set for faster lookup
  num_set = set(numbers)
  twin_primes = []
  
  for num in numbers:
    if is_prime(num):
      # Check if twin prime exists in the list
      if (num + 2 in num_set and is_prime(num + 2)) or \
         (num - 2 in num_set and is_prime(num - 2)):
        if num not in twin_primes:
          twin_primes.append(num)
  
  return sorted(twin_primes)