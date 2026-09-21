class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        ans = []
        q = deque()
        q.append(root)
        while q:
            n = len(q)
            level = []
            for i in range(n):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    if node.left: q.append(node.left)
                    if node.right: q.append(node.right)
            if level: ans.append(level)
        return ans