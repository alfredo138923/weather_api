from datetime import datetime
from utils import unix_timestamp_to_readable_date, deg_to_compass
import random


def test_unix_timestamp_to_readable_date():

    unix_timestamp = 1653270268
    timestamp = datetime(2022, 5, 22, 20, 44, 28)

    result = unix_timestamp_to_readable_date(unix_timestamp)

    assert timestamp == result


def test_degress_to_compass():
    # Test North direction

    assert deg_to_compass(random.uniform(0, 11.25)) == 'North'

    assert deg_to_compass(random.uniform(11.26, 33.75)) == 'North-Northeast'

    assert deg_to_compass(random.uniform(33.76, 56.25)) == 'Northeast'

    assert deg_to_compass(random.uniform(56.26, 78.75)) == 'East-Northeast'

    assert deg_to_compass(random.uniform(78.76, 101.25)) == 'East'

    assert deg_to_compass(random.uniform(101.26, 123.75)) == 'East-Southeast'
    assert deg_to_compass(random.uniform(123.76, 146.25)) == 'Southeast'
    assert deg_to_compass(random.uniform(146.26, 168.75)) == 'South-Southeast'
    assert deg_to_compass(random.uniform(168.76, 191.25)) == 'South'
    assert deg_to_compass(random.uniform(191.26, 213.75)) == 'South-Southwest'
    assert deg_to_compass(random.uniform(213.76, 236.25)) == 'Southwest'
    assert deg_to_compass(random.uniform(236.26, 258.75)) == 'West-Southwest'

    assert deg_to_compass(random.uniform(258.76, 281.25)) == 'West'
    assert deg_to_compass(random.uniform(281.26, 303.76)) == 'West-Northwest'
    assert deg_to_compass(random.uniform(303.76, 326.25)) == 'Northwest'
    assert deg_to_compass(random.uniform(326.25, 348.75)) == 'North-Northwest'
    assert deg_to_compass(random.uniform(348.76, 360)) == 'North'
