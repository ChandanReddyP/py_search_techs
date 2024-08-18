def print_binary(lst,low_ind,high_ind,search_element):

    while low_ind <= high_ind:
        mid = (low_ind + high_ind) // 2

        if lst[mid] < search_element:
            low_ind = mid + 1
        
        elif lst[mid] > search_element:
            high_ind = mid - 1

        elif lst[mid] == search_element:
            return mid

    else:
        return -1

lst=[11,21,32,43,54,62,72,87,90]
search_element = 72
result = print_binary(lst, 0, len(lst) - 1, search_element)
print ("The searching element is in the index of :", result)