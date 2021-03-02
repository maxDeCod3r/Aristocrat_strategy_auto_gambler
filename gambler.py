from selenium import webdriver
import time

class Gambler:
    def __init__(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('https://bananobet.com/')

    def start(self) -> None:
        self.bet_amount = self.driver.find_element_by_id('bet_amount')
        self.bet_button = self.driver.find_element_by_id('betSubmit')
        self.user_balance = self.driver.find_element_by_id('userBalance')

    def set_bet(self, amount: float = 0.1) -> None:
        self.bet_amount.clear()
        self.bet_amount.send_keys(str(amount))

    def make_bet(self, amount: float = 0.1) -> None:
        prev_balance = float(self.user_balance.text)
        if prev_balance < amount:
            raise ValueError("Balance too low!!!")
        if prev_balance < amount * 8: # TODO: tweak the 8 to represent an accurate safety net
            print(f"Screw that, accepting loss of {amount*2}")
            return
        self.set_bet(amount)
        self.bet_button.click()
        time.sleep(1)
        if float(self.user_balance.text) > prev_balance:
            return
        else:
            self.make_bet(amount*2)

    def keep_make_bet(self, amount: float = 0.1) -> None:
        while True:
            self.make_bet(amount)


# if __name__ == "__main__":
#     g = Gambler()
#     a = input('Ready?')
#     g.make_bet()
