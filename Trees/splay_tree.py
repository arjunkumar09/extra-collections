from bst import TreeNode, BST

class SplayTree(BST):
    def zig_zig(self, start_node, left_children=True):
        child = start_node
        parent = child.parent
        grand_parent = parent.parent
        # start zig-zig
        if left_children:
            print("Left zig-zig")
            child.parent = grand_parent.parent
            grand_parent.set_left(parent.right)
            parent.set_right(grand_parent)
            parent.set_left(child.right)
            child.set_right(parent)
        else:
            print("Right zig-zig")
            child.parent = grand_parent.parent
            grand_parent.set_right(parent.left)
            parent.set_left(grand_parent)
            parent.set_right(child.left)
            child.set_left(parent)
        #child is now the grand-parent
        return child

    def zig_zag(self, start_node, left_right_children=True):
        child = start_node
        parent = child.parent
        grand_parent = parent.parent
        # start zig-zag
        if left_right_children:
            print("Left-Right zig-zag")
            child.parent = grand_parent.parent
            grand_parent.set_left(child.right)
            parent.set_right(child.left)
            child.set_right(grand_parent)
            child.set_left(parent)
            pass
        else:
            print("Right-Left zig-zag")
            child.parent = grand_parent.parent
            grand_parent.set_right(child.left)
            parent.set_left(child.right)
            child.set_left(grand_parent)
            child.set_right(parent)
        return child

    def zig(self, start_node, left_child=True):
        child = start_node
        parent = child.parent
        if left_child:
            print("Left zig")
            child.parent = parent.parent
            parent.set_left(child.right)
            child.set_right(parent)
        else:
            print("Right zig")
            child.parent = parent.parent
            parent.set_right(child.left)
            child.set_left(parent)
        return child






if __name__ == "__main__":
    # test Left zig-zig
    stree = SplayTree(30)
    stree.insert(20)
    stree.insert(10)
    print(stree)
    stree.root = stree.zig_zig(stree.root.left.left, left_children=True)
    print(stree)
    print('='*50)

    # test Right zig-zig
    stree = SplayTree(10)
    stree.insert(20)
    stree.insert(30)
    print(stree)
    stree.root = stree.zig_zig(stree.root.right.right, left_children=False)
    print(stree)
    print('='*50)

    # test Right-left zig-zig
    stree = SplayTree(10)
    stree.insert(30)
    stree.insert(20)
    print(stree)
    stree.root = stree.zig_zag(stree.root.right.left, left_right_children=False)
    print(stree)
    print('='*50)

    # test Left-right zig-zig
    stree = SplayTree(30)
    stree.insert(10)
    stree.insert(20)
    print(stree)
    stree.root = stree.zig_zag(stree.root.left.right, left_right_children=True)
    print(stree)
    print('='*50)

    # test right zig
    stree = SplayTree(10)
    stree.insert(20)
    print(stree)
    stree.root = stree.zig(stree.root.right, left_child=False)
    print(stree)
    print('='*50)

    # test left zig
    stree = SplayTree(20)
    stree.insert(10)
    print(stree)
    stree.root = stree.zig(stree.root.left, left_child=True)
    print(stree)
    print('='*50)