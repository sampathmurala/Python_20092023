class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def insert(node, key: int) -> Node:
    if node is None:
        return Node(key)
    if key < node.key:
        node.left = insert(node.left, key)
    elif key > node.key:
        node.right = insert(node.right, key)
    return node


def inorder(root_node):
    if root_node is not None:
        inorder(root_node.left)
        print(root_node.key, end=" ")
        inorder(root_node.right)


def inorder_traverse(root_node, arr):
    if root_node is not None:
        inorder_traverse(root_node.left, arr)
        arr.append(root_node.key)
        inorder_traverse(root_node.right, arr)


def preorder(root_node):
    if root_node is not None:
        print(root_node.key, end=" ")
        inorder(root_node.left)
        inorder(root_node.right)


def postorder(root_node):
    if root_node is not None:
        inorder(root_node.left)
        inorder(root_node.right)
        print(root_node.key, end=" ")


def height(node) -> int:
    if node is None:
        return 0
    ldepth = height(node.left)  # depth of left subtree
    rdepth = height(node.right)  # depth of right subtree
    return max(ldepth, rdepth) + 1


def find_node(root_node, node_val):
    if node_val is None:
        return Node(node_val)
    if root_node.key == node_val:
        return root_node
    if node_val < root_node.key:
        return find_node(root_node.left, node_val)
    elif node_val > root_node.key:
        return find_node(root_node.right, node_val)


def inorder_successor(root_node, node_val: int):
    successor = None
    given_node = find_node(root_node, node_val)
    while root_node:
        if given_node.key < root_node.key:
            successor = root_node
            root_node = root_node.left
        elif given_node.key > root_node.key:
            root_node = root_node.right
        else:
            if root_node.right:
                successor = root_node.right
                while successor.left:
                    successor = successor.left
            break
    return successor


if __name__ == '__main__':
    root = None
    nodes = [3, 2, 5, 1]
    for v in nodes:
        root = insert(root, v)
    inorder_traversal = []
    inorder_traverse(root, inorder_traversal)
    inorder_successor_node = inorder_successor(root, 2)
    print(f"Inorder Successor of the node {2} is : {inorder_successor_node.key}")

    # print(f"inorder:")
    # inorder(root)
    # print(f"\npreorder:")
    # preorder(root)
    # print(f"\npostorder:")
    # postorder(root)
    # print(f"\nHeight of BST: {height(root)}")

    # Find Inorder Successor of the given node
    # inorder_successor(root, 8)
