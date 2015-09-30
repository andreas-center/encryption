class setColor:
    def red(self,name):
        return "\033[91m" + name
    def white(self,name):
        return "\033[0m" + name
    def green(self,name):
        return "\033[92m" + name
    def yellow(self,name):
        return "\033[93m" + name + "\033[0m"
setColor = setColor()
