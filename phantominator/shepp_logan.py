"""Driving function.

Notes
-----
Calls to CT, MR, 2D, and 3D variants of Shepp-Logan will be handled
by this handler function.  It serves to point to the correct
implementation of Shepp-Logan to use given a set of parameters.
"""

from phantominator import ct_shepp_logan


def shepp_logan(*args, **kwargs):
    """Shepp-Logan phantom.

    Notes
    -----
    See phantominator.ct_shepp_logan() for docstrings explaining usage.
    """

    # Always use CT version (MR version removed)
    return ct_shepp_logan(*args, **kwargs)
