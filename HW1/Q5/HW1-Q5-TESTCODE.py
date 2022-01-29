import random
from q5 import find_median

random.seed()

max_comb_array_size = 2000
max_array_entry = 1e6
min_array_entry = -1e6

def gen_arr_median(arr):
    arr_median = None

    median_pos = int(len(arr) / 2)

    if (len(arr) % 2 == 0):
        arr_median = (arr[median_pos] + arr[median_pos - 1]) / 2.0
    else:
        arr_median = arr[median_pos]

    return arr_median


def gen_large_sorted_arr():
    arr_len = 0

    while (arr_len == 0):
        arr_len = random.randint(0, max_comb_array_size)

    rand_arr = []

    for i in range(0, arr_len):
        rand_arr.append(random.randint(min_array_entry, max_array_entry))

    rand_arr.sort()

    arr_med = gen_arr_median(rand_arr)

    return (rand_arr, arr_med)


def split_array(arr):
    array1 = []
    array2 = []

    for i in range(len(arr)):
        rand_sel = 1 if (random.random() >= 0.5) else 0

        if (rand_sel):
            array2.append(arr[i])
        else:
            array1.append(arr[i])

    return (array1, array2)

# Main body of code
num_of_tests = input("Enter the number of tests you want to run: ")

for i in range(num_of_tests):
    arr_data = gen_large_sorted_arr()
    arr_median = gen_arr_median(arr_data[0])
    split_arrays = split_array(arr_data[0])

    calc_median = find_median(split_arrays[0], split_arrays[1])
    test_passed = "PASS" if (calc_median == arr_median) else "FAIL"

    print("")
    print("Test #" + str(i+1))
    print("Array 1 length: " + str(len(split_arrays[0])))
    print("Array 2 length: " + str(len(split_arrays[1])))
    print("Expected median: " + str(arr_median))
    print("Median found by algorithm: " + str(calc_median))
    print("Result: " + test_passed)
    print("")
    print("----------------------------------------")