def get_val(collection, key=None, default='git'):
    if key == None:
        return collection.values(default)
    return collection[key]





