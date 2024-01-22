# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
def get_average(values):
    result = 0
    for v in values:
        result += v
    return result / len(values)


print("Average", get_average([5, 6, 7, 8]))

# test changes
