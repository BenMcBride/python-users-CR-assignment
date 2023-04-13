from mysqlconnection import connectToMySQL # assuming connection file is called mysqlconnection.py

class User: # replace with name of class (table name)
    DB = "users_schema" # replace with name of schema
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;" # change all mentions of 'users' to table name
        results = connectToMySQL(cls.DB).query_db(query)
        users = []
        for i in results:
            users.append( cls(i) )
        return users
    # class method to save our friend to the database
    @classmethod #
    def save(cls, data ): # change all mentions of 'users' to table name
        # change 'query =' line to  "INSERT INTO *table_name* (column_1_name, column_2_name) VALUES ((%(*input_name from HTML*)s,%(*input_name from HTML*)s))"
        query = "INSERT INTO users ( first_name , last_name , email , created_at, updated_at ) VALUES ( %(fname)s , %(lname)s , %(email)s , NOW() , NOW() );"
        result = connectToMySQL(cls.DB).query_db( query, data )
        return result
    @classmethod
    def get_one(cls, user_id): # server.py calls this to get 1 id from a friend with @app.route('/friend/show/<int:friend_id>')
        # change instances of 'friend_id' and 'users' in both to match the db table you're working from
        query  = "SELECT * FROM users WHERE id = %(id)s";
        data = {'id':user_id}
        results = connectToMySQL(cls.DB).query_db(query, data)
        return cls(results[0])