import Gamer


class User(Gamer):
    def __init__(self):
        self._chip_choice = None  # 선택한 코인
        self._balance = self.INIT_MONEY  # 가진 금액
        self._money_status = True

    def new_game(self):
        self._chip_choice = None  # 선택한 코인
        self._balance = self.INIT_MONEY  # 가진 금액
        self._money_status = True
        super().new_hand()

# properties

    @property
    def chip_choice(self):
        return self._chip_choice

    @chip_choice.setter
    def chip_choice(self, new_chip_choice):
        self._chip_choice = new_chip_choice

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, new_balance):
        self._balance = new_balance
