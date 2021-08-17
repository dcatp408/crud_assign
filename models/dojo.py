from dojos_ninjas_app.config.mysqlconnection import connectToMySQL
from dojos_ninjas_app.models import ninja
DATABASE = "dojo_ninjas"


class Dojo:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.ninjas = []

    @classmethod
    def dojo_with_ninjas(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas on ninjas.dojo_id = dojos.id  WHERE dojos.id = %(id)s"
        results = connectToMySQL(DATABASE).query_db(query, data)
        dojo = cls(results[0])
        for result in results:
            print(result)
            this_users = {
                "id": result["ninjas.id"],
                "first_name": result["first_name"],
                "last_name": result["last_name"],
                "age": result["age"],
                "created_at": result["ninjas.created_at"],
                "updated_at": result["ninjas.updated_at"],
                "dojo_id": result["dojo_id"],
            }
            dojo.ninjas.append(ninja.Users(this_users))
        return dojo

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(DATABASE).query_db(query)
        dojos = []
        for result in results:
            dojos.append(cls(result))
        return dojos

    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name , created_at, updated_at ) VALUES ( %(name)s , NOW() , NOW() );"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def show(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        dojo = cls(result[0])
        return dojo

    @classmethod
    def get_id(cls, data):
        result = []
        query = "SELECT id FROM dojos WHERE title = %(first_name)s AND last_name = %(last_name)s"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result[0]['id']

    @classmethod
    def update(cls, data):
        query = "UPDATE dojos SET first_name = %(first_name)s, last_name = %(last_name)s, age = %(age)s, updated_at = NOW(), WHERE id= %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM dojos WHERE id = %(id)s"
        return connectToMySQL(DATABASE).query_db(query, data)
