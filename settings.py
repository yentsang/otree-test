import random
from os import environ


SESSION_CONFIGS = [
    # dict(
    #    name='control',
    #    display_name="Cenario controle",
    #    app_sequence=['control', 'survey'],
    #    num_demo_participants=2,
    #    time_pressure = True,
    # ),
    #  dict(
    #     name='jogo',
    #     display_name = "jogo1",
    #     app_sequence=['control','survey_int', 'cenario1','survey_int2', 'cenario2_adapt', 'survey'],
    #     num_demo_participants=2,
    #     time_pressure = True,
    #  ),
    # dict(
    #    name='jogo2',
    #    display_name="jogo2",
    #    app_sequence=['control', 'survey_int', 'cenario2', 'survey_int2', 'cenario1_adapt', 'survey'],
    #    num_demo_participants=2,
    # ),
    # dict(
    #    name='jogo3',
    #    display_name="jogo3",
    #    app_sequence=['control', 'survey_int', 'cenario3', 'survey_int2', 'cenario4_adapt', 'survey'],
    #    num_demo_participants=2,
    # ),
    # dict(
    #    name='jogo4',
    #    display_name="jogo4",
    #    app_sequence=['control', 'survey_int', 'cenario4', 'survey_int2', 'cenario3_adapt', 'survey'],
    #    num_demo_participants=2,
    # ),
    dict(
       name='teste',
       display_name="Cenario controle",
       app_sequence=['prisoner', 'survey'],
       num_demo_participants=2,
       time_pressure = True,
    ),

]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=8.00, doc=""
)

PARTICIPANT_FIELDS = [ ]
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = False

ROOMS = [
    dict(
        name='controle_cenario1_cenario2_adapt',
        display_name='jogo1',
        participant_label_file='_rooms/Jogo_Experimento.txt',
        use_secure_urls=True
    ),
    dict(
        name='controle_cenario2_cenario1_adapt',
        display_name='jogo2',
        participant_label_file='_rooms/Jogo_Experimento.txt',
        use_secure_urls=True
    ),
    dict(
        name='controle_cenario3_cenario4_adapt',
        display_name='jogo3',
        participant_label_file='_rooms/Jogo_Experimento.txt',
        use_secure_urls=True
    ),
    dict(
        name='controle_cenario4_cenario3_adapt',
        display_name='jogo4',
        participant_label_file='_rooms/Jogo_Experimento.txt',
        use_secure_urls=True
    ),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""


SECRET_KEY = '6283546717038'

INSTALLED_APPS = ['otree']
