#Initialize an empty output list
#Initialize an list of nodes to visit and add the root node to it
#While there are nodes in the nodes to visit list
  #Remove the first node from the nodes to visit list
  #Add its value to the output list
  #Add its children (if any) to the end of the nodes to visit list
#Return the output list

class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    pass

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