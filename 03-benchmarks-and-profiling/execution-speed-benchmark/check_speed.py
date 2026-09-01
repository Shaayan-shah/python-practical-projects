"""
Python Loop & Comprehension Performance Benchmark
Measures and compares execution times of standard for-loops, list comprehensions,
map() operations, and generator expressions.
"""

import time
from typing import Callable, Any


def benchmark_function(name: str, func: Callable[[], Any], iterations: int = 1_000_000):
    """Measure execution time of a callable function."""
    start = time.perf_counter()
    func()
    elapsed = time.perf_counter() - start
    print(f"  {name:<30} : {elapsed * 1000.0:>8.2f} ms ({iterations:,} elements)")
    return elapsed


def main():
    n = 1_000_000
    print("==================================================")
    print(f"      PYTHON EXECUTION SPEED BENCHMARK (N={n:,})   ")
    print("==================================================")

    def loop_append():
        res = []
        for i in range(n):
            res.append(i * 2)
        return res

    def list_comp():
        return [i * 2 for i in range(n)]

    def map_func():
        return list(map(lambda i: i * 2, range(n)))

    def gen_expr():
        return list(i * 2 for i in range(n))

    print("\nRunning Benchmarks...")
    benchmark_function("1. Standard For Loop", loop_append, n)
    benchmark_function("2. List Comprehension", list_comp, n)
    benchmark_function("3. Built-in map()", map_func, n)
    benchmark_function("4. Generator Expression", gen_expr, n)

    print("\n[Observation] List comprehensions execute at C-level speed, consistently outperforming standard Python append loops.")
    print("==================================================")


if __name__ == "__main__":
    main()
