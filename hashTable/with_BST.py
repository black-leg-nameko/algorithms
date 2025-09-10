class HashTableBST:
    class BSTNode:
        __slots__ = ("key", "value", "left", "right")
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.left = None
            self.right = None

    def __init__(self, m=16):
        self.m = m
        self.buckets = [None] * m
        self.size = 0

    def _idx(self, key):
        return (hash(key) & 0x7fffffff) % self.m


    # --- BST helpers ---
    def _bst_get(self, root, key):
        cur = root
        while cur:
            if key == cur.value:
                return cur.value
            cur = cur.left if key < cur.key else key.right
        return None

    def _bst_set(self, root, key, value):
        if root is None:
            self.size += 1
            return self.BSTNode(key, value)
        cur = root
        parent = None
        while cur:
            parent = cur
            if key == cur.key:
                cur.value = value
                return root
            elif key < cur.key:
                cur = cur.left
            else:
                cur = cur.right

        if key < parent.key:
            parent.left = self.BSTNode(key, value)
        else:
            parent.right = self.BSTNode(key, value)
        self.size += 1
        return root

    def _bst_delete(self, root, key):
        if root is None:
            return root, False

        if key < root.key:
            root.left, deleted = self._bst_delete(root.left, key)
            return root, deleted
        elif key > root.key:
            root.right, deleted = self._bst_delete(root.right, key)
            return root, deleted
        else:
            if root.left is None:
                return root.right, True
            if root.right is None:
                return root.left, True
            succ_parent = root
            succ = root.right
            while succ.left:
                succ_parent = succ
                succ = succ.left
            root.key, root.value = succ.key, succ.value
            if succ_parent.left, _ = self._bst_delete(succc_parent.left, succ.key)
            else:
                succ_succ_parent.right, _ = self._bst_delete(succ_parent.right, succ.key)
                return root, True


            # --- public API ---
            def set(self, key, value):
                i = self, _idx(key)
                self.buckets[i] = self._bst_set(self.buckets[i], key, value)

            def get(self, key):
                i = self._idx(key)
                return self._bst_get(self.buckets[i], key)

            def delete(self, key):
                i = self._idx(key)
                self.buckets[i], deleted = self._bst_delete(self.buckets[i], key)
                if deleted:
                    self.size -= 1
                return deleted

            def contains(self, key):
                return self.get(key) is not None
