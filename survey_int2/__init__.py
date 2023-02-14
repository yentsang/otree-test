from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'survey_int2'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    trust_1 = models.StringField(
        choices=[['1', '1'], ['2', '2'], ['3', '3'], ['4', '4'], ['5', '5']],
        label = 'Quao confiável foi o(a) outro(a) participante ao longo do jogo? (1=extremamente não confiável; 5=extremamente confiável)',
        widget=widgets.RadioSelect
    )
    opportunism_1 = models.StringField(
        choices=[['1', '1'], ['2', '2'], ['3', '3'], ['4', '4'], ['5', '5']],
        label='Quao oportunista foi o(a) outro(a) participante ao longo do jogo? (1=extremamente altruísta; 5=extremamente oportunista)',
        widget=widgets.RadioSelect
    )
    colaboration_1 = models.StringField(
        choices=[['1', '1'], ['2', '2'], ['3', '3'], ['4', '4'], ['5', '5']],
        label='Quao colaborativo foi o(a) outro(a) participante ao longo do jogo? (1=extremamente não colaboritvo; 5=extremamente colaborativo)',
        widget=widgets.RadioSelect
    )
    colaboration_2 = models.StringField(
    choices=[['1', '1'], ['2', '2'], ['3', '3'], ['4', '4'], ['5', '5']],
    label='Quao colaborativo foi você em relação ao(a) outro(a) participante ao longo do jogo? (1=extremamente não colaboritvo; 5=extremamente colaborativo)',
    widget=widgets.RadioSelect
    )



# FUNCTIONS
# PAGES
class Percepcao(Page):
    form_model = 'player'
    form_fields = ['trust_1', 'opportunism_1', 'colaboration_1', 'colaboration_2']

page_sequence = [Percepcao]
