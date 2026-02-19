def align_text(thickness, c):
    pattern = []
    for i in range(thickness):
        line = " " * (thickness - i - 1) + c * (2 * i + 1) + " " * (thickness - i - 1)
        pattern.append(line)
    for i in range(thickness + 1):
        line = (c * thickness) + " " * (thickness * 4) + (c * thickness)
        pattern.append(line)
    for i in range((thickness + 1) // 2):
        line = c * (thickness * 6)
        pattern.append(line)
    for i in range(thickness + 1):
        line = (c * thickness) + " " * (thickness * 4) + (c * thickness)
        pattern.append(line)
    for i in range(thickness):
        spaces = " " * i
        chars = c * (2 * (thickness - i) - 1)
        line = " " * (thickness * 4) + spaces + chars + spaces
        pattern.append(line)
    return pattern

