def print_formatted(number):
    lines = []
    for i in range(1, number + 1):
        decimal_str = str(i)
        octal_str = oct(i)[2:]
        hex_str = hex(i)[2:].upper()
        binary_str = bin(i)[2:]
        line = f"{decimal_str} {octal_str} {hex_str} {binary_str}"
        lines.append(line)
    return "\n".join(lines)