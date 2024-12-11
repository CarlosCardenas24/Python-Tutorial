from bank_accounts import *

Carlos = BankAccount(1000, "Carlos")
Lola = BankAccount(2000, "Lola")

Carlos.getBalance()
Lola.getBalance()

Lola.deposit(500)

Carlos.withdraw(10000)
Carlos.withdraw(10)

Carlos.transfer(10000, Lola)
Carlos.transfer(100, Lola)

Nala = InterestRewardsAcct(1000, "Nala")

Nala.getBalance()

Nala.deposit(100)

Nala.transfer(100, Carlos)

Jasmine = SavingsAcct(1000, "Jasmine")

Jasmine.getBalance()

Jasmine.deposit(100)

Jasmine.transfer(10000, Lola)
Jasmine.transfer(1000, Lola)