class Node:
    def __init__(self, node, name='0'):
        self.parent = node
        self.id = name

def count_tree_depth(node):
    current_node = node
    count = 0
    while current_node.parent != None:
        count += 1
        current_node = current_node.parent

    return count

def skip_n_nodes(node, n):
    current_node = node
    count = n
    while count != 0:
        count -= 1
        current_node = current_node.parent
    
    return current_node

def first_equal_node(node_a, node_b):
    current_node_b = node_b
    current_node_a = node_a
    while current_node_b is not None or current_node_a is not None:
        if current_node_a.id == current_node_b.id:
            return current_node_a
        
        current_node_b = current_node_b.parent
        current_node_a = current_node_a.parent
    
    return None

if __name__ == "__main__":
    node_c = Node(Node(Node(None, '0'), '1'), 'C')
    node_a = Node(Node(Node(node_c, '2'), '3'), 'A')
    node_b = Node(Node(node_c, '4'), 'B')

    node_a_depth = count_tree_depth(node_a)
    node_b_depth = count_tree_depth(node_b)
    print(f'from A depth {node_a_depth}')
    print(f'from B depth {node_b_depth}')

    diff = abs(node_a_depth - node_b_depth)
    print(f'diff {diff}')

    node_a_skipped = skip_n_nodes(node_a, diff)
    print(f'from A skip to {node_a_skipped.id}')

    result = first_equal_node(node_a_skipped, node_b)
    if result is None:
        print('Not found')
    
    print(result.id)