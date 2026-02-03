import yaml

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def create_tree(value):
    return Node(value)

def add_node_by_path(root, path, value):
    current = root
    for direction in path[:-1]:
        if direction == "L":
            if not current.left:
                current.left = Node(None)
            current = current.left
        elif direction == "R":
            if not current.right:
                current.right = Node(None)
            current = current.right
    if path[-1] == "L":
        current.left = Node(value)
    elif path[-1] == "R":
        current.right = Node(value)

def edit_node_by_path(root, path, new_value):
    current = root
    for direction in path:
        if not current:
            return
        current = current.left if direction == "L" else current.right
    if current:
        current.value = new_value

def delete_tree(root):
    return None


def delete_node_by_path(root, path):
    current = root
    for direction in path[:-1]:
        current = current.left if direction == "L" else current.right
        if not current:
            return

    if path[-1] == "L":
        current.left = None
    else:
        current.right = None

def print_tree(root, level=0, prefix="Root:"):
    if not root:
        print(prefix + "None")
        return

    print(" " * (level * 4) + prefix + str(root.value))
    if root.left or root.right:
        print_tree(root.left, level + 1, "L---")
        print_tree(root.right, level + 1, "R---")




def build_tree_from_yaml(yaml_file):
    with open(yaml_file, "r") as f:
        data = yaml.safe_load(f)

    def build_node(node_dict):
        if not node_dict:
            return None

        node = Node(node_dict.get("value"))
        node.left = build_node(node_dict.get("left"))
        node.right = build_node(node_dict.get("right"))
        return node

    return build_node(data)


def write_tree_to_yaml(root, yaml_file):
    def node_to_dict(node):
        if not node:
            return None

        return {
            "value": node.value,
            "left": node_to_dict(node.left),
            "right": node_to_dict(node.right),
        }

    with open(yaml_file, "w") as f:
        yaml.dump(node_to_dict(root), f)
