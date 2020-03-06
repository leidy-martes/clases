def score(word):
    d =      { x:1  for x in 'AEIOULNRST'} 
    d.update({ x:2  for x in 'DG'})
    d.update({ x:3  for x in 'BCMP'})
    d.update({ x:4  for x in 'FHVWY'})
    d.update({ x:5  for x in 'K'})
    d.update({ x:8  for x in 'JX'})
    d.update({ x:10 for x in 'QZ'})

    s = 0
    for c in word.upper():
        s += d[c]

    return s
