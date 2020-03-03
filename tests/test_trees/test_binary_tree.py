import pytest
from tests import *
from extra.trees.binary_tree import BinaryTreeNode, BinaryTree




def test_binary_treenode():
    with pytest.raises(ValueError):
        BinaryTreeNode(None)
        BinaryTreeNode('  ')
        BinaryTree(BinaryTree(get_value()))
    # the following shouldn't raise anything
    BinaryTreeNode(get_int())
    BinaryTreeNode(get_float())
    BinaryTreeNode(get_string())
    BinaryTreeNode(get_value())
    BinaryTreeNode(get_list())


def test_binary_tree():
    # create tree using BinaryTreeNode
    root = BinaryTreeNode("GrandFather")
    root.set_left(BinaryTreeNode("Father"))
    root.get_left().set_left(BinaryTreeNode("Me"))
    root.get_left().set_right(BinaryTreeNode("Sibling"))
    root.set_right(BinaryTreeNode("Uncle"))
    root.get_right().set_left(BinaryTreeNode("Cousin"))
    root.get_right().set_right(BinaryTreeNode("Cousin"))
    btree = BinaryTree(root)
    #test tree structure
    assert btree.root.get_data() == "GrandFather"
    assert btree.root.get_left().get_data() == "Father"
    assert btree.root.get_left().get_left().get_data() == "Me"
    assert btree.root.get_left().get_right().get_data() == "Sibling"
    assert btree.root.get_left().get_left().get_left() is None
    assert btree.root.get_left().get_left().get_right() is None
    assert btree.root.get_left().get_right().get_left() is None
    assert btree.root.get_left().get_right().get_right() is None
    assert btree.root.get_right().get_data() == "Uncle"
    assert btree.root.get_right().get_left().get_data() == "Cousin"
    assert btree.root.get_right().get_right().get_data() == "Cousin"
    assert btree.root.get_right().get_left().get_left() is None
    assert btree.root.get_right().get_left().get_right() is None
    assert btree.root.get_right().get_right().get_left() is None
    assert btree.root.get_right().get_right().get_right() is None
    # test various functions
    assert btree.get_depth() == btree.get_height() == 2
    assert btree.is_balanced()
    assert btree.is_perfect()
    assert btree.is_strict()
    assert len(btree) == 7
    assert btree.count_leaf_nodes() == 4
    assert [item.get_data() for item in btree] == btree.to_list() == \
        ["GrandFather", "Father", "Uncle", "Me", "Sibling", "Cousin", "Cousin"]
    assert btree.preorder_traverse() == btree.depth_first_traverse() == \
        ["GrandFather", "Father", "Me", "Sibling", "Uncle", "Cousin", "Cousin"]
    assert btree.postorder_traverse() == \
        ["Me", "Sibling", "Father", "Cousin", "Cousin", "Uncle", "GrandFather"]
    assert btree.inorder_traverse() == \
        ["Me", "Father", "Sibling", "GrandFather", "Cousin", "Uncle", "Cousin"]
    assert btree.breadth_first_traverse() == \
        ["GrandFather", "Father", "Uncle", "Me", "Sibling", "Cousin", "Cousin"]
    with pytest.raises(ValueError):
        BinaryTree(None)
        BinaryTree("    ")
        btree.traverse(get_string())
        btree.traverse(get_list())
        btree.traverse(get_value())
        btree.traverse(get_float())


def test_binary_tree_with_numbers():
    btree = BinaryTree(1)
    btree.root.set_left(BinaryTreeNode(2))
    btree.root.set_right(BinaryTreeNode(3))
    btree.root.get_right().set_left(BinaryTreeNode(6))
    btree.root.get_right().set_right(BinaryTreeNode(7))
    btree.root.get_left().set_left(BinaryTreeNode(4))
    btree.root.get_left().set_right(BinaryTreeNode(5))
    assert len(btree) == 7
    assert btree.get_height() == 2
    assert btree.root.get_left().get_data() == 2
    assert btree._get_depth(btree.root.left) == 1
    assert btree.to_list() == [1, 2, 3, 4, 5, 6, 7]
    assert btree.count_leaf_nodes() == 4
    assert btree.is_balanced()
    assert btree.is_perfect()
    assert btree.is_strict()
    assert btree.preorder_traverse() == [1, 2, 4, 5, 3, 6, 7]
    assert btree.postorder_traverse() == [4, 5, 2, 6, 7, 3, 1]
    assert btree.inorder_traverse() == [4, 2, 5, 1, 6, 3, 7]
    assert btree.breadth_first_traverse() == [1, 2, 3, 4, 5, 6, 7]
    assert btree.traverse() == [4, 2, 5, 1, 6, 3, 7]


def test_parse():
    pass

