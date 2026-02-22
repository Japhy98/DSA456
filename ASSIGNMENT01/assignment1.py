import random
import time
import sys
import matplotlib.pyplot as plt

# Helps prevent recursion-depth issues (still good to set)
sys.setrecursionlimit(1_000_000)

# ------------------------------------------------------------
# Helper: best / worst / average case list generators
# ------------------------------------------------------------
def make_list(n, case="worst", seed=42):
    """
    case:
      - "best": already sorted ascending
      - "worst": sorted descending
      - "avg": random list
    """
    rng = random.Random(seed + n)
    arr = [rng.randint(0, 10**6) for _ in range(n)]
    if case == "best":
        arr.sort()
    elif case == "worst":
        arr.sort(reverse=True)
    elif case == "avg":
        pass
    else:
        raise ValueError("case must be one of: best, worst, avg")
    return arr


# ------------------------------------------------------------
# Step 1 + Step 2: Sorting algorithms that return T(n) steps
# Counting rule (simple + consistent):
#   - each comparison = 1 step
#   - each assignment = 1 step
#   - each swap (tuple swap) = 3 steps (proxy like your sample)
# ------------------------------------------------------------

def bubble_sort(my_list):
    steps = 0
    n = len(my_list)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            steps += 1  # comparison
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
                steps += 3  # swap assignments
    return steps


def selection_sort(my_list):
    steps = 0
    n = len(my_list)
    for i in range(n - 1):
        min_idx = i
        steps += 1  # assignment (proxy)
        for j in range(i + 1, n):
            steps += 1  # comparison
            if my_list[j] < my_list[min_idx]:
                min_idx = j
                steps += 1  # assignment
        if min_idx != i:
            my_list[i], my_list[min_idx] = my_list[min_idx], my_list[i]
            steps += 3
    return steps


def insertion_sort(my_list):
    """Required version: insertion_sort(my_list)"""
    return insertion_sort_range(my_list, 0, len(my_list) - 1)


def insertion_sort_range(my_list, left, right):
    """Required version: insertion_sort(my_list, left, right)"""
    steps = 0
    for i in range(left + 1, right + 1):
        key = my_list[i]
        steps += 1  # assignment
        j = i - 1
        steps += 1  # assignment

        while j >= left:
            steps += 1  # comparison
            if my_list[j] > key:
                my_list[j + 1] = my_list[j]
                steps += 1  # assignment
                j -= 1
                steps += 1  # assignment
            else:
                break

        my_list[j + 1] = key
        steps += 1  # assignment
    return steps


def quick_sort(my_list):
    """
    Iterative (stack-based) quicksort to avoid recursion depth errors.
    Uses median-of-three pivot to reduce worst-case behavior on sorted inputs.
    Returns step count.
    """
    steps = 0
    n = len(my_list)
    if n <= 1:
        return steps

    def median_of_three(a, i, j, k):
        nonlocal steps
        # 3-ish comparisons (we count them)
        steps += 1
        if a[i] > a[j]:
            i, j = j, i
        steps += 1
        if a[j] > a[k]:
            j, k = k, j
        steps += 1
        if a[i] > a[j]:
            i, j = j, i
        return j  # index of median

    stack = [(0, n - 1)]
    steps += 1  # assignment (proxy)

    while stack:
        low, high = stack.pop()
        steps += 1  # assignment (proxy)

        if low >= high:
            steps += 1  # comparison proxy
            continue

        mid = (low + high) // 2
        pivot_idx = median_of_three(my_list, low, mid, high)
        pivot = my_list[pivot_idx]
        steps += 2  # assignments (pivot_idx, pivot)

        # move pivot to end
        if pivot_idx != high:
            my_list[pivot_idx], my_list[high] = my_list[high], my_list[pivot_idx]
            steps += 3

        # partition
        i = low - 1
        steps += 1
        for j in range(low, high):
            steps += 1  # comparison
            if my_list[j] <= pivot:
                i += 1
                steps += 1
                if i != j:
                    my_list[i], my_list[j] = my_list[j], my_list[i]
                    steps += 3

        # place pivot
        if i + 1 != high:
            my_list[i + 1], my_list[high] = my_list[high], my_list[i + 1]
            steps += 3
        p = i + 1
        steps += 1

        # push smaller side first (keeps stack smaller)
        left_size = p - 1 - low
        right_size = high - (p + 1)
        steps += 2

        if left_size > right_size:
            stack.append((low, p - 1))
            stack.append((p + 1, high))
        else:
            stack.append((p + 1, high))
            stack.append((low, p - 1))
        steps += 2  # appends proxy

    return steps


