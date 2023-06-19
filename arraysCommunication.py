import datetime
import math
import time


def manipulate_arrays():
    # VAR DECLARATION
    counter = 0
    log_counter = 10

    time_storage_for_reversion = []  # helps with reversing the millisecond function

    # information_list contains information that will be used in the succession
    # using numbers from the Fibonacci sequence for fun
    information_list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]

    print(f'\nHere is the contents of Array 1: \n{information_list}\n')

    # operation_list contains the operations that will be done to the value of information_list
    operation_list = []

    for i in range(len(information_list)):
        counter += 1
        now = datetime.datetime.now()
        operation_list.append(information_list[i] - counter**2 + int(now.strftime("%f")))
        time_storage_for_reversion.append(now.strftime("%f"))

    print(f'\nArray 2 manipulates the contents from array by subtracting an incrementing counter and then '
          f'adding the current milliseconds and here is the output:')
    print(operation_list)

    # final_manipulation_list performs operations that unite the contents of information_list and operation_list and then manipulate it even further
    final_manipulation_list = []

    for i in range(len(information_list)):
        log_counter = int(str(log_counter) + '0')
        final_manipulation_list.append((operation_list[i] - information_list[i]) * math.log(log_counter))

    print(f'\nArray 3 manipulates the contents from 1 and 2 by unionizing them and then adding a log_counter '
          f'to it and here is the output:')
    print(final_manipulation_list)

    # ----------------------------------------------------------------------------------------------------------- #
    time.sleep(2)

    # Next, we will revert the terms of list 3 back into its original elements
    print('\n\nNow we will revert the list!\n\n')

    reversion_list = []

    log_counter = 10
    counter = 0

    for i in range(len(information_list)):
        counter += 1
        log_counter = int(str(log_counter) + '0')
        reversion_list.append(int((final_manipulation_list[i]) / math.log(log_counter) + information_list[i]
                                  - int(time_storage_for_reversion[i]) + counter**2))

    time.sleep(2)
    print(f'\nReverted Array uncovers everything in Array 3 back to 1 by using the contents of ARRAY 1 2 and 3 ---> here it is:')
    print(reversion_list)
    print("\nHere is the time Storage for Reversion:")
    print(time_storage_for_reversion)
    print("\n")


if __name__ == '__main__':
    manipulate_arrays()

