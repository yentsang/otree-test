from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    nome = models.StringField(label='Qual é o seu nome?')
    age = models.IntegerField(label='Qual a sua idade?', min=13, max=125)
    experience = models.IntegerField(label="Quantos anos de experiencia profissional você possui?", max=70)
    position = models.StringField(label='Qual é o seu cargo atual?')
    endereco = models.StringField(label='Qual é o seu e-mail?')
    educacao = models.StringField(
        choices=[['1o. grau completo', '1o. grau completo'], ['2o. grau completo', '2o. grau completo'],
                ['3o. grau incompleto', '3o. grau incompleto'],['3o. grau completo', '3o. grau completo'],
                ['mestrado incompleto', 'mestrado incompleto'],['mestrado completo', 'mestrado completo'],
                ['Doutorado incompleto', 'Doutorado incompleto'],['Doutorado completo', 'Doutorado completo'],
                ['Pós-doc incompleto', 'Pós-doc incompleto'], ['Pós-doc completo', 'Pós-doc completo']],
        label='qual o seu nivel educacional?',
        widget=widgets.RadioSelect,
    )
    gender = models.StringField(
        choices=[['Masculino', 'Masculino'], ['Feminino', 'Feminino'],['Prefiro não responder', 'Prefiro não responder']],
        label='qual o seu Genero?',
        widget=widgets.RadioSelect,
    )
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
class Demographics(Page):
    form_model = 'player'
    form_fields = ['nome', 'age', 'gender', 'experience', 'endereco', 'position', 'educacao']


class Percepcao(Page):
    form_model = 'player'
    form_fields = ['trust_1', 'opportunism_1', 'colaboration_1', 'colaboration_2']

class Agradecimento(Page):
    form_model = 'player'


page_sequence = [Percepcao, Demographics, Agradecimento]
