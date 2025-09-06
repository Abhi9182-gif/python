"""
Signal Processing Package

This package provides functionality for generating various signals
and performing operations on them.

Modules:
- unitary_signals: Unit step, impulse, and ramp signals
- trigonometric_signals: Sine, cosine, and exponential signals
- operations: Signal operations like shifting, scaling, etc.
"""

from . import unitary_signals
from . import trigonometric_signals
from . import operations

__version__ = "1.0.0"
__author__ = "Abhinay Choudhari"