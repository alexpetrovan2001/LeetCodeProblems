class LRUCache:
    # Average sol -> 57% time and 54% memory
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.map = {}
        self.deque = []

    def get(self, key: int) -> int:
        if key in self.map:
            self.deque.append(key)
            self.map[key][1] += 1
            return self.map[key][0]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.deque.append(key)
            self.map[key][0] = value
            self.map[key][1] += 1
        else:
            while self.length == self.capacity:
                key_to_check = self.deque.pop(0)
                if self.map[key_to_check][1] == 1:
                    del self.map[key_to_check]
                    self.length -= 1
                else:
                    self.map[key_to_check][1] -= 1
            self.deque.append(key)
            self.map[key] = [value, 1]
            self.length += 1


class DLL:
    def __init__(self, prev=None, next=None, key=None, val=None):
        self.prev = prev
        self.next = next
        self.val = val
        self.key = key


class LRUCache2:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.nodes_map = {}
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        if key in self.nodes_map:
            node = self.nodes_map[key]
            self.add_to_dll(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.nodes_map:
            node = self.nodes_map[key]
            node.val = value
            self.add_to_dll(node)
        else:
            node = DLL(None, None, key, value)
            self.add_to_dll(node)

    def remove_from_dll(self, node):
        prev_node = node.prev
        next_node = node.next
        if not prev_node and not next_node:
            self.head = None
            self.tail = None
        elif prev_node and next_node:
            prev_node.next = next_node
            next_node.prev = prev_node
            node.next = None
            node.prev = None
        elif not prev_node and next_node:  # Node == Head
            self.head = self.head.next
            if self.head:
                self.head.prev = None
        else:  # Node == Tail =>
            self.tail = self.tail.prev
            if self.tail:
                self.tail.prev = None
        del self.nodes_map[node.key]
        self.length -= 1

    def add_to_dll(self, node):
        if node.key in self.nodes_map:
            self.remove_from_dll(node)
        if self.length == self.capacity:
            self.remove_from_dll(self.head)
        if self.tail:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        else:  # First element to add to the list -> head and tail not initialized
            self.tail = node
            self.head = node
        self.nodes_map[node.key] = node
        self.length += 1


lRUCache = LRUCache2(10)
ops = [[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]
dict = {}
for op in ops:
    if len(op) == 1:
        key = op[0]
        lru_val = lRUCache.get(key)
        if key not in dict:
            dict_val = -1
        else:
            dict_val = dict[key]
        if dict_val != lru_val:
            raise ValueError(f"problem at key {op[0]} - lru val - {lru_val}; dict_val - {dict_val}")
    else:
        key = op[0]
        val = op[1]
        dict[key] = val
        lRUCache.put(key, val)