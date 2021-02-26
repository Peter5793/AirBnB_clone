#!/usr/bin/python3
"""
Console entry point for command line interpreter
"""
import cmd
from models.base_model import BaseModel
import models
from models.user import User

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    cls_arr = {"BaseModel": BaseModel
                "User":User}

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

    def do_create(self, line):
        """creats an intance of a class BaseModel 
        and saves it to JSON file & prints id
        """
        if line:
            if line in HBNBCommand.cls_arr:
                class_to_ins = HBNBCommand.cls_arr.get(line)
                new_inst = class_to_ins()
                new_inst.save()
                print(new_inst.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, line):
        """Prints the STR representation of an instance """
        list_line = line.split(' ')
        if line == "":
            print("** class name missing **")
        elif list_line[0] not in HBNBCommand.cls_arr.keys():
            print("**class doesn't exist **")
        elif len(list_line) < 2:
            print("** instance id missing **")
        elif list_line[0] + '.' + list_line[1] not in\
                models.storage.all().keys():
            print("** no instance found **")
        else:
            obj = models.storage.all().get(list_line[0] + '.' + list_line[1])
            print(obj)

    def do_destroy(self, line):
        """ deletes an intance based on the class name and id 
        saves the changes into JSON file
        """
        list_line = line.split(' ')
        if line == "":
            print("** class name missing **")
        elif list_line[0] not in HBNBCommand.cls_arr.keys():
            print("**class doesn't exist **")
        elif len(list_line) < 2:
            print("** instance id missing **")
        elif list_line[0] + '.' + list_line[1] not in\
                models.storage.all().keys():
            print("** no instance found **")
        else:
            models.storage.all().pop(list_line[0] + '.' + list_line[1], None)
            models.storage.save()

    def do_all(self, line):
        """prints string represenation of all intances based or not
        class name
        """
        list_line = line.split(' ')
        string = ""
        list_all = []
        if line == "":
            for key, value in models.storage.all().items():
                string = str(value)
                list_all.append(string)
            print(list_all)
        elif list_line[0] not in HBNBCommand.cls_arr.keys():
            print("** class doesn't exist **")
        else:
            for key, value in models.storage.all().items():
                if value.__class__.__name__== list_line[0]:
                    string = str(value)
                    list_all.append(string)
            print(list_all)

    def do_update(self, line):
        """
        updates an intance attribute
        """
        list_line = line.split(' ')
        if line == "":
            print("** class name missing **")
        elif list_line[0] not in HBNBCommand.cls_arr.keys():
            print("** class doesn't exist **")
        elif len(list_line) < 2:
            print("** instnace id missing **")
        elif list_line[0] + '.' + list_line[1] not in \
                models.storage.all().keys():
            print("** no instance found **")
        elif len(list_line) < 3:
            print("** attribute name missing **")
        elif len(list_line) < 4:
            print("** value missing **")
        else:
            obj = models.storage.all().get(list_line[0] + '.' + list_line[1])
            setattr(obj, list_line[2], list_line[3][1: -1])
            obj.save()    


if __name__ == '__main__':
    HBNBCommand().cmdloop()
