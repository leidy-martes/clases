def to_rna(dna_strand):
    dic= {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
    '''a =[]
    'for x in dna_strand:
        'a.append(dic[x])'''
    return ''.join([dic[x] for x in dna_strand])
