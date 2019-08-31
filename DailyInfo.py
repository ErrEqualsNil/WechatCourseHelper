import JsonChange
path = "./DailyInfo.json"
def createInfo(timeStr,Info):
    dict = JsonChange.read(path)
    if dict is not None:
        if timeStr not in dict.keys():
            dict[timeStr] = []
        dict[timeStr].append(Info)
    JsonChange.change(path,dict)

def checkReturnMsg(timeStr):
    msg = '今日事项如下:\n'
    dict = JsonChange.read(path)
    if timeStr in dict.keys() and len(dict[timeStr]) is not 0:
        for each in dict[timeStr]:
            msg = msg + each + '\n'
    else:
        msg = '今天无记录项'
    return msg

def deleteMsg(timeStr,msgContent):
    success = False
    dict = JsonChange.read(path)
    if timeStr in dict.keys():
        if msgContent == "all":
            dict.pop(timeStr)
        else:
            dict[timeStr].remove(msgContent)
        success =True
    JsonChange.change(path,dict)
    if success:
        return "删除成功"
    else:
        return "删除失败"
