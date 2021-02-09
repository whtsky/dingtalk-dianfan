import os
from datetime import datetime

import chinese_calendar
import requests

_postfixes = ["呀", "啦", "哟", "了吗？", "咯"]


def get_postfix(date: datetime) -> str:
    return _postfixes[date.weekday() % len(_postfixes)]


def main():
    today = datetime.today()
    is_workday_today = chinese_calendar.is_workday(today)
    print("is_workday_today: ", is_workday_today)

    if not is_workday_today:
        return

    url = f"https://oapi.dingtalk.com/robot/send?access_token={os.getenv('DINGTALK_ACCESS_TOKEN')}"
    response = requests.post(
        url,
        json={
            "msgtype": "text",
            "text": {"content": f"点饭{get_postfix(today)}"},
            "at": {"atMobiles": [], "isAtAll": True},
        },
    )

    print(response.content)


if __name__ == "__main__":
    main()
