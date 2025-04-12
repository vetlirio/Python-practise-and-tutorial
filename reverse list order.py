ef reverse_list(items):
    new_items = []
    for i in range(len(items) - 1, -1, -1):
        new_items.append(items[i])
    return new_items