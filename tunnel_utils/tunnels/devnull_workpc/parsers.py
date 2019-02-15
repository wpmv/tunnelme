import re


def extract_coordinates(input_message, coordinate_regex=None):
    """
    Extract the challenge coordinates from the raw challenge message.
    :param input_message: (str) Raw message from host
    :param coordinate_regex: (str) Regex to parse coordinates
    :return: 2D array of coordinates on the grid
    """
    default_coord_regex = r"\[\w{2}\]"
    coords = [
        [index[0].lower(), int(index[1])]
        for index in [
            coord.strip("[").strip("]")
            for coord in re.findall(
                coordinate_regex or default_coord_regex, input_message
            )
        ]
    ]
    return coords
