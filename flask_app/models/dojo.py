from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Dojo():
    
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_dojo_survey(cls,data):
        query = 'INSERT INTO dojos (name, location, language, comment) VALUES (%(name)s, %(location)s, %(language)s, %(comment)s);'
        new_survey_id = connectToMySQL('dojo_survey').query_db(query, data)
        return new_survey_id

    @classmethod
    def get_survey(cls):
        query = 'SELECT * FROM dojos;'
        results = connectToMySQL('dojo_survey').query_db(query)
        survey = Dojo(results[len(results)-1])
        return survey

    @staticmethod
    def validate_survey(info):
        is_valid = True
        if len(info['name'])< 3 or len(info['name'])> 45:
            flash ("Name must be between 3 and 45 characters long.")
            is_valid = False
        if len(info['location'])< 3 or len(info['location'])> 45:
            flash ("Location must be between 3 and 45 characters long.")
            is_valid = False
        if len(info['language'])< 2 or len(info['language'])> 45:
            flash ("Language must be between 3 and 45 characters long.")
            is_valid = False
        if len(info['comment']) > 255:
            flash ("Comment must not be longer than 255 characters.")
            is_valid = False
        return is_valid