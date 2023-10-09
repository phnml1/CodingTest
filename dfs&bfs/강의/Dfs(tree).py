#root만 주면 root가 가리키는 tree에 속한 모든노드를 접근하자
def dfs(cur_node):
    if cur_node is None:
        return
    dfs(cur_node.left)
    dfs(cur_node.right)

dfs(root)

#preorder

def preorder(cur_node):
    if cur_node is None:
        return
    print(cur_node)
    preorder(cur_node.left)
    preorder(cur_node.right)

#inorder
def inorder(cur_node):
    if cur_node is None:
        return
    inorder(cur_node.left)
    print(cur_node)
    inorder(cur_node.right)

def postorder(cur_node):
    if cur_node is None:
        return
    postorder(cur_node.left)
    postorder(cur_node.right)
    print(cur_node)
    