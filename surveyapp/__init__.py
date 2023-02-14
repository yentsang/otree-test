from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'surveyapp'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    age = models.IntegerField(label="please enter your age")
    gender = models.StringField(label="please choose your gender",
                                choices=["male","female","other", "prefer not top say"]
                                )
    is_lefthanded = models.BooleanField(label="are you left handed",
                                        choices= [
                                            [True,"yes"],
                                            [False,"no"]
                                        ])



# PAGES
class SurveyQuestions(Page):
    form_model = "player"
    form_fields = ["age","gender","is_lefthanded"]


page_sequence = [SurveyQuestions,]
