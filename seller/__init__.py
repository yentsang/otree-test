from otree.api import *
import random


class Constants(BaseConstants):

    name_in_url = 'seller'
    players_per_group = 2
    num_rounds = 6
    cenario_part_1 = 2
    cenario_part_2 = 4
    p1_role = 'Buyer'
    p2_role = 'Provider'

    
class Subsession(BaseSubsession):
    
    cenario = models.FloatField()

    def creating_session(subsession):

        subsession.cenario = random.randint(1, 2)

        print(subsession.cenario)

class Player(BasePlayer):
    pass

class Group(BaseGroup):
    
    decision_buyer = models.IntegerField(
        choices=[
            [1, 'Partnership'],
            [0, 'Arm-Lenght'],
        ]
    )

    decision_provider = models.IntegerField(
        choices=[
            [1, 'Partnership'],
            [0, 'Arm-Lenght'],
        ]
    )


def set_payoffs(group: Group):

    p1 = group.get_player_by_role(Constants.p1_role)
    p2 = group.get_player_by_role(Constants.p2_role)

    for p in [p1, p2]:
        if group.decision_buyer == 1 and group.decision_provider == 1:
            p.payoff += 100
        elif group.decision_buyer == 0 and group.decision_provider == 0:
            p.payoff += 60
        elif group.decision_buyer == 1 and group.decision_provider == 0:
            if p == p1:
                p.payoff += 30
            elif p == p2:
                p.payoff += 120
        elif group.decision_buyer == 0 and group.decision_provider == 1:
            if p == p1:
                p.payoff += 120
            elif p == p2:
                p.payoff += 30


class PageBuyer(Page):

    form_model = 'group'
    form_fields = ['decision_buyer']

    @staticmethod
    def is_displayed(player):
        return player.round_number <= Constants.cenario_part_1 and player.role == 'Buyer'

class PageProvider(Page):

    form_model = 'group'
    form_fields = ['decision_provider']

    @staticmethod
    def is_displayed(player):
        return player.round_number <= Constants.cenario_part_1 and player.role == 'Provider'

class ControlWaitPage(WaitPage):
    
    after_all_players_arrive = set_payoffs

    @staticmethod
    def is_displayed(player):
        return player.round_number <= Constants.cenario_part_1

class PageCenarioBuyer_1(Page):

    form_model = 'group'
    form_fields = ['decision_buyer']

    @staticmethod
    def is_displayed(player):
        return (player.round_number > Constants.cenario_part_1 and player.round_number <= Constants.cenario_part_2) and player.role == 'Buyer'

class PageCenarioProvider_1(Page):

    form_model = 'group'
    form_fields = ['decision_provider']

    @staticmethod
    def is_displayed(player):
        return (player.round_number > Constants.cenario_part_1 and player.round_number <= Constants.cenario_part_2) and player.role == 'Provider'

class CenarioWaitPage_1(WaitPage):
    
    after_all_players_arrive = set_payoffs

    @staticmethod
    def is_displayed(player):
        return (player.round_number > Constants.cenario_part_1 and player.round_number <= Constants.cenario_part_2)

## Cenario 2
class PageCenarioBuyer_2(Page):

    form_model = 'group'
    form_fields = ['decision_buyer']

    @staticmethod
    def is_displayed(player):
        return player.round_number > Constants.cenario_part_2 and player.role == 'Buyer'

class PageCenarioProvider_2(Page):

    form_model = 'group'
    form_fields = ['decision_provider']

    @staticmethod
    def is_displayed(player):
        return player.round_number > Constants.cenario_part_2 and player.role == 'Provider'

class CenarioWaitPage_2(WaitPage):
    
    after_all_players_arrive = set_payoffs

    @staticmethod
    def is_displayed(player):
        return player.round_number > Constants.cenario_part_2


page_sequence = [PageBuyer, PageProvider, ControlWaitPage,
                 PageCenarioBuyer_1, PageCenarioProvider_1, CenarioWaitPage_1,
                 PageCenarioBuyer_2, PageCenarioProvider_2, CenarioWaitPage_2]