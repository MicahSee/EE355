
def find_median(arraynums1, arraynums2):
    array_1_idx = 0
    array_2_idx = 0

    combined_array = []

    while (array_1_idx < len(arraynums1) or array_2_idx < len(arraynums2)):
        if (array_2_idx == len(arraynums2)):
            combined_array.append(arraynums1[array_1_idx])

            array_1_idx += 1
        elif (array_1_idx == len(arraynums1)):
            combined_array.append(arraynums2[array_2_idx])

            array_2_idx += 1
        else:
            if (arraynums1[array_1_idx] < arraynums2[array_2_idx]):
                combined_array.append(arraynums1[array_1_idx])

                array_1_idx += 1
            else:
                combined_array.append(arraynums2[array_2_idx])

                array_2_idx += 1

    comb_len = len(arraynums1) + len(arraynums2)
    median_pos = int((comb_len - 1) / 2)

    median = None

    if (comb_len % 2 == 0):
        median = (combined_array[median_pos] + combined_array[median_pos+1]) / 2.0
    else:
        median = combined_array[median_pos]

    return median