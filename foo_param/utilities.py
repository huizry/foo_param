def format_volume(volume: int | float, ndigits: int, unit: str, geo_obj: str,) -> str:
    """
    Formats the volume as a string with rounding, unit of measurement, and the shape of the object.

        Parameters
        ----------
        volume : float
            The volume of the geometrical object
        ndigits: int
            The number of decimals to use when rounding the number
        unit: str
            The unit of measurement for the volume
        geo_obj: str
            The name of the geometrical object

        Returns
        ----------
        str
            The formatted volume output
    """

    if not (type(volume) is int or type(volume) is float):
        raise TypeError("Volume must be int or float")
    if type(ndigits) is not int:
        raise TypeError("ndigits must be int")
    if type(unit) is not str:
        raise TypeError("unit must be str")
    if type(geo_obj) is not str:
        raise TypeError("shape must be str")

    return f"The volume of {geo_obj.strip().lower()} is {round(volume, ndigits)} cubic {unit.strip().lower()}."