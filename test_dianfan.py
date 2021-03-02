from datetime import date
from datetime import datetime

import pytest

from dianfan import get_next_workday
from dianfan import get_remaining_dianfan_count
from dianfan import get_remaining_workday_count_in_month


"""
chinese_calendar library does not care about tz
"""


@pytest.mark.parametrize(
    "input,output",
    (
        (datetime(2021, 2, 8, 1, 1, 1, 1), date(2021, 2, 9)),
        (datetime(2021, 2, 10, 1, 1, 1, 1), date(2021, 2, 18)),
        (datetime(2021, 2, 11, 1, 1, 1, 1), date(2021, 2, 18)),
        (datetime(2021, 2, 18, 1, 1, 1, 1), date(2021, 2, 19)),
    ),
)
def test_next_workday(input: datetime, output: date):
    assert get_next_workday(input).date() == output


@pytest.mark.parametrize(
    "input,output",
    (
        (datetime(2021, 2, 26, 1, 1, 1, 1), 1),
        (datetime(2021, 2, 25, 1, 1, 1, 1), 2),
        (datetime(2021, 2, 21, 1, 1, 1, 1), 5),
        (datetime(2021, 2, 20, 1, 1, 1, 1), 6),
        (datetime(2021, 2, 18, 1, 1, 1, 1), 8),
    ),
)
def test_get_remaining_workday_count_in_month(input: datetime, output: int):
    assert get_remaining_workday_count_in_month(input) == output


@pytest.mark.parametrize(
    "input,output",
    (
        (datetime(2021, 2, 25, 1, 1, 1, 1), 1),
        (datetime(2021, 2, 26, 1, 1, 1, 1), 23),
    ),
)
def test_get_remaining_dianfan_count(input: datetime, output: int):
    assert get_remaining_dianfan_count(input) == output