# ------------------------------------------------------------
# Validation helper
# ------------------------------------------------------------
def is_sorted(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))


# ------------------------------------------------------------
# Step 1: main test (n=100)
# ------------------------------------------------------------
def step1_test():
    print("\nSTEP 1: correctness test on list length 100\n" + "-" * 55)

    base = make_list(100, case="avg")
    algorithms = [
        ("bubble_sort", bubble_sort),
        ("selection_sort", selection_sort),
        ("insertion_sort", insertion_sort),
        ("quick_sort", quick_sort),
        ("insertion_sort_range(10,90)", lambda a: insertion_sort_range(a, 10, 90)),
    ]

    for name, func in algorithms:
        arr = base[:]  # copy
        steps = func(arr)

        if "range" in name:
            ok = is_sorted(arr[:10]) and is_sorted(arr[10:91]) and is_sorted(arr[91:])
        else:
            ok = is_sorted(arr)

        print(f"{name:28s} | steps={steps:12d} | ok={ok}")


# ------------------------------------------------------------
# Step 2: best/worst/avg test for T(n)
# ------------------------------------------------------------
def step2_test(n=100):
    print("\nSTEP 2: T(n) best/worst/avg (n=100)\n" + "-" * 55)

    cases = ["best", "avg", "worst"]
    algorithms = [
        ("bubble_sort", bubble_sort),
        ("selection_sort", selection_sort),
        ("insertion_sort", insertion_sort),
        ("quick_sort", quick_sort),
    ]

    for name, func in algorithms:
        print(f"\n{name}:")
        for c in cases:
            arr = make_list(n, case=c)
            steps = func(arr)
            print(f"  {c:5s} case -> steps = {steps}")


# ------------------------------------------------------------
# Step 3 + Step 4: plotting utilities
# ------------------------------------------------------------
def time_sort(func, arr):
    start = time.perf_counter()
    steps = func(arr)
    end = time.perf_counter()
    return steps, (end - start)


def run_experiments(sizes):
    """
    Runs worst-case tests and returns:
      results_steps[name] = [(n, steps), ...]
      results_time[name]  = [(n, seconds), ...]
    """
    results_steps = {}
    results_time = {}

    algorithms = [
        ("bubble_sort", bubble_sort, 20000),         # O(n^2)
        ("selection_sort", selection_sort, 20000),   # O(n^2)
        ("insertion_sort", insertion_sort, 20000),   # O(n^2)
        ("quick_sort", quick_sort, 2_000_000),       # faster, allow larger
    ]

    for name, func, max_n in algorithms:
        results_steps[name] = []
        results_time[name] = []

        for n in sizes:
            if n > max_n:
                print(f"Skipping {name} for n={n} (too large / would take too long).")
                continue

            arr = make_list(n, case="worst")
            steps, seconds = time_sort(func, arr)

            if not is_sorted(arr):
                raise RuntimeError(f"{name} failed to sort for n={n}")

            results_steps[name].append((n, steps))
            results_time[name].append((n, seconds))
            print(f"{name:14s} n={n:8d} | steps={steps:14d} | time={seconds:.6f}s")

    return results_steps, results_time


def plot_results(results, title, y_label):
    plt.figure()
    for name, points in results.items():
        if not points:
            continue
        xs = [p[0] for p in points]
        ys = [p[1] for p in points]
        plt.plot(xs, ys, marker="o", label=name)

    plt.xscale("log")
    plt.yscale("log")
    plt.title(title)
    plt.xlabel("n (log scale)")
    plt.ylabel(y_label + " (log scale)")
    plt.legend()
    plt.grid(True)
    plt.show()


# ------------------------------------------------------------
# MAIN
# ------------------------------------------------------------
def main():
    # Step 1
    step1_test()

    # Step 2
    step2_test(n=100)

    # Step 3 + 4 sizes (requested list; code will skip sizes that are too big)
    sizes = [10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000, 1000000, 10000000]

    print("\nSTEP 3 & 4: experiments (worst case)\n" + "-" * 55)
    results_steps, results_time = run_experiments(sizes)

    # Step 3 plot: T(n) vs n
    plot_results(
        results_steps,
        title="Step 3: T(n) (operation count) vs n (worst case)",
        y_label="T(n) steps"
    )

    # Step 4 plot: time vs n
    plot_results(
        results_time,
        title="Step 4: Runtime (seconds) vs n (worst case)",
        y_label="Time (seconds)"
    )

    print("\nDONE ✅")


if __name__ == "__main__":
    main()