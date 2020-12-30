# **Tree and Graphs**

**Validate Binary Search Tree**

    Set constraints(low, high) to every node that 
    a valid node should satisfying low <= node.val <= high 
    node.left update high (child must be smaller than parent)
    node.right update low (child must be larger than parent)
    
    Recursive: 
        low, high = -math.inf, math.inf
        Base Case: 
            not root -> True
        Recurse: 
            check constrains low <= node.val <= high 
            isValid(root.left, low, node.val) and isValid(root.right, node.val, high)
                 
    Iterative: BFS/DFS + Tuple 

**Symmetric Tree**
    
    check mirror need two root that 
    one root is left and one root is right
    left.val == right.val
    
    Recursive:
        Base Case:
            not root : True
            not left and not right : Ture
            not left or not right : False
        Recurse: 
            left.val == right.val
            left.left == left.right and left.right == right.left
    
    Iterative: BFS/DFS
    
**Binary Tree Maximum Path Sum**

    def maxPathSum(self, root: TreeNode) -> int:
        def maxPath(root):
            nonlocal maxSum
            if not root:
                return 0
            
            left = maxPath(root.left)
            right = maxPath(root.right)
            maxSum = max(maxSum, left + right + root.val)
            return max(left + root.val, right + root.val, 0)
        
        maxSum = -math.inf  
        maxPath(root)
        return maxSum
        
        
**Diameter of Binary Tree**

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def height(root):
            nonlocal diameter
            if not root:
                return 0
            
            left = height(root.left)
            right = height(root.right)
            diameter = max(diameter, left + right)
            return max(left, right) + 1
        
        diameter = 0
        height(root)
        return diameter  
