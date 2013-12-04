#!/local/bin/python

from subject import Subject
from insertbuilder import InsertBuilder

class Comment(Subject):

    _comment_id = None
    _user_id = None
    _post_id = None
    _comment = None
    
    def __init__(self, comment_id = None):
        super(Comment, self).__init__()
        self._comment_id = comment_id

    def comment(self, comment):
        self._comment = comment

    def user_id(self, user_id):
        self._user_id = user_id

    def post_id(self, post_id):
        self._post_id = post_id

    def save(self):
        
        if self._comment_id:
            self.update(self)
        else:
            try:
                insert = InsertBuilder()
                insert.setStatement('insert into comments (user_id, post_id, comment)')
                insert.setValues('values ("' + self._user_id + '", "' + self._post_id + '" , "' + self._comment +'")')
                self._db.execute(insert);
            except:
                print "Could not insert record"
                
        self.notify()

    def update(self):
        update = UpdateBuilder()
