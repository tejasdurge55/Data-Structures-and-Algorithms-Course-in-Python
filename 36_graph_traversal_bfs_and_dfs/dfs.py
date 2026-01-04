# traverse this graph from A

# graph diagram

# A-B
# |   \
# |     E
# |   /
# C-D 

customDict={
    "a" : ["b","c"],
    "b" : ["a", "e"],
    "c" : ["a","d"],
    "d" : ["c","e"],
    "e" : ["b","d"],
}

#dfs with array as stack
print("--dfs using array--")
visited=set()
stack_array=['e']
while stack_array:  #O(V)
    currentVertex=stack_array.pop()
    if currentVertex not in visited:
        visited.add(currentVertex)
        print(currentVertex)
    for values in customDict[currentVertex]: #O(E)
        if values not in visited:
            stack_array.append(values)


# time complexity is O(V+E), rest all operations have O(1) time complexity like, inserting, poping,etc.

