import datetime
from threading import Timer
import itchat
import DailyInfo
import JsonChange
def send_daily(timeStr):
    day = datetime.datetime.strptime(timeStr,"%Y%m%d")
    tomorrowStr = (day +datetime.timedelta(days=1)).strftime("%Y%m%d")
    msg = get_daily_msg(timeStr)+DailyInfo.checkReturnMsg(timeStr)
    itchat.send(msg,'filehelper')
    timer = Timer(86400,send_daily,[tomorrowStr])
    timer.start()

def get_interval_secs(target_time):
    today = (datetime.datetime.today()).strftime("%Y%m%d")
    today_target = today + target_time
    today_target_datetime = datetime.datetime.strptime(today_target,'%Y%m%d%H%M%S')
    now_datetime = datetime.datetime.now()
    interval = today_target_datetime - now_datetime
    secs = interval.total_seconds()
    if secs > 0 :
        print(secs)
        return int(secs),True
    else:
        print(secs+86400)
        return int(secs + 86400),False

def get_daily_msg(TimeStr):
    Askday = datetime.datetime.strptime(TimeStr,"%Y%m%d")
    today =datetime.datetime.today()
    first_day = datetime.datetime(2019,8,26)
    delta = (Askday-first_day).days
    weeks = int(delta / 7) + 1
    day = delta % 7 + 1
    msg = ""
    DayOfWeek = ['','周一','周二','周三','周四','周五','周六','周日']
    if Askday.strftime("%Y%m%d") == today.strftime("%Y%m%d"):
        msg = msg + '今天是第'+ str(weeks) + '周'+DayOfWeek[day]+'\n'
    else:
        msg = msg + Askday.strftime("%Y,%m,%d")+" 第"+str(weeks)+'周'+DayOfWeek[day]+":\n"
    calculator = 0
    dict =JsonChange.read('./classes.json')
    for classes,lines in dict.items():
        for each in lines:
            if weeks in each['Week'] and DayOfWeek[day] == each['Day']:
                msg = msg+classes+":"+"时间:"+each['Time']+"\n地点:"+each['Place']+"\n教师:"+each['Teacher']+"\n"
                calculator += 1
    if calculator == 0:
        msg += "今日无课\n"
    else:
        msg += "今天共{}节课\n".format(calculator)
    return msg

def getTodayStr():
    return datetime.datetime.today().strftime("%Y%m%d")
def getTomorrowStr():
    t = datetime.datetime.today() + datetime.timedelta(days=1)
    tStr = t.strftime("%Y%m%d")
    return tStr
