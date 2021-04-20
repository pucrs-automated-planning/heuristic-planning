# TODO Ensure we are not replicating stuff in this code
# -----------------------------------------------
# Applicable
# -----------------------------------------------


def applicable(state, positive, negative):
    return positive.issubset(state) and not negative.intersection(state)

# -----------------------------------------------
# Apply
# -----------------------------------------------


def apply(state, positive, negative):
    return frozenset(state.difference(negative).union(positive))

# -----------------------------------------------
# regressable
# -----------------------------------------------


def regressable(state, add_effects, del_effects):
    return add_effects.intersection(state) and del_effects.intersection(state)

# -----------------------------------------------
# regr
# -----------------------------------------------


def regress(state, action):
    return frozenset((state.difference(action.add_effects).union(action.positive_preconditions)))


def stateToLisp(state):
    lisp = '('
    # Nasty iterative way of doing this
    for literal in state:
        parf = ['{!s}' for par in literal]
        parf = ' '.join(parf)
        pars = parf.format(*list(literal))
        lisp += '({!s})'.format(pars)
    lisp += ') '
    return lisp

