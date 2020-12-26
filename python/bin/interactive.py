#!/usr/bin/env python3
import os
import importlib

DAY = os.getenv('DAY')

if DAY:
    src = importlib.import_module(f'day{DAY}')
    tests = importlib.import_module(f'tests.test_day{DAY}')

    globals().update({k: getattr(src, k) for k in [m for m in src.__dict__ if not m.startswith('_')]})
    globals().update({k: getattr(tests, k) for k in [m for m in tests.__dict__ if m.startswith('EXAMPLE')]})
