
def mecabsplit(mecab_tagger,inputs, pos):
    r=[]
    inputs = mecab_tagger.parse(inputs)
    t = inputs.split('\n')[:-2]
    for i in t:
        field = i.split('\t')
        if field[1].split(',')[-1] is not '*':
            r.extend( [ (x.split('/')[0],x.split('/')[1]) for x in field[1].split(',')[-1].split('+') ] )
        else:
            r.append( (field[0],field[1].split(',')[0]) )
    if pos:
        return r
    else:
        return [ x[0] for x in r ]
    return r