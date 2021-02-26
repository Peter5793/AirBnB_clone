#!/usr/bin/python3
"""
Console entry point for command line interpreter
"""
import cmd
from models.base_model import BaseModel
import models


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"

    def do_quit(self, line):
        """ Quit command to exit the program
        """
        return True
    
    def do_EOF(self, line):
        """ Exit clearly at the end of file
        """

    def emptyline(self):
        """Empty line that does nothing"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
