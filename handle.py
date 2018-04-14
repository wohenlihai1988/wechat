# -*- coding: utf-8 -*-
# filename: handle.py

import hashlib
import web

class Handle(object):
    def GET(self):
        try:
            webData = web.data()
            print 'handle post webdata is ', webData
            recMsg = receive.parse_xml(webData)
            if isinstance(recMsg, receive.Msg) and recmsg.MstType == 'text':
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                content = 'test'
                replyMsg = reply.TextMsg(toUser, fromUser, content)
                return replyMsg.send()
            else:
                print 'do nothing for now'
                return 'success' 
        except Exception, Argument:
            return Argument