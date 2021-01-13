import os
from datetime import datetime

import chinese_calendar
import requests


def main():
    is_workday_today = chinese_calendar.is_workday(datetime.today())
    print("is_workday_today: ", is_workday_today)

    if not is_workday_today:
        return

    url = f"https://oapi.dingtalk.com/robot/send?access_token={os.getenv('DINGTALK_ACCESS_TOKEN')}"
    response = requests.post(
        url,
        json={
            "msgtype": "text",
            "text": {"content": "点饭"},
            "at": {"atMobiles": [], "isAtAll": True},
        },
    )

    print(response.content)


if __name__ == "__main__":
    main()
