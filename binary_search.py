#Using while loop

def binary_search(arr, x):
	low = 0
	high = len(arr) - 1
	mid = 0

	while low <= high:

		mid = (high + low) // 2

		if arr[mid] < x:
			low = mid + 1

		elif arr[mid] > x:
			high = mid - 1

		else:
			return mid

	return -1

if __name__=="__main__":   
    arr = [ 2, 3, 4, 10, 40 ]
    x = 4

    # Function call
    result = binary_search(arr, x)

    if result != -1:
        print("Element is present at index", str(result))
    else:
        print("Element is not present in array")

#Using for loop
def binary_search(list_num, first_index, last_index, to_search):
    if last_index >= first_index:
       
        mid_index = (first_index + last_index) // 2
        mid_element = list_num[mid_index]
       
 
        if mid_element == to_search:
            return f"{mid_element} occurs in position {mid_index}"
 
        elif mid_element > to_search:
            new_position = mid_index - 1
            return binary_search(list_num, first_index, new_position, to_search)
 
        elif mid_element < to_search:
            new_position = mid_index + 1
            return binary_search(list_num, new_position, last_index, to_search)
 
    else:
        return " Does not appear in the list"
       
list_container = [ 1, 9, 11, 21, 34, 54, 67, 90 ]
search = 11
first = 0
last= len(list_container) - 1
 
print(binary_search(list_container,first,last,search))