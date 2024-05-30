import math

def sphere_volume(radius: int | float) -> float:
    """
    Calculates the volume of a sphere

        Parameters
        ----------
        radius : float
            The radius of the sphere

        Returns
        ----------
        float
            The volume of the sphere

        Raises
        ----------
        ValueError
            If the radius of the sphere is negative
    """

    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return (4/3) * math.pi * (radius ** 3)