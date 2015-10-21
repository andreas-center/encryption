import os
import sys
# ---------------------------------- #
class print_line:
    def message(self,value):
        return " \033[91m[\033[0m\033[92m*\033[0m\033[91m]\033[0m\033[93m %s \033[0m" % value
print_line = print_line()
# ---------------------------------- #
class system_output:
    def count(self,file):
        with open('db/%s' % file) as f:
            amount = sum(1 for _ in f)
            return amount

    def print_cmd(self,file):
        with open('db/%s' % file) as f:
            lines = f.readlines()
            return lines
system_output = system_output()
# ---------------------------------- #
encrypt_count = system_output.count('encrypt')
encrypt_print = system_output.print_cmd('encrypt')
filesystem_count = system_output.count('filesystem')
filesystem_print = system_output.print_cmd('filesystem')
base_count = system_output.count('base')
base_print = system_output.print_cmd('base')
edit_files_count = system_output.count('edit_files')
edit_files_print = system_output.print_cmd('edit_files')
# ---------------------------------- #
input(print_line.message("Press [ENTER] to setup the encryption "))
for x in range(0,encrypt_count):
    print(encrypt_print[x])
# ---------------------------------- #
input(print_line.message("Press [ENTER] to setup the filesystem "))
for x in range(0,filesystem_count):
    print(filesystem_print[x])
# ---------------------------------- #
input(print_line.message("Press [ENTER] to setup the base system "))
for x in range(0,base_count):
    print(base_print[x])
# ---------------------------------- #
input(print_line.message("Press [ENTER] to setup the files"))
for x in range(0,edit_files_count):
    print(edit_files_print[x])

