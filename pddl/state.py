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

