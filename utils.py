from datetime import datetime


def unix_timestamp_to_readable_date(posix_time):
    """
        Convert unix_timestamp to readable date
    :param posix_time:
    :return:
    """

    res = datetime.fromtimestamp(posix_time)

    return res


def deg_to_compass(degrees):
    """
    Convert degresses to cardinal directions
    :param degrees:
    :return:
    """

    cardinal_directions = [
        "North", "North-Northeast", "Northeast", "East-Northeast", "East",
        "East-Southeast", "Southeast", "South-Southeast", "South", "South-Southwest",
        "Southwest", "West-Southwest", "West", "West-Northwest", "Northwest", "North-Northwest"
    ]

    val = int((degrees / 22.5) + .5)

    return cardinal_directions[(val % 16)]
