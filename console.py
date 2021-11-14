#!/usr/bin/python3
import cmd
import sys
from datetime import datetime
from models.base_model import BaseModel
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.user import User
import models

allowed_class = {"BaseModel": BaseModel, "Place": Place, "State": State,
                 "City": City, "Amenity": Amenity, "Review": Review,
                 "User": User}


class HBNBCommand(cmd.Cmd):

    intro = 'Welcome to the AirBnB clone. Type help or ? to list commands. \n'
    prompt = '(hbnb) '
    file = None

    def do_create(self, arg):
        """Create a new instance of BaseModel, saves it and prints the id"""
        if len(arg) == 0:
            print("** class name missing **")
            return
        else:
            try:
                string = arg + "()"
                instance = eval(string)
                print(instance.id)
                instance.save()
            except Exception as f:
                print("** class doesn't exist **")

    def do_EOF(self, arg):
        'Check if it is End-Of-File: EOF'
        # something to be done here
        return True

    def do_quit(self, arg):
        'close the Airbnb window, and exit:  EXIT'
        print('Thank you for AirBnB clone shell;-)')
        self.close()
        # bye()
        return True

    def do_show(self, arg):
        """Prints the string representation of an instance
            based on the class name and id."""
        cmd_line = arg.split()
        if len(cmd_line) == 0:
            print("** class name missing **")
            return
        elif cmd_line[0] not in allowed_class.keys():
            print("** class doesn't exist **")
        elif len(cmd_line) == 1:
            print("** instance id missing **")
        elif len(cmd_line) == 2:
            instance = cmd_line[0] + "." + cmd_line[1]
            if instance in models.storage.all():
                print(models.storage.all()[instance])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and
        id (save the change into the JSON file)."""
        cmd_line = arg.split()
        if len(cmd_line) == 0:
            print("** class name missing **")
            return
        elif cmd_line[0] not in allowed_class.keys():
            print("** class doesn't exist **")
        elif len(cmd_line) == 1:
            print("** instance id missing **")
        elif len(cmd_line) == 2:
            instance = cmd_line[0] + "." + cmd_line[1]
            if instance in models.storage.all():
                del models.storage.all()[instance]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances
            based or not on the class name."""
        cmd_line = arg.split()
        if len(cmd_line) == 0 or cmd_line[0] == "BaseModel":
            print('["', end="")
            flag = 0
            for obj_id in models.storage.all().keys():
                if flag == 1:
                    print('", "', end="")
                obj = models.storage.all()[obj_id]
                print(obj, end="")
                flag = 1
            print('"]')
        elif cmd_line[0] not in allowed_class.keys():
            print("** class doesn't exist **")
        else:
            print('["', end="")
            # result = []
            flag = 0
            len_class = len(cmd_line[0])
            for obj_id in models.storage.all().keys():
                if obj_id[:len_class] == cmd_line[0]:
                    if flag == 1:
                        print('", "', end="")
                    obj = models.storage.all()[obj_id]
                    print(obj, end="")
                    flag = 1
            print('"]')

    def do_update(self, line):
        """Updates an instance based on the class name and id
            by adding or updating attribute"""
        cmd_line = line.split()
        untouchable = ["id", "created_at", "updated_at"]
        objets = models.storage.all()
        if not line:
            print("** class name missing **")
        elif cmd_line[0] not in allowed_class.keys():
            print("** class doesn't exist **")
        elif len(cmd_line) == 1:
            print("** instance id missing **")
        else:
            instance = cmd_line[0] + "." + cmd_line[1]
            if instance not in models.storage.all():
                print("** no instance found **")
            elif len(cmd_line) < 3:
                print("** attribute name missing **")
            elif len(cmd_line) < 4:
                print("** value missing **")
            elif cmd_line[2] not in untouchable:
                ojb = objets[instance]
                ojb.__dict__[cmd_line[2]] = cmd_line[3]
                ojb.updated_at = datetime.now()
                ojb.save()

    def do_count(self, arg):
        "count instances of the class"

        cmd_line = arg.split()

        if cmd_line[0] not in allowed_class:
            return
        else:
            counter = 0
            keys_list = models.storage.all().keys()
            for search in keys_list:
                len_search = len(cmd_line[0])
                if search[:len_search] == cmd_line[0]:
                    counter += 1
                    # print(search)
            print(counter)

    def close(self):
        if self.file:
            self.file.close()
            self.file = None

if __name__ == '__main__':
    HBNBCommand().cmdloop()
