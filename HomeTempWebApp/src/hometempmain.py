import webapp2
from google.appengine.ext import db

class Datalogging(db.Model):
    #content = db.StringProperty(multiline=False)
    t1 = db.FloatProperty()
    t2 = db.FloatProperty()
    t3 = db.FloatProperty()
    t4 = db.FloatProperty()
    date = db.DateTimeProperty(auto_now_add=True)

class MainPage(webapp2.RequestHandler):
    def get(self):
      
        
        self.response.headers['Content-Type'] = 'text/plain'
        n=self.request.get('value1')
        m=self.request.get('value2')
        o=self.request.get('value3')
        p=self.request.get('value4')
        del_command=self.request.get('empty')
        if del_command=='true':
            self.response.out.write('Clear all data\n')
            dataloggings = db.GqlQuery("SELECT * FROM Datalogging")
            db.delete(dataloggings)
        else:
            if not n:
                self.response.out.write('Empty input. Recently 10 stored values are:\n')
                dataloggings = db.GqlQuery("SELECT * FROM Datalogging ORDER BY date DESC LIMIT 10")
                for datalogging in dataloggings:
                    self.response.out.write('%s\t%s\t%s\t%s\t%s' %(datalogging.t1,datalogging.t2,datalogging.t3,datalogging.t4,datalogging.date))            
                    self.response.out.write('\n')
            else:
                self.response.out.write('logging: %s\t%s\t%s\t%s\n' %(n,m,o,p))
                datalogging = Datalogging()
                datalogging.t1 = float(n)
                datalogging.t2 = float(m)
                datalogging.t3 = float(o)
                datalogging.t4 = float(p)
                datalogging.put()

app = webapp2.WSGIApplication([('/', MainPage)], debug=True)
