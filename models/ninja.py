from dojos_ninjas_app.config.mysqlconnection import connectToMySQL

DATABASE = "dojo_ninjas"


class Users:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL(DATABASE).query_db(query)
        ninjas = []
        for result in results:
            ninjas.append(cls(result))
        return ninjas

    @classmethod
    def save(cls, data):
        query = "INSERT INTO ninjas (first_name,last_name, age, dojo_id, created_at, updated_at ) VALUES ( %(first_name)s , %(last_name)s ,%(age)s ,  %(dojo_id)s, NOW(), NOW()) ;"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_by_id(cls, data):
        result = []
        query = "SELECT id FROM ninjas WHERE title = %(first_name)s AND last_name = %(last_name)s"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result[0]['id']

    @classmethod
    def get_info(cls, data):
        query = "SELECT * FROM ninjas WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = "UPDATE ninjas SET first_name = %(first_name)s, last_name = %(last_name)s, age = %(age)s, updated_at = NOW() WHERE id= %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM ninjas WHERE id = %(id)s"
        return connectToMySQL(DATABASE).query_db(query, data)
