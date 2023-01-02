import inspect
from objprint import op

def f():
    frame = inspect.currentframe()
    op(
        frame,
        honor_existing = False,
        depth=2
    )

f()