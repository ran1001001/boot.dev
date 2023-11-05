class HashMap:
    def key_to_index(self, key):
        sum = 0
        hash_len = len(self.hashmap)
        for char in key:
            sum += ord(char)
        return sum % hash_len

    def __init__(self, size):
        self.hashmap = [None for i in range(size)]

    def __repr__(self):
        buckets = []
        for v in self.hashmap:
            if v is not None:
                buckets.append(v)
        return str(buckets)


def test(size, keys):
    hm = HashMap(size)
    print(f"Using hashmap with size: {size}")
    for key in keys:
        index = hm.key_to_index(key)
        print(f"{key} hashes to index {index}")
    print("=====================================")


def main():
    test(4, ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"])
    test(256, ["hello", "world"])
    test(512, ["golang", "python", "java", "javascript", "rust", "c", "c++"])


main()
