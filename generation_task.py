nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	[1, 2, None],
]

def flat_generator(a: list) -> list:
    return [x for sublist in a for x in sublist]

for item in  flat_generator(nested_list):
    print(item)