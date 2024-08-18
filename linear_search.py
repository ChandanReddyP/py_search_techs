def linear_search(lst,search_ele):

    for ind in range(len(lst)):
        if lst[ind]==search_ele:
            return ind
    return -1


lst=[12,32,-24,34,11,56]
search_ele=22  

result=linear_search(lst,search_ele)
print(result)