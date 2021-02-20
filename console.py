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
    
    def do_create(self, line):
        """ Creates an instance of class """
        if line:
            if line in HBNBCOmmand.cls_arr:
                class_to_ins = HBNBCommmand.cls_arr.get(line)
                new_inst = class_to_ins()
                new_inst.save()
                print(new_inst.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, line):
        """prints the STR represntation of an instance"""
        list_line = line.split(' ')
        if line == "":
            print("** class name missing **")
        elif list_line[0] not in HBNBCommand/cls_arr.keys():
            print("** class doesn't exist **")
        elif len(list_line) < 2:
            print("** instance id missing **")
        elif list_line[0] + '.' + list[1] not in \
                models.storage.all().keys():
            print("** no instance found **")
        else:
            obj = models.storage.all().get(list_line[0] + '.' + list_line[1])
            print(obj)

    def do_destroy(self, line):
        """deletes an isntance based on the class name and id"""
        list_line = line.split(' ')
        if line == "":
            print("** class name missing **")
        elif list_line[0] not in HBNBCommand.cls_arr.keys():
            print("** class doesn't exist **")
        elif len(list_line) < 2:
            print("** intance id missing **")
        elif list_line[0] + '.' + list_line[1] not in \
                models.storage.all().keys():
            print("** no instance found **")
        else:
            models.storage.all().pop(list_line[0] + '.' + list_line[1], None)
            models.storage.save()

    def do_all(self, line):
        """ Prints string rep of all instances based on the Class name"""
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
                if value.__class__.__name__ == list_line[0]:
                    string = str(value)
                    list_all.append(string)
            print(list_all)

    def do_updates(self, line):
        """ Updates an instance attribute"""
        list_line = line.split(' ')
        if line == "":
            print("** class name missing **")
        elif list_line[0] not in HBNBCommand.cls_arr.keys():
            print("** class doesn't exist **")
        elif len(list_line) < 2:
            print("** instance id missing **")
        elif list_line[0] + '.' + list_line[1] not in \
                 models.storage.all().keys():
             print("** no instance found **")
        elif len(list_line) < 3:
             print("** attribute name missing **")
        elif len(list_line) < 4:
             print("** value missing **")
        else:
             obj = models.storage.all().get(list_line[0] + '.' + list_line[1])
             setattr(obj, list_line[2], list_line[3][1:-1])
             obj.save()


    
if __name__ == '__main__':
    HBNBCommand().cmdloop()
