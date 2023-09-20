def LCA(root, p, q):
    if root == None:
        return None
    #left방문, right방문, 자기할일하므로 postorder
    left = LCA(root.left,p,q)
    right = LCA(root.right, p, q)
    #얘가먼저여야함
    if root == p and root == q:
        return root
    elif left and right:
        return root
    return left or right