class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = list()
    
    def __str__(self):
        the_string = ''
        # first line is category name centered
        the_string += '*' * ((30 - len(self.category)) // 2)
        the_string += self.category
        the_string += '*' * (30 - len(the_string)) + '\n'
        
        # add a line for each entry in ledger
        for line in self.ledger:
            money_string = self._num_to_str(line['amount'])
            if len(money_string) < 7:
                money_string = ' '*(7 - len(money_string)) + money_string
            else:
                money_string = money_string[:7]
            if len(line['description']) < 23:
                the_string += line['description'] + ' '*(23 - len(line['description'])) + money_string + '\n'
            else:
                the_string += line['description'][:23] + money_string + '\n'

        the_string += f'Total: {self._num_to_str(self.get_balance())}'
        return the_string

    def deposit(self, amount, description = ''):
        self.ledger.append({'amount': amount, 'description': description})
    
    def withdraw(self, amount, description = ''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False

    def get_balance(self):
        return sum([line['amount'] for line in self.ledger])
    
    def transfer(self, amount, destination):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {destination.category}')
            destination.deposit(amount, f'Transfer from {self.category}')
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()
    
    def _num_to_str(self, amount):
        if abs(amount % 1) < 0.001:
            return f'{amount}.00'
        elif abs(amount % 0.1) < 0.001:
            return f'{amount}0'
        else:
            return str(amount)
    

def create_spend_chart(categories: list) -> str:
    spend_list = [];
    category_list = [category.category for category in categories]
    percent_bins = [10*i for i in range(11)]
    print_str = 'Percentage spent by category'

    for each_cat in categories:
        spend_list.append(-sum([line['amount'] for line in each_cat.ledger if line['amount'] < 0 ]))
    percent_list = [100*yo/sum(spend_list) for yo in spend_list]
    
    for a_bin in percent_bins[-1::-1]:
        print_str += '\n' + ' '*(3 - len(str(a_bin))) + f'{a_bin}| '
        for cat in percent_list:
            if cat >= a_bin:
                print_str += 'o  '
            else:
                print_str += '   '
    print_str += '\n    -' + '-'*len(percent_list)*3

    count = 0
    while count < max([len(i) for i in category_list]):
        print_str += '\n     '
        for yo in category_list:
            if count < len(yo):
                print_str += yo[count] + '  '
            else:
                print_str += '   '
        count += 1

    print(print_str)
    return print_str

bob = Category('Bob')
alice = Category('Alice')

alice.deposit(200, 'start')
bob.deposit(345, 'starter pack')
alice.withdraw(100, 'nah')
alice.transfer(38, bob)
bob.transfer(383, alice)

yo = create_spend_chart([alice, bob]) 