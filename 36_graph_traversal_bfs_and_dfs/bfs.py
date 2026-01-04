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


# set initialization and basic array and dictionary use cases
"""
set_a=set()
value=customDict.get('a')
visited=[customDict['a']]
print(value)
print(visited)
"""

#bfs
visited=set()
visited.add('e')
stack_array=['e']
while stack_array:
    currentVertex=stack_array.pop(0)
    print(currentVertex)
    for values in customDict[currentVertex]:
        if values not in stack_array and values not in visited:
            visited.add(values)
            stack_array.append(values)
