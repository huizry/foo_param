import pytest
from foo_param import calculations

# Typical volume
def test_sphere_volume_typical():
    assert calculations.sphere_volume(3.12) == pytest.approx(127.22, rel=1e-2)

# Small volume
def test_sphere_volume_small():
    assert calculations.sphere_volume(0.54) == pytest.approx(0.66, rel=1e-2)

# Very small volume
def test_sphere_volume_very_small():
    assert calculations.sphere_volume(1.26e-5) == pytest.approx(8.37e-15, rel=1e-2)

# Large volume
def test_sphere_volume_large():
    assert calculations.sphere_volume(957047.25) == pytest.approx(3.67e18, rel=1e-2)

# Very large volume
def test_sphere_volume_very_large():
    assert calculations.sphere_volume(1.26e10) == pytest.approx(8.37e30, rel=1e-2)

# Zero volume
def test_sphere_volume_zero():
    assert calculations.sphere_volume(0) == 0

# Negative volume
def test_sphere_volume_negative():
    with pytest.raises(ValueError):
        calculations.sphere_volume(-4.19)

# Wrong radius type
def test_sphere_volume_str():
    with pytest.raises(TypeError):
        calculations.sphere_volume("hello world!")