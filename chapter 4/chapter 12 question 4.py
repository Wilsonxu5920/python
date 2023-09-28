def find_largest(lst):
    if not lst:
        return 0
    current_value = lst[0]
    largest_rest = find_largest(lst[1:])
    if current_value > largest_rest:
        return current_value
    else:
        return largest_rest
input_string = input("Enter a list of numbers: ")
lst = list(map(int, input_string))


print(f"Largest value in the list is: {find_largest(lst)}")