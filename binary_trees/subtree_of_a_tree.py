from tabnanny import check
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # find root first
        def findRoot(node):
            print(node.val)
            if not node:
                return None

            if node.val == subRoot.val:
                return node

            left = findRoot(node.left)

            if left:
                return left

            right = findRoot(node.right)

            if right:
                return right


        subrootNode = findRoot(root)

        print(subrootNode.val)

        if not subrootNode:
            return False

        def checkSubroot(rootNode, subrootNode):
            if (rootNode and not subrootNode) or (not rootNode and subrootNode):
                return False
            if (not rootNode and not subrootNode) or (
                    rootNode.val == subrootNode.val and checkSubroot(rootNode.left, subrootNode.left) and checkSubroot(rootNode.right, subrootNode.right)):
                return True

            return False

        return checkSubroot(subrootNode, subRoot)


if __name__ == '__main__':
    # Creating the 'Root' tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    # Creating the 'Subroot' tree
    subroot = TreeNode(2)
    subroot.left = TreeNode(4)
    subroot.right = TreeNode(5)

    solution = Solution()
    print(solution.isSubtree(root,subroot))
