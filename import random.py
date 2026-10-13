import random


def generate_array(length, min_val, max_val):
    return [random.randint(min_val, max_val) for _ in range(length)]


def print_array(arr):
    formatted_elements = [f"[cell - {i},value - {val}]" for i, val in enumerate(arr)]
    print("{" + ",".join(formatted_elements) + "}")


def bubble_sort(arr, ascending=True):
    a = arr.copy()
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if ascending:
                if a[j] > a[j + 1]:
                    a[j], a[j + 1] = a[j + 1], a[j]
            else:
                if a[j] < a[j + 1]:
                    a[j], a[j + 1] = a[j + 1], a[j]
    return a


def insertion_sort(arr, ascending=True):
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        if ascending:
            while j >= 0 and a[j] > key:
                a[j + 1] = a[j]
                j -= 1
        else:
            while j >= 0 and a[j] < key:
                a[j + 1] = a[j]
                j -= 1
        a[j + 1] = key
    return a


def selection_sort(arr, ascending=True):
    a = arr.copy()
    n = len(a)
    for i in range(n):
        target_idx = i
        for j in range(i + 1, n):
            if ascending:
                if a[j] < a[target_idx]:
                    target_idx = j
            else:
                if a[j] > a[target_idx]:
                    target_idx = j
        a[i], a[target_idx] = a[target_idx], a[i]
    return a


if __name__ == "__main__":
    original_arr = generate_array(length=8, min_val=1, max_val=20)
    
    print("=== ІСНУЮЧИЙ МАСИВ ===")
    print_array(original_arr)
    print("\n" + "="*50 + "\n")

    print("--- 1. BUBBLE SORT ---")
    print("Прямий порядок (ascending=True):")
    print_array(bubble_sort(original_arr, True))
    
    print("Зворотний порядок (ascending=False):")
    print_array(bubble_sort(original_arr, False))
    print()

    print("--- 2. INSERTION SORT ---")
    print("Прямий порядок (ascending=True):")
    print_array(insertion_sort(original_arr, True))
    
    print("Зворотний порядок (ascending=False):")
    print_array(insertion_sort(original_arr, False))
    print()

    print("--- 3. SELECTION SORT ---")
    print("Прямий порядок (ascending=True):")
    print_array(selection_sort(original_arr, True))
    
    print("Зворотний порядок (ascending=False):")
    print_array(selection_sort(original_arr, False))