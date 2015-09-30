import os
import sys
class Output:
    def message(self,message):
        return "\n [*] - ".rjust(10) + message.ljust(10)
    def question(self,question):
        return "\n [?] - ".rjust(10) + question.ljust(10)
    def exclamation(self,exclamation):
        return "\n [!] - ".rjust(10) + exclamation.ljust(10)
    def null(self,osSystem):
        null = " > /dev/null"
        os.system(osSystem + null)
        print(osSystem)
    def line(self):
        return "\n------------------------------------------------------"
    def logo(self):
        return "                    _       _      _                  \n     /\            | |     | |    (_)                 \n    /  \   _ __ ___| |__   | |     _ _ __  _   ___  __\n   / /\ \ | '__/ __| '_ \  | |    | | '_ \| | | \ \/ /\n  / ____ \| | | (__| | | | | |____| | | | | |_| |>  < \n /_/    \_\_|  \___|_| |_| |______|_|_| |_|\__,_/_/\_\ \n"
output = Output()
