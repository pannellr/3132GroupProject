#!/local/bin/python

from subject import Subject
from selectbuilder import SelectBuilder

class User(Subject):

    _user_id = None
    _user_name = None
    _password = None
    _role = None

    def init(self, user=None):
        super(User, self).__init__()

    def return_pw(self, user_name = None):
        password = ''

        if user_name:
            select = SelectBuilder()
            select.setStatement('select password')
            select.setTables('from users')
            select.setWhere('where user_name = "' + user_name + '"')
            result = self._db.execute(select)
            row = result.fetch_row(1,1)
            password = row[0]

        return password


    def load(self,user_name = None):
        self._user_name = user_name

        if self._user_name:
            select = SelectBuilder()
            select.setStatement('select *')
            select.setTables('from users')
            select.setWhere('where user_name = "' + self._user_name +'"')
            result = self._db.execute(select)
            row = result.fetch_row(1,1)
            
            self._user_id = row[0]['user_id']
            self._user_name = row[0]['user_name']
            self._role = row[0]['role']
    
    
