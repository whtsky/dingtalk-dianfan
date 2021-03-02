import os
from datetime import datetime
from datetime import timedelta

import chinese_calendar
import requests

_postfixes = ["呀", "啦", "哟", "了吗？", "咯"]


def get_postfix(date: datetime) -> str:
    return _postfixes[date.weekday() % len(_postfixes)]


one_day = timedelta(days=1)


def get_next_workday(date: datetime) -> datetime:
    date += one_day
    while not chinese_calendar.is_workday(date):
        date += one_day
    return date


def get_remaining_workday_count_in_month(date: datetime) -> int:
    count = 0
    start_month = date.month
    while date.month == start_month:
        if chinese_calendar.is_workday(date):
            count += 1
        date = get_next_workday(date)
    return count


def get_remaining_dianfan_count(date: datetime) -> int:
    dianfan_target_date = get_next_workday(date)
    return get_remaining_workday_count_in_month(dianfan_target_date)


def main():
    today = datetime.today()
    is_workday_today = chinese_calendar.is_workday(today)
    print("is_workday_today: ", is_workday_today)

    if not is_workday_today:
        return

    content = f"点饭{get_postfix(today)}"
    remaining_dianfan_count = get_remaining_dianfan_count(today)
    if remaining_dianfan_count < 5:
        content += f"\n本月还能点{remaining_dianfan_count}次饭\n记得设零点的闹钟抢面包哟"

    url = f"https://oapi.dingtalk.com/robot/send?access_token={os.getenv('DINGTALK_ACCESS_TOKEN')}"
    response = requests.post(
        url,
        json={
            "msgtype": "text",
            "text": {"content": content},
            "at": {"atMobiles": [], "isAtAll": True},
        },
    )

    print(response.content)


if __name__ == "__main__":
    main()
