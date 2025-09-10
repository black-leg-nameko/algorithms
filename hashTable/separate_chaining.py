class HashTableChaining:
    class Node:
        __slots__ = ("key", "value", "next")
        def __init__(self, key, value, nxt=None):
            self.key = key
            self.value = value
            self.next = nxt


        def __init__(self, m=16):
            self.m = m
            self.buckets = [None] * m
            self.size = 0


        def _idx(self, key):
            return (hash(key) & 0x7fffffff) % self.m


        def set(self, key, value):
            i = self._idx(key)
            node = self.buckets[i]
            while node:
                if node.key == key:
                    node.value = value
                    return
                node = node.next

            self.bucckets[i] = self.Node(key, value, self.buckets[i])
            self.size += 1

        def get(self, key):
            i = self._idx(key)
            node = self.buckets[i]
            while node:
                if node.key == key:
                    return node.value
                node = node.next
            return None


        def delete(self, key):
            i = self._idx(key)
            prev = None
            node = self.buckets[i]
            while node:
                if node.key == key:
                    if prev:
                        prev.next = node.next
                    else:
                        self.buckets[i] = node.next
                    self.size -= 1
                    return True
                prev, node = node, node.next
            return False

        def contains(self, key):
            return self.get(key) is not None
