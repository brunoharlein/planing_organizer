# coding: utf-8
from .connection import connection
from .entities.conference import Conference
from .entities.speaker import Speaker

class conferenceModel():
    """Class to perform all queries related to the conference table in the database"""

    def __init__(self):
        # Create a instance of the connection class to acces the database
        self.db = connection()

    def get_conferences(self):
        # the query to execute
        sql ="""select * from conference as c
                inner join speaker as s
                on s.id = c.speaker_id
                order by c.event_date, c.event_time"""
        conferences = self.db.make_request(sql)
        # turn the list of lists returned by the database into a list of objects
        # For each list representing a speaker and a conference
        for key, value in enumerate(conferences):
            # instanciate a speaker and a conference
            speaker = Speaker(value)
            conference = Conference(value)
            # Set the right id, otherwise the conference takes the speaker id
            # NB: this is an ugly solution but it avoids complicating the correction too much
            conference.id = value[0]
            # set the speaker object in the conference object
            conference.speaker = speaker
            # replace the list by the object in the list of conferences
            conferences[key] = conference
        return conferences

    def add_conference(self, conference):
        # the query to execute
        sql = """insert into conference(title, summary, event_date, registering_date, event_time, speaker_id)
                 values(%s, %s, %s, now(), %s, %s)"""
        arguments = (conference.title, conference.summary, conference.event_date, conference.event_time, conference.speaker)
        message=  "Nous n'avons pas pu enregistrer la conférence, un problème est survenu"
        return self.db.make_request(sql, arguments=arguments, message=message)

    def delete_conference(self, id):
        # the query to execute
        sql = """delete from conference
                 where id = %s"""
        arguments = (id,)
        message = "Un problème est survenu, nous n'arrivons pas à supprimer la conférence d'id {}".format(id)
        return self.db.make_request(sql, arguments=arguments, message=message)
