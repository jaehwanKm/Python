class Node:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        return node.height if node else 0

    def update_height(self, node):
        node.height = 1 + max(self.height(node.left), self.height(node.right))

    def balance_factor(self, node):
        return self.height(node.left) - self.height(node.right)

    def rotate_right(self, y):
        x = y.left
        temp = x.right

        x.right = y
        y.left = temp

        self.update_height(y)
        self.update_height(x)

        return x

    def rotate_left(self, x):
        y = x.right
        temp = y.left

        y.left = x
        x.right = temp

        self.update_height(x)
        self.update_height(y)

        return y

    def rebalance(self, node):
        self.update_height(node)
        balance = self.balance_factor(node)

        if balance > 1:
            if self.balance_factor(node.left) < 0:
                node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        if balance < -1:
            if self.balance_factor(node.right) > 0:
                node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def insert(self, key, value=None):
        self.root = self._insert(self.root, key, value)

    def _insert(self, node, key, value):
        if node is None:
            return Node(key, value)

        if key < node.key:
            node.left = self._insert(node.left, key, value)
        elif key > node.key:
            node.right = self._insert(node.right, key, value)
        else:
            node.value = value
            return node

        return self.rebalance(node)

    def delete(self, key, value=None):
        self.root = self._delete(self.root, key, value)

    def _delete(self, node, key, value):
        if node is None:
            return None

        if key < node.key:
            node.left = self._delete(node.left, key, value)

        elif key > node.key:
            node.right = self._delete(node.right, key, value)

        else:
            if value is not None and node.value != value:
                return node

            if node.left is None:
                return node.right

            if node.right is None:
                return node.left

            successor = self.find_min(node.right)
            node.key = successor.key
            node.value = successor.value
            node.right = self._delete(node.right, successor.key, successor.value)

        return self.rebalance(node) if node else None

    def find_min(self, node):
        while node.left:
            node = node.left
        return node

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.key)
            self._inorder(node.right, result)

    def tree_height(self):
        return self.height(self.root) - 1

    def path_to(self, key):
        path = []
        node = self.root

        while node:
            path.append(node.key)

            if key == node.key:
                return path
            elif key < node.key:
                node = node.left
            else:
                node = node.right

        return path


tree = AVLTree()

data = [35, 18, 7, 26, 12, 3, 68, 22, 30, 99]

for x in data:
    tree.insert(x)

print("삽입 후 중위 순회:", tree.inorder())
print("삽입 후 트리 높이:", tree.tree_height())
print("루트에서 30까지의 경로:", tree.path_to(30))

for x in [3, 68, 18]:
    tree.delete(x)

print("삭제 후 중위 순회:", tree.inorder())
print("삭제 후 트리 높이:", tree.tree_height())
print("루트에서 30까지의 경로:", tree.path_to(30))