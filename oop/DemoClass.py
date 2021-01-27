class Demo():
    def __init__(self,type,valid):
        self.type=type
        self.valid=valid


demo=Demo("sample",True)
print(f"{demo} {demo.type} {demo.valid}")