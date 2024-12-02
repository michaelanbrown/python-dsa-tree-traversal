class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    pass


### Breadth First

#Initialize an empty output list
#Initialize an list of nodes to visit and add the root node to it
#While there are nodes in the nodes to visit list
  #Remove the first node from the nodes to visit list
  #Add its value to the output list
  #Add its children (if any) to the end of the nodes to visit list
#Return the output list

  def breadth_first_traversal(node):
    result = []
    nodes_to_visit = [node]

    while len(nodes_to_visit) > 0:

      # 1. Remove the first node from the `nodes_to_visit` list
      node = nodes_to_visit.pop(0)
      # 2. Add its value to the result list
      result.append(node['value'])
      # 3. Add its children (if any) to the END of the `nodes_to_visit` list
      nodes_to_visit = nodes_to_visit + node['children']

    return result


child_1 = {
  'value': 2,
  'children': []
}

child_2 = {
  'value': 3,
  'children': []
}

child_3 = {
  'value': 4,
  'children': []
}

root = {
  'value': 1,
  'children': [child_1, child_2, child_3]
}
print(breadth_first_traversal(root))
# => [1, 2, 3, 4]



###Depth First

#Initialize an empty output list
#Initialize an list of nodes to visit and add the root node to it
#While there are nodes in the list of nodes to visit
  #Remove the first node from the list of nodes to visit
  #Add its value to the output list
  #Add its children (if any) to the BEGINNING of the list of nodes to visit
#Return the output list

def depth_first_traversal(node):
  result = []
  nodes_to_visit = [node]

  while len(nodes_to_visit) > 0:
    # 1. Remove the first node from the `nodes_to_visit` list
    node = nodes_to_visit.pop(0)
    # 2. Add its value to the result list
    result.append(node['value'])
    # 3. Add its children (if any) to the BEGINNING of the `nodes_to_visit` list
    nodes_to_visit = node['children'] + nodes_to_visit

  return result