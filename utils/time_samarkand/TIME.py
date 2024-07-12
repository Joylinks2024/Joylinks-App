# def get_sam_datetime():
#     import datetime
#     import pytz
#     now = datetime.datetime.now(pytz.utc)
#     tz_samarkand = pytz.timezone('Asia/Samarkand')
#     now_samarkand = now.astimezone(tz_samarkand).strftime('%Y-%m-%d %H:%M:%S')
#     return now_samarkand
#
# print(get_sam_datetime())
# ______________________________________________________________________________________________________________________


async def date_time_now():
    import datetime
    import pytz

    now = datetime.datetime.now(pytz.timezone('Asia/Samarkand'))
    return int(datetime.datetime.timestamp(now))


# print(type(date_time_now()))
# import datetime
#
# dt_object = datetime.datetime.fromtimestamp(date_time_now())
#
# print(dt_object)
async def timestamp(timestamp):
    import datetime
    dt_object = datetime.datetime.fromtimestamp(timestamp)
    return dt_object
