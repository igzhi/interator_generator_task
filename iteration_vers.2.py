nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]

class FlatIterator:
    def __init__(self, _list):
        self._list = _list
    def __iter__(self):
        self.cursor = -1
        return self
    def __next__(self):
        flat_list = sum(self._list,[])
        self.cursor += 1
        if self.cursor == len(flat_list):
            raise StopIteration
        return flat_list[self.cursor]

if __name__ == '__main__':
    for elem in FlatIterator(nested_list):
        print(elem)