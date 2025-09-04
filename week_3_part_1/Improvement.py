def to_fahrenheit(celsius):
    # docsting
    """Convert a given temperature in Celsius to Fahrenheit , as long as it is above absolute zero."""

    if celsius < -273.15:
        return "Temperature below -273.15 is not possible"
    else :
        fahrenheit = 1.8 * celsius + 32
        return fahrenheit
