import os, time, requests

from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    def handle(self, *args, **options):
        url = os.getenv("APITABLE_BASE_URL") + "/fusion/v1/datasheets/dstq4XcMvHojo2chjz/records"
        token = os.getenv("APITABLE_TOKEN")
        records = []

        with connection.cursor() as cursor:
            time_start = '2024-01-01 00:00:00'
            time_end = '2024-01-31 23:59:59'
            cursor.callproc('GetSalesAmountRankingBySPU', (time_start, time_end))
            rows = cursor.fetchall()
            for row in rows:
                print(row)
                r = {
                    "品牌": row[0],
                    "SPU名称": row[1],
                    "销售额": float(row[2]),
                    "时间": time_start[:7]
                }
                records.append({ "fields": r })

        print(len(records))
        for i in range(int(len(records)/30)+1):
            s = 30 * i
            e = 30 * (i + 1)
            if i == int(len(records)/30):
                e = len(records)
            res = requests.post(
                url=url,
                json={"records": records[s:e]},
                headers={"Authorization": f"Bearer {token}"},
            )
            res.raise_for_status()
            time.sleep(1)
