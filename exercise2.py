class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1  # Додатковий параметр для AVL-дерева

def find_min_value(root):
    # Ітеративний підхід для пошуку мінімального значення в BST або AVL-дереві
    current = root
    while current.left is not None:
        current = current.left
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

# Знаходимо найменше значення
min_value = find_min_value(root)
print("Найменше значення в дереві:", min_value)