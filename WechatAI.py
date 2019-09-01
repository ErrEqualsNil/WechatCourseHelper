import itchat
import ConnectTuling
from threading import Timer
import TimeControler
import re
import DailyInfo

@itchat.msg_register([itchat.content.TEXT])
def msg_reply(msg):
    today = TimeControler.getTodayStr()
    if msg['ToUserName'] == 'filehelper':
        print(msg)
        if msg['Content'] == '课表':
            itchat.send(TimeControler.get_daily_msg(today),'filehelper')
        elif re.match(r'课表 \d\d\d\d \d\d \d\d',msg['Content']):
            splits = msg['Content'].split(" ")
            timeStr = splits[1] + splits[2] + splits[3]
            itchat.send(TimeControler.get_daily_msg(timeStr),'filehelper')
        elif re.match(r'添加事项 \d\d\d\d \d\d \d\d .*',msg['Content']):
            splits = msg['Content'].split(" ")
            timeStr = splits[1]+splits[2]+splits[3]
            Info = splits[4]
            DailyInfo.createInfo(timeStr,Info)
            itchat.send('添加成功','filehelper')
        elif re.match(r'删除事项 \d\d\d\d \d\d \d\d .*', msg['Content']):
            splits = msg['Content'].split(" ")
            timeStr = splits[1] + splits[2] + splits[3]
            Info = splits[4]
            response = DailyInfo.deleteMsg(timeStr,Info)
            itchat.send(response,'filehelper')
        elif msg['Content'] == 'help':
            itchat.send("添加格式:添加事项 2000 01 01 做事\n"+"删除格式:删除事项 2000 01 01 做事(或all)\n",'filehelper')
        elif msg['Content'] == "事项":
            itchat.send(DailyInfo.checkReturnMsg(today),'filehelper')
    else:
        print(msg)
        response = ConnectTuling.postMsg(msg['Content'],msg['FromUserName'][1:32])
        return '[AI-助手自动回复]'+response

def main():
    itchat.auto_login(enableCmdQR=2)
    timeDelta,isToday = TimeControler.get_interval_secs("080000")
    today = TimeControler.getTodayStr()
    tomorrow = TimeControler.getTomorrowStr()
    msg = TimeControler.get_daily_msg(today)+DailyInfo.checkReturnMsg(today)
    itchat.send(msg, 'filehelper')
    if isToday:
        timer = Timer(timeDelta, TimeControler.send_daily, [today])
    else:
        timer = Timer(timeDelta, TimeControler.send_daily, [tomorrow])
    timer.start()
    itchat.run()

if __name__ == '__main__':
    main()