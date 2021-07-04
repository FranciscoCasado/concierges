class Match:
    """ """
    def __init__(self):
        self._players = []
        self._decks = []
        self._dices = []
        self._building = []
        self._turn_count = 0
        self._turn_actions = {}

        def current_turn(self):
            return self._turn_count

        def __increment_turn_count(self):
            self._turn_count +=1
        
        def new_turn(self, player):
            self.__increment_turn_count()
            floor = player.roll_floor_dice()
            card = player.draw_card_from_deck(floor.deck_type)
            dice_choice = player.decide_what_to_do(card.choices)
            result = player.roll_chance_dice(dice_choice)
            player.earn_reward_and_curse(result)
            self.aplly_card_effects()
            # end turn








