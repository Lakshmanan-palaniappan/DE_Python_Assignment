def merge_the_tools(string, k):
    result = []
    for i in range(0, len(string), k):
        substring = string[i:i+k]
        seen = set()
        res = []
        for j in substring:
            if j not in seen:
                seen.add(j)
                res.append(j)
        result.append(''.join(res))
    return result