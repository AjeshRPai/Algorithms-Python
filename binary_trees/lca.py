class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        current = root

        while current:
            if p.val < current.val and q.val < current.val:
                current = current.left
            elif p.val > current.val and q.val > current.val:
                current = current.right
            else:
                return current


if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(1)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(4)
    root.right.left.left = TreeNode(5)
    diameter = TreeNode(root)
    solution = Solution()
    lca = solution.lowestCommonAncestor(root, p = TreeNode(3), q= TreeNode(5))
    print(lca.val)