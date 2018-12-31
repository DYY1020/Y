import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self,m):
    
        m=int(m) if m is not None else 9
        html = '''
        <html>
        <body>
        <table>
        '''
        for i in range(1, m+1):
            html +='<tr>'
            for j in range(1, i+1):
                html += '<td>%d*%d=%d</td>' % (i,j,i*j)
            html +='</tr>'

        html +='''
        <ml>
        </body>
        </table>
        '''
        self.write(html)


        

application=tornado.web.Application([
        (r"(?:/([0-9])?)",MainHandler)
    ])


if __name__ == '__main__':    
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
