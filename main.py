#coding: utf-8
import json
import tornado.ioloop  
import tornado.web  
from send_mail import send_mail
  
class MainHandler(tornado.web.RequestHandler):  
    def get(self):  
        self.write("Hello, world") 


class SendHandler(tornado.web.RequestHandler):
    def post(self):
        body = json.loads(self.request.body)
        receve = body["receve"].encode("utf-8")
        subject = body["subject"].encode("utf-8")
        context = body["context"].encode("utf-8")
        self.write(send_mail(receve, subject, context))

    def get(self):
        receve = self.get_argument("receve", "").encode("utf-8")
        subject = self.get_argument("subject", "").encode("utf-8")
        context = self.get_argument("context", "").encode("utf-8")
        self.write(send_mail(receve, subject, context)) 
        #self.write("this get method {} {} {}\n".format(receve, subject, context)) 
  
def main():
    application = tornado.web.Application([  
        (r"/",MainHandler),  
        (r"/send", SendHandler)
    ])  
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
  
if __name__=="__main__":  
    main()
