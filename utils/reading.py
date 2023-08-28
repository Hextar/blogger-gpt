# from utils.reading import get_reading_speed

def calculate_reading_time(text):
    """
    Calculate the estimated reading time for a given text.

    Args:
        text (str): The text to be read.

    Returns:
        int: Estimated reading time in seconds.
    """
    words = len(text.split())
    reading_time_minutes = words / 400
    reading_time_seconds = int(reading_time_minutes * 60)

    return reading_time_seconds
