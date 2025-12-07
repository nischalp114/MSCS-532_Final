import time
import gc
import random
from typing import Optional, Tuple, List

import numpy as np

# Type alias for a simple singly linked list node:
# Node is a tuple: (value: float, next: Optional[Node])
Node = Optional[Tuple[float, "Node"]]


def build_linked_list(n: int) -> Node:
    """Build a singly linked list of n random floats."""
    head: Node = None
    for _ in range(n):
        head = (random.random(), head)
    return head


def sum_linked_list(head: Node) -> float:
    """Traverse the linked list and compute the sum of all values."""
    total = 0.0
    node = head
    while node is not None:
        value, node = node  # unpack (value, next)
        total += value
    return total


def build_pylist(n: int) -> List[float]:
    """Build a Python list (dynamic array) of n random floats."""
    return [random.random() for _ in range(n)]


def sum_pylist(values: List[float]) -> float:
    """Sum elements in a Python list."""
    total = 0.0
    for v in values:
        total += v
    return total


def build_np_array(n: int) -> np.ndarray:
    """Build a NumPy array of n random floats."""
    return np.random.random(size=n)


def sum_np_array(values: np.ndarray) -> float:
    """Sum elements using NumPy's optimized reduction."""
    return float(values.sum())


def bench(fn, builder, n: int, repeats: int = 5):
    """Benchmark fn(builder(n)) for a fixed n, returning list of runtimes."""
    times = []
    for _ in range(repeats):
        data = builder(n)
        gc.collect()
        t0 = time.perf_counter()
        fn(data)
        t1 = time.perf_counter()
        times.append(t1 - t0)
    return times


def main():
    N = 2_000_000  # two million elements
    repeats = 5

    configs = [
        ("Linked list", sum_linked_list, build_linked_list),
        ("Python list", sum_pylist, build_pylist),
        ("NumPy array", sum_np_array, build_np_array),
    ]

    print(f"Benchmarking with N = {N:,} elements, {repeats} repeats\n")

    for name, fn, builder in configs:
        times = bench(fn, builder, N, repeats)
        avg = sum(times) / len(times)
        print(f"{name:12s} times: {times}")
        print(f"{name:12s} average: {avg:.6f} seconds\n")


if __name__ == "__main__":
    main()
