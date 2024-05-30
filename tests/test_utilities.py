import pytest
from foo_param import utilities

# Typical volume
def test_format_volume_typical():
    assert utilities.format_volume(3.12, 2, "cm", "sphere") == "The volume of sphere is 3.12 cubic cm."

# Small volume
def test_format_volume_small():
    assert utilities.format_volume(0.54, 2, "cm", "sphere") == "The volume of sphere is 0.54 cubic cm."

# Very small volume
def test_format_volume_very_small():
    assert utilities.format_volume(1.26e-5, 2, "cm", "sphere") == "The volume of sphere is 0.0 cubic cm."

# Large volume
def test_format_volume_large():
    assert utilities.format_volume(957047.25, 2, "cm", "sphere") == "The volume of sphere is 957047.25 cubic cm."

# Very large volume
def test_format_volume_very_large():
    assert utilities.format_volume(1.26e10, 2, "cm", "sphere") == "The volume of sphere is 12600000000.0 cubic cm."

# Zero volume
def test_format_volume_zero():
    assert utilities.format_volume(0, 2, "cm", "sphere") == "The volume of sphere is 0 cubic cm."

# Negative volume
def test_format_volume_negative():
    assert utilities.format_volume(-4.19, 2, "cm", "sphere") == "The volume of sphere is -4.19 cubic cm."

# Wrong volume type
def test_format_wrong_volume_type():
    with pytest.raises(TypeError):
        utilities.format_volume("volume is not a string nor float", 2, 'cm', "sphere")

# Wrong ndigits type
def test_format_wrong_ndigits_type():
    with pytest.raises(TypeError):
        utilities.format_volume(3.14, "ndigits is not int", 'cm', "sphere")

# Wrong unit type
def test_format_wrong_unit_type():
    with pytest.raises(TypeError):
        utilities.format_volume(3.14, 2, 100, "sphere")

# Wrong shape type
def test_format_wrong_geo_obj_type():
    with pytest.raises(TypeError):
        utilities.format_volume(3.14, 2, 'cm', 100)