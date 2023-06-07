import time

def bubble_sort_fast(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def bubble_sort_slow(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Data yang sama untuk keduanya
data = [64, 34, 25, 12, 22, 11, 90]

# Bubble Sort versi cepat
start_time = time.perf_counter()
sorted_data_fast = bubble_sort_fast(data)
end_time = time.perf_counter()
execution_time_fast = end_time - start_time
print("Hasil Bubble Sort (Versi Cepat):", sorted_data_fast)
print("Waktu eksekusi (Versi Cepat):", execution_time_fast)

# Bubble Sort versi lambat
start_time = time.perf_counter()
sorted_data_slow = bubble_sort_slow(data)
end_time = time.perf_counter()
execution_time_slow = end_time - start_time
print("Hasil Bubble Sort (Versi Lambat):", sorted_data_slow)
print("Waktu eksekusi (Versi Lambat):", execution_time_slow)