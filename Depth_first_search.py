
nodes = [
    {"children": ["B", "C", "D"], "id": "A", "value": "A"},
    {"children": ["E", "F"], "id": "B", "value": "B"},
    {"children": [], "id": "C", "value": "C"},
    {"children": ["G", "H"], "id": "D", "value": "D"},
    {"children": [], "id": "E", "value": "E"},
    {"children": ["I", "J"], "id": "F", "value": "F"},
    {"children": ["K"], "id": "G", "value": "G"},
    {"children": [], "id": "H", "value": "H"},
    {"children": [], "id": "I", "value": "I"},
    {"children": [], "id": "J", "value": "J"},
    {"children": [], "id": "K", "value": "K"}
]
array = []

def dps(nodes):
    num = 1
    array.append(nodes[0]["value"])
    while num < len(nodes):
        a = nodes[num]["value"]
        array.append(a)
        for i in nodes[num]["children"]:
            array.append(i)
        num +=1
    print("".join(map(str,array)))
dps(nodes)