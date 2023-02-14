from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'prisoners_dilemma_simple'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 5
    payoff_both_cooperate = 0.5
    payoff_both_defect = 0.3
    payoff_cooperate_defect_high = 0.75
    payoff_cooperate_defect_low = 0.2



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    defect = models.BooleanField(
        label="Please choose if you want to cooperate or defect",
        choices=[
            [True, "Defect"],
            [False, "Cooperate"],
        ]
    )
    quantity = models.IntegerField(
        label="Please enter the quantity to purchase"
    )

# FUNCTIONS
def other_player(player: Player):
    return player.get_others_in_group()[0]


# PAGES
class MyPage(Page):
    form_model = "player"
    form_fields = ["defect","quantity",]

    @staticmethod
    def is_displayed(player):
        return player.id_in_group == 1

class MyPage2(Page):
    @staticmethod
    def after_all_players_arrive(group: Group):
        player_lists = group.get_players()
        player_1 = player_lists[0]
        player_2 = player_lists[1]
        return dict(
            pedido = player_2.id_in_group
        )

    form_model = "player"
    form_fields = ["defect",]

    @staticmethod
    def is_displayed(player):
        return player.id_in_group == 2

class ResultsWaitPage(WaitPage):
    @staticmethod
    def after_all_players_arrive(group: Group):
        player_lists = group.get_players()
        player_1 = player_lists[0]
        player_2 = player_lists[1]
        if player_1.defect:
            if player_2.defect:
                player_1.payoff = C.payoff_both_defect
                player_2.payoff = C.payoff_both_defect

            else:
                player_1.payoff = C.payoff_cooperate_defect_high
                player_2.payoff = C.payoff_cooperate_defect_low
        else:
            if player_2.defect:
                player_1.payoff = C.payoff_cooperate_defect_low
                player_2.payoff = C.payoff_cooperate_defect_high
            else:
                player_1.payoff = C.payoff_both_cooperate
                player_2.payoff = C.payoff_both_cooperate


class Results(Page):

    @staticmethod
    def vars_for_template(player: Player):
        opponent = other_player(player)
        return dict(
            same_choice=player.defect == opponent.defect,
            my_choice=player.field_display('defect'),
            opponent_choice=opponent.field_display('defect'),
        )


page_sequence = [MyPage, MyPage2, ResultsWaitPage, Results]
