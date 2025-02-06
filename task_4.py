import uuid
import heapq
import networkx as nx
import matplotlib.pyplot as plt


class Node:
  def __init__(self, key, color="skyblue"):
    self.left = None
    self.right = None
    self.val = key
    self.color = color # Optional argument to store node color
    self.id = str(uuid.uuid4()) # Unique identifier for each node


def add_edges(graph, node: Node, pos, x=0, y=0, layer=1):
  if node is not None:
    graph.add_node(node.id, color=node.color, label=node.val) # Use id and save node value
    if node.left:
      graph.add_edge(node.id, node.left.id)
      l = x - 1 / 2 ** layer
      pos[node.left.id] = (l, y - 1)
      l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
    if node.right:
      graph.add_edge(node.id, node.right.id)
      r = x + 1 / 2 ** layer
      pos[node.right.id] = (r, y - 1)
      r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
  return graph


def draw_tree(tree_root):
  tree = nx.DiGraph()
  pos = {tree_root.id: (0, 0)}
  tree = add_edges(tree, tree_root, pos)

  colors = [node[1]['color'] for node in tree.nodes(data=True)]
  labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)} # Use node values for labels

  plt.figure(figsize=(8, 5))
  nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
  plt.show()


def build_heap_tree(heap, index=0):
  # If it's the first value create root from it and change value to the Node in the heap list
  if index == 0:
    root = Node(heap[index])
    heap[index] = root

  # If index of the left value exist, create node from it, change in the heap list and add as left child of the parent
  if index * 2 + 1 <= len(heap) - 1:
    left_child = Node(heap[index * 2 + 1])
    heap[index * 2 + 1] = left_child
    heap[index].left = left_child
  else:
    return
  
  # If index of the right value exist, create node from it, change in the heap list and add as right child of the parent
  if index * 2 + 2 <= len(heap) - 1:
    right_child = Node(heap[index * 2 + 2])
    heap[index * 2 + 2] = right_child
    heap[index].right = right_child
  else:
    return

  index += 1
  build_heap_tree(heap, index)

  return heap[0]


if __name__ == '__main__':
  heap_list = [15, 1, 3, 5, 7, 9, 2, 4, 8, 10, 11, 14]

  heapq.heapify(heap_list)

  # Build tree from the heap
  heap_tree_root = build_heap_tree(heap_list)

  # Visualise tree of the binary heap 
  draw_tree(heap_tree_root)