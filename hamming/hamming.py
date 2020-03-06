def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Incorrect length of strands")
    i=0
    sum = 0
    for ch in strand_a:
        if ch != strand_b[i]:
            sum+=1
        i+=1
    return sum
