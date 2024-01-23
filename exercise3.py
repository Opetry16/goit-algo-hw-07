class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1  # Додатковий параметр для AVL-дерева

def tree_sum(root):
    # Рекурсивний підхід для знаходження суми значень в BST або AVL-дереві
    if root is None:
        return 0
    return root.key + tree_sum(root.left) + tree_sum(root.right)

# Приклад використання:
# Задаємо структуру BST або AVL-дерева
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.left = TreeNode(12)
root.right.right = TreeNode(18)

# Знаходимо суму значень
total_sum = tree_sum(root)
print("Сума значень в дереві:", total_sum)