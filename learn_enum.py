from enum import Enum, auto

BugStatus = Enum(
    value="Status",
    names=('new', 'invalid', 'with_break',
           'in_fixing', 'fixed',)
)

print('\n'.join(f"{s.name:15}: {s.value}" for s in BugStatus))