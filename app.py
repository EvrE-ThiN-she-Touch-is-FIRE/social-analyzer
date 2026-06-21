#!/usr/bin/env python
"""CLI entry point for repo-root execution."""

import os
import sys
from importlib import import_module

ROOT = os.path.dirname(os.path.abspath(__file__))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

if __name__ == '__main__':
    import_module('social-analyzer').main_logic()