# Stubs for torch.multiprocessing.pool (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

import multiprocessing.util
from .queue import SimpleQueue
from typing import Any

def clean_worker(*args: Any, **kwargs: Any) -> None: ...

class Pool(multiprocessing.pool.Pool): ...