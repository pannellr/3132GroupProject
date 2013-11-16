import MySQLdb

class Database:

    #values needed to establish connection
    database_name = ''
    database_user = ''
    database_pass = ''
    database_host = ''
    database_handle = ''



    def __init__(self, name, user, password, host):
        self.database_name = name
        self.database_user = user
        self.database_pass = password
        self.database_host = host

    def connect(self):
        self.database_handle = MySQLdb.connect(self.database_host,
                                               self.database_user,
                                               self.database_pass,
                                               self.database_host,
                                               self.database_name
                                               )

    
    def dump(self):
        print self
