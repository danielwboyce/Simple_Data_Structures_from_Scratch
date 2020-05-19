# This hash map uses separate chaining and linked lists to resolve collisions
from node import NodeSinglyLinked
from singly_linked_list import SinglyLinkedList

class HashMapSeparateChaining:
    def __init__(self, max_size):
        self.array_size = max_size
        self.array = [SinglyLinkedList() for item in range(self.array_size)]

    def hash(self, key):
        return sum(key.encode())

    def compress(self, hash_code):
        return hash_code % self.array_size

    def assign(self, key, value):
        array_index = self.compress(self.hash(key))
        payload = NodeSinglyLinked([key, value])
        list_at_index = self.array[array_index]
        for item in list_at_index:
            if key is item[0]:
                item[1] = value
                return
        list_at_index.insert(payload)
        return

    def retrieve(self, key):
        array_index = self.compress(self.hash(key))
        list_at_index = self.array[array_index]
        for item in list_at_index:
            if key is item[0]:
                return item[1]
        return None

    def delete(self, key):
        array_index = self.compress(self.hash(key))
        list_at_index = self.array[array_index]
        found_item = False
        value_to_delete = None
        for item in list_at_index:
            if key is item[0]:
                found_item = True
                value_to_delete = item[1]
        if found_item:
            list_at_index.remove_node([key, value_to_delete])
            return
        else:
            return