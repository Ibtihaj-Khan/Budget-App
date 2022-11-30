class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = list()

    def deposit(self, amount, desc=""):
        self.ledger.append({"amount": amount, "description": desc})

    def withdraw(self, amount, desc=""):
        if not self.check_funds(amount):
            return False
        else:
            self.ledger.append({"amount": -abs(amount), "description": desc})
            return True

    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance+=float(item["amount"])
        return balance

    def check_funds(self, amount):
        balance = 0
        for item in self.ledger:
            balance+=float(item["amount"])

        if float(amount) > balance:
            return False
        elif float(amount) <= balance:
            return True
    
    def transfer(self, amount, object):
        if self.withdraw(amount, "Transfer to {}".format(object.category)):
            object.deposit(amount, "Transfer from {}".format(self.category))
            return True
        else:
            return False

    def __str__(self):
        total = 0
        output = self.category.center(30,'*') + '\n'
        for item in self.ledger:
            output += item["description"][:23].ljust(23)
            total += item["amount"]
            output += str("{:.2f}".format(item["amount"]))[:7].rjust(7)
            output += '\n'
        output += "Total: {}".format(total)
        return output


def create_spend_chart(categories):
  output = "Percentage spent by category\n"

  total = 0
  expenses = []
  names = []
  length = 0

  for item in categories:
    expense = sum([-x["amount"] for x in item.ledger if x["amount"] < 0])
    total += expense

    if len(item.category) > length:
      length = len(item.category)

    expenses.append(expense)
    names.append(item.category)

  expenses = [(x/total)*100 for x in expenses]
  names = [label.ljust(length, " ") for label in names]

  for c in range(100,-1,-10):
    output += str(c).rjust(3, " ") + "|"
    for x in expenses:
      output += " o " if x >= c else "   "
    output += " \n"

  output += "    " + "---"*len(names) + "-\n"

  for i in range(length):
    output += "    "
    for label in names:
      output += " " + label[i] + " "
    output += " \n"

  return output.strip("\n")
