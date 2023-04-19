import itertools
from collections import ChainMap

# best
enumerate(..., start=0)
itertools.takewhile(lambda x: x, ...)
itertools.accumulate(...)

# chain
ChainMap()
itertools.chain(...)
itertools.chain.from_iterable(...)

# zip
itertools.zip_longest(...)
zip(..., strict=True)

# grouping
itertools.pairwise(...)
itertools.groupby(...)

# feature
itertools.starmap(..., ...)
itertools.cycle(...)

