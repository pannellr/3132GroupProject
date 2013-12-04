#!/local/bin/python

from subject import Subject
from insertbuilder import InsertBuilder
from selectbuilder import SelectBuilder
from deletebuilder import DeleteBuilder

class Post(Subject):
    _post_id = None
    _user_id = None
    _lat = None
    _lng = None
    _post = None

     
    def __init__(self, post_id=None, post=None, user_id=None, lat=None, lng=None):
        super(Post, self).__init__()
        self._post_id = post_id
        self._post = post
        self._user_id = user_id
        self._lat = lat
        self._lng = lng

    # Accesors
    def post(self):
        return self._post

    def post(self, value):
        self._post = value

    def user_id(self):
        return self._user_id

    def user_id(self, value):
        self._user_id = value

    def post_id(self):
        return self._post_id

    def post_id(self, post_id):
        self._post_id = post_id

    def lat(self, lat):
        self._lat = lat

    def lat(self):
        return self._lat

    def lng(self, lng):
        self._lng = lng

    def lng(self):
        return self._lng

    

    # Database methods
    def all(self):
        posts = dict()
        result = super(Post, self).all('posts')
        while True:
            post = result.fetch_row(1,1)
            if not post: break
            post_id = post[0]['post_id']
            posts[post_id] = { 'post_id' : str(post[0]['post_id']),
                               'user_id' : str(post[0]['user_id']),
                               'lat' : str(post[0]['lat']),
                               'lng' : str(post[0]['lng']),
                               'post' : str(post[0]['post']),
                               'comments' : dict(),
                               'created_at' : post[0]['created_at'].strftime('%m/%d/%Y')
                               }
            #get the comments
            select = SelectBuilder()
            select.setStatement('select *')
            select.setTables('from comments')
            select.setWhere('where post_id = ' + str(post[0]['post_id']))
            comments = self._db.execute(select)

            while True:
                comment = comments.fetch_row(1,1)
                if not comment: break
                comment_id = comment[0]['comment_id']
                posts[post_id]['comments'][comment_id] = { 'comment_id' : str(comment[0]['comment_id']),
                                                  'user_id' : str(comment[0]['user_id']),
                                                  'comment' : str(comment[0]['comment']),
                                                  'created_at' : comment[0]['created_at'].strftime('%m/%d/%Y')
                                                  }
        return posts
        
        

    def fetch(self, post_id):
        post = self._db.query('select * from posts where post_id = ' + post_id)
        return post

    def save(self):
        if self._post_id:
            self.update(self)
        else:
            try:
                insert = InsertBuilder()
                insert.setStatement('insert into posts (user_id, post, lat, lng)')
                insert.setValues('values ("1", "' + self._post + '" , "44.34567", "-66.78945")')
                self._db.execute(insert);
            except:
                print "Could not insert record"

            self.notify()
        

    def update(self, post):
        try:
            self._db.query('update posts set user_id ="'+post.user_id()+'", post = "'+post.post()+'", lat ="'+post.lat()+'", lng = "'+post.lng()+'" where post_id = "' + post.post_id()).commit()
        except:
            #self.setMessage('Post could not be updated')
            print "query failed"
            
 #       self.notify()

    def destroy(self, post_id):
        delete = DeleteBuilder()
        delete.setStatement('delete from posts where post_id = ' + str(post_id))
        self._db.execute(delete)
        self.notify()
