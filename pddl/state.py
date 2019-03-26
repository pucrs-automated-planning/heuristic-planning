#-----------------------------------------------
# Applicable
#-----------------------------------------------

def applicable(state, precondition):
    positive, negative = precondition 
    return positive.issubset(state) and not negative.intersection(state)

#-----------------------------------------------
# Apply
#-----------------------------------------------

def apply(state, effects):
    positive, negative = effects
    return frozenset(state.difference(negative).union(positive))