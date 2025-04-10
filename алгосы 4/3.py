def data_base(n, k, priority, permutations):
    priority = [p - 1 for p in priority]
    
    def sort_key(record):
        return tuple(record[i] for i in priority)
    
    sort_permutations= sorted(permutations, key=sort_key)

    sorted_names = [record[0] for record in sort_permutations]
    
    return sorted_names

result = data_base(3, 3, [2, 1, 3], [('a', 1, 2, 3), ('b', 2, 1, 3), ('c', 3, 1, 2)])
print(result) 