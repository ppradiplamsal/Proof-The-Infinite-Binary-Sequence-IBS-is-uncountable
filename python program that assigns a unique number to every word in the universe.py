def generate_n_primes(N):
  primes  = []
  chkthis = 2
  while len(primes) < N:
     ptest    = [chkthis for i in primes if chkthis%i == 0]
     primes  += [] if ptest else [chkthis]
     chkthis += 1
  return primes


def f(x):
    lsString = tuple(list(x))
    lenn = len(lsString)
    lsPrimes = generate_n_primes(lenn)
    prod = 1
    for i in range(lenn):
        prod*=lsPrimes[i]**ord(lsString[i])

    return prod


print(f("bapple"))
