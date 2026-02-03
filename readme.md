# Binary Tree Implementation with YAML Integration

A Python package that provides a **Binary Tree data structure**, helper functions to manipulate it, and utilities to **build a tree from a YAML file** or **export a tree to YAML**.

This project is suitable for learning data structures, recursion, file parsing, and basic package organization in Python.

---

## ✨ Features

### Feature Set 1: Binary Tree

* `Node` class for creating a Binary Tree
* Create a new binary tree
* Add nodes to an existing tree using a path (`L`, `R`, `LL`, etc.)
* Delete a node or an entire tree *(optional/extendable)*
* Edit the value of an existing node
* Print:

  * The entire binary tree
  * Specific ranges or subtrees *(extendable)*

### Feature Set 2: YAML Integration

* Build a binary tree from a YAML file
* Export a binary tree into a YAML file

### Bonus Feature

* Easily extendable to a **general (N-ary) tree** with unlimited children per node

---

## 📁 Project Structure

```
binary_tree_package/
│
├── main.py          # Node class and helper functions
├── test_script.py   # Script to test tree functionality
├── test.yaml        # Sample YAML input
├── requirements.txt # Dependencies (optional)
└── README.md        # Project documentation
```

---

## 🧰 Requirements

* Python 3.8 or higher
* PyYAML

Install dependency:

```bash
pip install pyyaml
```

---

## 🚀 How to Run

1. Clone or download the project
2. Navigate to the project directory
3. Install dependencies
4. Run the test script

```bash
python test_script.py
```

---

## 🧪 Test Script Example

```python
from main import *

if __name__ == "__main__":
    root = Node(10)

    add_node_by_path(root, "L", 5)
    add_node_by_path(root, "R", 15)
    add_node_by_path(root, "LL", 3)
    add_node_by_path(root, "LR", 7)
    add_node_by_path(root, "RR", 18)

    print_tree(root)
```

---

## 🗂 YAML File Format

Example `test.yaml`:

```yaml
value: 10
left:
  value: 5
  left:
    value: 3
  right:
    value: 7
right:
  value: 15
  right:
    value: 18
```

---

## 🔁 Build Tree from YAML

```python
yaml_tree_root = build_tree_from_yaml("test.yaml")
print_tree(yaml_tree_root)
```

---

## 🖨 Sample Output

```
Root:10
    L---5
        L---3
        R---7
    R---15
        R---18
```

---

## 🌳 Bonus: General Tree (N-ary Tree)

To convert this project into a general tree:

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
```

Update helper functions to iterate over `children` instead of `left` and `right`.

---

## 🧠 Concepts Used

* Object-Oriented Programming (OOP)
* Recursion
* Tree Traversal
* YAML Parsing
* Python Modules & Imports

---

## 📌 Future Improvements

* Delete node by value or path
* Range-based tree printing
* Tree balancing (BST / AVL)
* Unit tests using `pytest`
* Full pip packaging (`setup.py` / `pyproject.toml`)

---

## 📄 License

This project is intended for educational purposes. You are free to modify and extend it.

---


