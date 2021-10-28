import random


class LotoCard:
    def __init__(self, player_type):
        self.player_type = player_type
        self._card = [
            [],
            [],
            []
        ]
        self._MAX_NUMBER = 90
        self._MAX_NUMBER_IN_CARD = 15
        self._number_stroked = 0
        NEED_SPACES = 4
        NEED_NUMBERS = 5

        self._numbers = random.sample(range(1, self._MAX_NUMBER + 1), self._MAX_NUMBER_IN_CARD)

        for line in self._card:
            for _ in range(NEED_SPACES):
                line.append(' ')
            for _ in range(NEED_NUMBERS):
                line.append(self._numbers.pop())

        # [' ', ' ', ' ', ' ', 9, 5, 12, 65, 4]

        def check_sort_item(item):
            if isinstance(item, int):
                return item
            return random.randint(1, self._MAX_NUMBER)

        for index, line in enumerate(self._card):
            self._card[index] = sorted(line, key=check_sort_item)

        # [' ', ' ', ' ', 9, 5, 12, 65,' ',  4]
        # [' ', 4, ' ', 5, 9, ' ', 12, ' ',  ' ']


    def comp_card (self):
        print(f'-----карточка компьютера-------')
        print(str(f'{self._card[0]}\n{self._card[1]}\n{self._card[2]}').replace(',', '').replace('[', '').replace(']','').replace("'", ''))



l = LotoCard('компьютер')
l.comp_card()


