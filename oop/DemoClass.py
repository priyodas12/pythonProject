class Demo():
    # CLASS object attributes:
    amount = 100
    fixed_rate = 182.56

    # constructor of class
    def __init__(self, type, valid):
        # attribute we take in the argument
        # actual attribute assignment done here:
        self.mytype = type
        self.validity = valid

    # Operation/ Actions --> Methods
    def calculate_interest(self):
        print(f" Calculated Interest:: {self.amount*self.fixed_rate}")


demo = Demo(type="special",valid=True)

print(f"{demo} {demo.mytype} {demo.validity} {demo.amount} {demo.fixed_rate}")
demo.calculate_interest()
