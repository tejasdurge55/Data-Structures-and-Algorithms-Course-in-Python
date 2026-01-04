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

#bfs with array as stack
print("--bfs using array--")
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


# bfs with deque 
# to pop out first element in 0(1) complexity 
# as removing 0th index from array takes O(N) complexity
print("--bfs using deque--")
from collections import deque

visited=set()
visited.add('e')
stack_array=deque(['e'])
while stack_array:
    currentVertex=stack_array.popleft()
    print(currentVertex)
    for values in customDict[currentVertex]:
        if values not in stack_array and values not in visited:
            visited.add(values)
            stack_array.append(values)
