#4
import utils

print(utils.currency_rates('USD'))
print(utils.currency_rates('EUR'))
print(utils.currency_rates('USD'))

#5
import sys
print(utils.currency_rates(sys.argv[1]))