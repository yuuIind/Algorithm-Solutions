def flatten_generator(item):
    if isinstance(item, (list, tuple)):
        for subitem in item:
            yield from flatten_generator(subitem)
    elif item is not None:
        yield item

def flatten(iterable):
    flattened = []
    for item in iterable:
        flattened.extend(flatten_generator(item))
    return flattened
