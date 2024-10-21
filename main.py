import time
from typing import Annotated

import typer

from obfuls2 import obfu_primes

def _ordinal(n: int) -> str:
    if 10 <= n % 100 <= 20:
        suffix = 'th'
    else:
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')
    return f"{n}{suffix}"


def main(
    n_primes: Annotated[int, typer.Option(help="How many prime numbers to calculate")],
) -> None:

    start_time = time.time()
    primes = obfu_primes.calculate_primes(n_primes)
    end_time = time.time()

    print(f"Calculated {n_primes} prime numbers in {end_time - start_time:.2f} seconds")
    print(f"The {_ordinal(n_primes)} prime was {primes[-1]}")


if __name__ == "__main__":
    typer.run(main)
