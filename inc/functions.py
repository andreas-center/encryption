class Lines:
    def message(self,value):
        return "_".rjust(7) + "\n" + "".ljust(5) + "[\033[91m*\033[0m] ".ljust(15) + value
    def question(self,value):
        return "_".rjust(7) + "\n" + "".ljust(5) + "[\033[91m?\033[0m] ".ljust(15) + value
    def exclamation(self,value):
        return "_".rjust(7) + "\n" + "".ljust(5) + "[\033[91m!\033[0m] ".ljust(15) + value

lines = Lines()
