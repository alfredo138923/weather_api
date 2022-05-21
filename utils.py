from datetime import datetime


def unix_timestamp_to_readable_date(posix_time):
    res = datetime.fromtimestamp(posix_time)

    print(res)

    return res


def deg_to_compass(num):
    arr = [
        "North", "North-Northeast", "Northeast", "East-Northeast", "East",
        "East-Southeast", "Southeast", "South-Southeast", "South", "South-Southwest",
        "Southwest", "West-Southwest", "West", "West-Northwest", "Northwest", "North-Northwest"
    ]

    val = int((num / 22.5) + .5)

    return arr[(val % 16)]
