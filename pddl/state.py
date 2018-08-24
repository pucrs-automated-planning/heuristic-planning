#-----------------------------------------------
# Applicable
#-----------------------------------------------

def applicable(state, positive, negative):
    return positive.issubset(state) and not negative.intersection(state)

#-----------------------------------------------
# Apply
#-----------------------------------------------

def apply(state, positive, negative):
    return frozenset(state.union(positive).difference(negative))