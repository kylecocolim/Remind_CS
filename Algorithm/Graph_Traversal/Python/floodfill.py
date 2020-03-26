def fill(data, start_coords, fill_value):
    xsize, ysize = data.shape
    orig_value = data[start_coords[0], start_coords[1]]
    
    stack = set(((start_coords[0], start_coords[1]),))
    while stack:
        x, y = stack.pop()

        if data[x, y] == orig_value:
            data[x, y] = fill_value
            if x > 0:
                stack.add((x - 1, y))
            if x < (xsize - 1):
                stack.add((x + 1, y))
            if y > 0:
                stack.add((x, y - 1))
            if y < (ysize - 1):
                stack.add((x, y + 1))