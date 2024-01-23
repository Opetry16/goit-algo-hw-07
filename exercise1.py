class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1 

def find_max_value(root):
    # Ітеративний підхід для пошуку максимального значення в BST або AVL-дереві
    current = root
    while current.right is not None:
        current = current.right
    return current.key

# Приклад використання:
# Задаємо структуру BST або AVL-дерева
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.left = TreeNode(12)
root.right.right = TreeNode(18)

# Знаходимо найбільше значення
max_value = find_max_value(root)
print("Найбільше значення в дереві:", max_value)