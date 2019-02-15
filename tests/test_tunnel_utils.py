"""Test package level functionality of tunnel_utils"""

import tunnel_utils

def test_has_version():
    """Test that a __version__ attribute is defined."""
    assert hasattr(tunnel_utils, "__version__")
