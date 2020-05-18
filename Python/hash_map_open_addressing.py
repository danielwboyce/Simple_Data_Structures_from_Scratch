# This hash map uses open addressing and linear probing to handle collisions
class HashMapOpenAddressing:
  def __init__(self, array_size):
    self.array_size = array_size
    self.array = [None for item in range(array_size)]
    self.size = 0

  def has_space(self):
    return self.array_size > self.size

  # possible return values are None, True, or False
  def key_match(self, key, index):
    if self.array[index] is None:
      return None
    else:
      return key is self.array[index][0]

  def hash(self, key, count_collisions=0):
    key_bytes = key.encode()
    hash_code = sum(key_bytes)
    return hash_code + count_collisions

  def compressor(self, hash_code):
    return hash_code % self.array_size

  # given a key, this returns the index where the key has an entry
  # or None if it doesn't find one
  def index_finder(self, key):
    collisions = 0
    array_index = self.compressor(self.hash(key))

    if self.array[array_index] is None:
      return None
    elif self.key_match(key, array_index):
      return array_index
    else:
      while (self.array[array_index + collisions][0] is not key):
        if collisions is self.array_size:
          return None
        collisions += 1
      return array_index + collisions

  # given a key, this returns an empty index where the keypair can be
  # saved. if the array is full it returns None
  def empty_finder(self, key):
    if not self.has_space():
      return None
    else:
      array_index = self.compressor(self.hash(key))
      collisions = 0
      if self.array[array_index] is None:
        return array_index
      else:
        while(self.array[array_index + collisions] is not None):
          if collisions is self.array_size:
            return None
          collisions += 1
        return array_index + collisions

  def assign(self, key, value):
    if self.has_space() is False:
      return
    else:
      found_index = self.index_finder(key)
      if found_index is None:
        new_index = self.empty_finder(key)
        self.array[new_index] = [key, value]
        self.size += 1
        return
      else:
        self.array[found_index] = [key, value]
        return

  def retrieve(self, key):
    array_index = self.index_finder(key)
    if array_index is None:
      return None
    else:
      return self.array[array_index][1]

  def delete(self, key):
    array_index = self.index_finder(key)
    if array_index is None:
      return
    else:
      self.array[array_index] = None
      self.size -= 1
      return

