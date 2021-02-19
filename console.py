#!/usr/bin/python3
"""HBNB command class """
import cmd
import models
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'
    
    def default(self, line):
        """
        evaluate line
        """
        try:
            self.onecmd(eval(line))
        except:
            print("*** Unknown syntax : {}".format(line))

    def do_count(self, line):
        """counts the number of instances of a class """
        if line not in HBNBCommand.cls_arr.keys():
            print("** class doesn't exist **")
        else:
            _dict = models.storage.all()
            count = 0
            for key, value in _dict.items():
                if value.__class__.__name__== line:
                    count = count + 1
            print(count)

    def emptyline(self):
        """Empty line that does nothing"""
        pass

    def do_quit(self, line):
        """ Quit commnad to exit the program"""
        return True

    def do_EOF(self, line):
        """ Exit clearly at the end of File"""
        return True
    
if __name__ == '__main__':
    HBNBCommand().cmdloop()
