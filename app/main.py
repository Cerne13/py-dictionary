class Dictionary:
    def __init__(self):
        self.length = 0
        self.capacity = 8
        self.threshold = int(self.capacity * 2 / 3)
        self.items = [[] for _ in range(self.capacity)]

    def __len__(self):
        return self.length

    def __setitem__(self, key, value):
        hash_ = hash(key)
        index_ = hash_ % self.capacity

        while self.items[index_]:
            if self.items[index_][0] == key and self.items[index_][2] == hash_:
                self.items[index_] = [key, value, hash_]
                self.length -= 1
                break

            index_ = (index_ + 1) % self.capacity

        self.items[index_] = [key, value, hash_]
        self.length += 1

        if self.length == int(self.capacity * (2 / 3)):
            self.resize_hashtable()

    def __getitem__(self, key):
        hash_ = hash(key)
        index_ = hash_ % self.capacity

        while self.items[index_]:
            if self.items[index_][0] == key and self.items[index_][2] == hash_:
                return self.items[index_][1]

            index_ = (index_ + 1) % self.capacity

        raise KeyError('No such item in the dictionary')

    def resize_hashtable(self):
        self.capacity *= 2
        stored_items = self.items

        self.items = [[] for _ in range(self.capacity)]
        self.length = 0

        for item in stored_items:
            if item:
                self.__setitem__(item[0], item[1])
