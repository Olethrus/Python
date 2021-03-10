# This will import a function from a root level .py file
from mymodule import my_func
my_func()
#This will dig into a directory and pull a .py file as long as there is a __init__.py file in there
from Main_Package import Main_Script_1 # This pulls a root level .py file
from Main_Package.Sub_Package import Sub_Script_1 # This will pull a file one level in Main_Package.Sub_Packagae = <MainFolder>.<SubFolder> repeat this as many sub folders as you have
Main_Script_1.main_report()
Sub_Script_1.sub_report()
