# -*- coding: utf-8 -*-
# filename: handle.py
import reply
import receive
import web
import hashlib
import web

class Handle(object):
    def GET(self):
        try:
            print 'get'
            data = web.input()
            if len(data) == 0:
                return "hello, this is handle view"
	    print data
            signature = data.signature
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr
            token = "helloworld" #请按照公众平台官网\基本配置中信息填写

            list = [token, timestamp, nonce]
            list.sort()
            sha1 = hashlib.sha1()
            map(sha1.update, list)
            hashcode = sha1.hexdigest()
            print "handle/GET func: hashcode, signature: ", hashcode, signature
            if hashcode == signature:
                return echostr
            else:
                return ""
        except Exception, Argument:
            return Argument
        
    def POST(self):
        try:
	    print 'post'
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
