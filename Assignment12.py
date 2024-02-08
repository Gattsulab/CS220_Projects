# Discrete Structures (CSCI 220)
# Winter 2024
# Assignment 12 -  Trees and Tree Algorithms
# Raphael Attiaala
# Collaberated with Class

import copy
import numpy as np
from random import randint, shuffle
import Assignment11 as as11
import Assignment8 as as8
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def __str__(self):
        return "" if self is None else f"{self.key} -> [{self.left} , {self.right}]"


# [1] Declare a variable size and assign it a number, e.g. 100.
# Build a list of numbers between 1 and size, and then shuffle the numbers into a random permutation.
# We will refer to this list as the "keys".
def random_list(n):
    l = ordered_list(n)
    shuffle(l)
    return l


def ordered_list(n):
    l = [i for i in range(n)]
    return l


# [2] Define a function build_tree(keys) that builds a binary search tree by starting with a root node with  key[0]
# and gradually inserts the remaining keys following the BST property (smaller on the left, larger on the right).
# We will use a simple list as a node, in which node[0] is the key, node[1] is the left subtree (LST),
# and node[2] is the right subtree (RST).
def insert(root, key):
    # if root is none initilize the tree
    if root is None:
        return Node(key)
    # if root has item don't do it again
    elif root.key == key:
        return root
    # if key < roo  t put it on left
    elif root.key > key:
        root.left = insert(root.left, key)
    # if key > root put it on right
    else:
        root.right = insert(root.right, key)
    return root


def build_tree(keys):
    tree = Node(keys[0])
    for key in keys[1:]:
        insert(tree, key)
    return tree


# # [3] Implement the following functions
# preorder(tree) - pre-order traversal of the tree
def preorder(tree):
    if tree is None:
        return ""
    else:
        return clean(f"{tree.key} {preorder(tree.left)} {preorder(tree.right)}")


# postorder(tree) - post-order traversal of the tree
# inorder(tree) - in-order traversal of the tree
def inorder(tree):
    if tree is None:
        return ""
    else:
        return clean(f"{inorder(tree.left)} {tree.key} {inorder(tree.right)}")


# postorder(tree) - post-order traversal of the tree
def postorder(tree):
    if tree is None:
        return ""
    else:
        return clean(f"{postorder(tree.left)} {postorder(tree.right)} {tree.key} ")


def height(tree):
    if tree is None:
        return -1
    elif tree.right == None and tree.left == None:
        return 0
    else:
        return 1 + max(height(tree.left), height(tree.right))


def reverse_order(tree):
    if tree is None:
        return ""
    else:
        return clean(f"{reverse_order(tree.right)} {tree.key} {reverse_order(tree.left)}")


def clean(s):
    while s.find("  ") >= 0:
        s = s.replace("  ", " ")
    return s.strip()


def min_key(tree):
    if tree == None:
        return 9999
    elif tree.left == None:
        return tree.key
    else:
        return min_key(tree.left)


def max_key(tree):
    if tree == None:
        return -1
    elif tree.right == None:
        return tree.key
    else:
        return max_key(tree.right)


# [4] Define a function print_tree_properties that prints the name and value of each function listed in [3].
def print_tree_properties(description, tree, properties):
    data = [[prop.__name__, prop(tree)] for prop in properties]
    headers = ["Property Name", "Value"]
    alignments = ["l"] * 2
    as8.print_table(description, headers, data, alignments)


# [5] Define functions
# tree_to_matrix(tree) that maps a tree into an adjacency matrix
# tree_to_tablex(tree) that maps a tree into an adjacency table
# tree_to_edges(tree) that maps a tree into an edge set
def tree_to_matrix(edges, n):
    matrix = [[0] * n for _ in range(n)]
    for edge in edges:
        i, j = edge
        print(i, j, n)
        matrix[i][j] = 1
    return matrix


def tree_to_tablex(tree):
    pass


def tree_to_edges(tree, edges=None):
    if edges is None:
        edges = set()
    if tree is None:
        return edges
    if tree.right:
        edges.add((tree.key, tree.right.key))
        tree_to_edges(tree.right, edges)
    if tree.left:
        edges.add((tree.key, tree.left.key))
        tree_to_edges(tree.left, edges)
    return edges


# [6] Use the function from an earlier assignment to analyze the vertex properties of the obtained graph

# [7] Use the functions from an earlier assignment to analyze the relation properties of the obtained graph


# [8] Define a function draw_tree(tree) that draws the tree using the edge-list and draw_graph() from earlier assignment
def draw_tree(tree):
    pass


# [9] Wrap all the functionality from the previous tasks into a function do_tree(tree)

# [10] Build a Balanced Binary Search Tree using the approach at
# https://www.geeksforgeeks.org/sorted-array-to-balanced-bst/ and then call do_tree(on the bbst)

def do_tree(assn, desc, keys):
    tree = build_tree(keys)
    edges = set()
    edges = tree_to_edges(tree, edges)
    matrix = tree_to_matrix(edges, len(keys))
    properties = [height, min_key, max_key, inorder, reverse_order, preorder, postorder]
    as11.do_graph(assn, desc, matrix, True)
    print_tree_properties("Tree Properties", tree, properties)
    print("Vertices:", len(keys), "Edges:", len(edges))
    print("=" * 80)
    return tree


def main():
    assn = "Assignment12"
    keys = random_list(10)
    do_tree(assn, "Random Tree", keys)

    keys = ordered_list(10)
    do_tree(assn, "Ordered Tree", keys)

    keys = ordered_list(10)[::-1]
    do_tree(assn, "Backward Tree", keys)


if __name__ == '__main__':
    main()
