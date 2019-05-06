from Gamer import Gamer


class User(Gamer):
    def __init__(self):
        super().__init__()
        self._chip_choice = 0  # 선택한 코인
        self._balance = self.INIT_MONEY  # 가진 금액
        self._money_status = True
        self._play_status = 'st_hit'
        self.name = 'User'

    def new_game(self):
        self._chip_choice = 0  # 선택한 코인
        self._balance = self.INIT_MONEY  # 가진 금액
        self._money_status = True
        self.new_hand()

    # 잔고 확인
    def has_money(self):
        if self.balance < 100:
            self.money_status = False
            return False
        return True

    # 게임 가능 여부 확인
    def is_playable(self):
        if self.has_money() and self.play_status == 'st_stand':
            return True
        return False


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

    @property
    def money_status(self):
        return self._money_status

    @money_status.setter
    def money_status(self, new_money_status):
        self._money_status = new_money_status

    @property
    def play_status(self):
        return self._play_status

    @play_status.setter
    def play_status(self, new_play_status):
        self._play_status = new_play_status
