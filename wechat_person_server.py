import itchat,time,re
from itchat.content import *
@itchat.msg_register([TEXT])
def text_reply(msg):
    for i in range(3):
        time.sleep(2)
        if "二狗" in msg["Text"]:
            itchat.send(("你才是二狗"),msg["FromUserName"])
        elif "你好" in msg["Text"]:
            itchat.send(("请给我发红包，不然我会不停的发"), msg["FromUserName"])
        elif "资料" in msg["Text"]:
            itchat.send(("请转发文章领取资料或者给文章打赏"), msg["FromUserName"])
        elif "在吗" in msg["Text"]:
            itchat.send(("请不要问我在不在，万一是找我借钱呢"), msg["FromUserName"])
        else:
            itchat.send(("请发红包开启与机器人美女聊天模式"), msg["FromUserName"])
# match3 = re.search("资料", msg["Text"]).span()
@itchat.msg_register([PICTURE,RECORDING,VIDEO,SHARING])
def other_reply(msg):
    for i in range(3):
        time.sleep(2)
        itchat.send(("请给我发红包，不然我会不停的发"),msg["FromUserName"])
itchat.login()
itchat.run()
# itchat.auto_login(hotReload=True)
