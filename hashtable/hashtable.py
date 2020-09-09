from fnvhash import fnv1a_64

class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        if capacity < MIN_CAPACITY:
            self.capacity = MIN_CAPACITY
        else:
            self.capacity = capacity
        self.buckets = [None] * self.capacity


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return len(self.buckets)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return self.size / self.get_num_slots()


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        FNV_offset_basis = 14695981039346656037
        FNV_prime = 1099511628211 
        hashed_results = FNV_offset_basis
        key_bytes = key.encode()

        for byte in key_bytes:
            hashed_results = hashed_results * FNV_prime
            hashed_results= hashed_results ^ byte
        return hashed_results



    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hashed_results = 5381
        key_bytes = key.encode()
        for byte in key_bytes:
            hashed_results = ((hashed_results <<5)+hashed_results) + byte
        return hashed_results


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        #day1
        #idx = self.hash_index(key)
        #self.buckets[idx] = value

        #day2
        idx = self.hash_index(key)
        if (self.buckets[idx] == None):
            self.buckets[idx] = HashTableEntry(key, value)
            self.size += 1
        else:
            cur = self.buckets[idx]
            while cur.next != None and cur.key != key:
                cur = cur.next
            if cur.key == key:
                cur.value = value
            else: 
                new = HashTableEntry(key, value)
                new.next = self.buckets[idx]
                self.buckets[idx] = new
                self.size += 1
        if self.get_load_factor() > .7:
            self.resize(self.capacity * 2)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        #day1
        #idx = self.hash_index(key)
        #self.buckets[idx] = None
        #day2
        idx = self.hash_index(key)
        if self.buckets[idx].key == key:
            if self.buckets[idx].next == None:
                self.buckets[idx] = None
                self.size -= 1
            else:
                new_head = self.buckets[idx].next
                self.buckets[idx].next = None
                self.buckets[idx] = new_head
                self.size -= 1
        else:
            if self.buckets[idx] == None:
                return None
            else:
                cur_val = self.buckets[idx]
                prev_val == None
                while cur_val.next is not None and cur_val.key != key:
                    prev_val = cur_val
                    cur_val = cur_val.next
                if cur_val.key == key:
                    prev_val.next = cur_val.next
                    self.size -= 1
                    return cur_val
                else:
                    return None
            if self.get_load_factor() < .2:
                if self.capacity/2 > MIN_CAPACITY:
                    self.resize(self.capacity/2)
                elif self.capacity > MIN_CAPACITY:
                    self.resize(MIN_CAPACITY)


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        #day1
        #idx = self.hash_index(key)
        #value = self.buckets[idx]
        #return value
        #day2
        idx = self.hash_index(key)
        if self.buckets[idx] is not None and self.buckets[idx].key == key:
            return self.buckets[idx].value
        elif self.buckets[idx] is None:
            return None
        else:
            while self.buckets[idx].next != None and self.buckets[idx].key != key:
                self.buckets[idx] = self.buckets[idx].next
            if self.buckets[idx] == None:
                return None
            else:
                return self.buckets[idx].value


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        #day2
        old = self.buckets[:]
        old_capacity = self.capacity
        self.capacity = new_capacity
        self.buckets = [None] * new_capacity

        for idx in range(0, old_capacity):
            if old[idx] is not None:
                cur_entry = old[idx]
                self.put(cur_entry.key, cur_entry.value)



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
