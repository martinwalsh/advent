#!/usr/bin/env python
import os
import pytest
import inspect
import contextlib


@pytest.fixture(scope="function")
def load_input():
    @contextlib.contextmanager
    def _load_input(path):
        caller = inspect.stack()[2]
        path = os.path.join(os.path.dirname(caller.filename), path)
        with open(path) as f:
            yield f.read()

    return _load_input
