def bk(g,
       target_size,
       compsub=[],
       candidates=[]):
    '''
    bron-kerbosch algorithm. This version looks for cliques of
    a particular size.

    :param g: the graph (numpy.array)
    :param target_size: the size of clique to search for
    :param compsub: the current subclique
    :param candidates: row indices of nodes that are still potentials for the current clique
    '''

    if len(compsub) == target_size:
        # print "match:",compsub
        return [compsub[:]]

    rval = []

    # bootstrap candidates at start
    if len(compsub) == 0:
        candidates = [r for r in xrange(g.rows)]

    compsub.append(0) # add placeholder for new candidate

    for idx,cand in enumerate(candidates):
        compsub[-1] = cand
        new_candidates = filter(lambda x: g.get(x,cand), candidates[idx + 1:])
        rval += bk(g,
                   target_size,
                   compsub,
                   new_candidates)

    del compsub[-1] # remove placeholder

    return rval
        
