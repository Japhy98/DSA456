class ChainingTable:
    class Record:
        def __init__(self, key, value):
            self.key = key
            self.value = value

    def __init__(self, capacity=32):
        self.cap = capacity
        self.table = [None] * capacity
        self.size = 0

    def insert(self, key, value):
        index = hash(key) % self.cap

        if self.table[index] is None:
            self.table[index] = []

        # Check if key already exists
        for record in self.table[index]:
            if record.key == key:
                return False

        # Insert new record
        self.table[index].append(self.Record(key, value))
        self.size += 1

        # Resize if load factor > 1.0
        if self.size / self.cap > 1.0:
            self._resize()

        return True

    def modify(self, key, value):
        index = hash(key) % self.cap

        if self.table[index] is None:
            return False

        for record in self.table[index]:
            if record.key == key:
                record.value = value
                return True

        return False

    def remove(self, key):
        index = hash(key) % self.cap

        if self.table[index] is None:
            return False

        bucket = self.table[index]

        for i in range(len(bucket)):
            if bucket[i].key == key:
                bucket.pop(i)
                self.size -= 1
                return True

        return False

    def search(self, key):
        index = hash(key) % self.cap

        if self.table[index] is None:
            return None

        for record in self.table[index]:
            if record.key == key:
                return record.value

        return None

    def capacity(self):
        return self.cap

    def __len__(self):
        return self.size

    def _resize(self):
        old_table = self.table
        self.cap *= 2
        self.table = [None] * self.cap
        self.size = 0

        for bucket in old_table:
            if bucket is not None:
                for record in bucket:
                    self.insert(record.key, record.value)