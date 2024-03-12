#!/usr/bin/python3
"""
Entry point of the command interpreter.
"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        print("")
        return True

    def emptyline(self):
        """An empty line + ENTER shouldn’t execute anything."""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it, prints the id."""
        if not arg:
            print("** class name missing **")
            return
        try:
            if arg in HBNBCommand.class_dict:
                obj = HBNBCommand.class_dict[arg]()
                obj.save()
                print(obj.id)
            else:
                print("** class doesn't exist **")
        except Exception as e:
            print(e)

    def do_show(self, arg):
        """Shows an instance based on class name and id."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1 or not args[1]:
            print("** instance id missing **")
            return
        if args[0] in HBNBCommand.class_dict:
            all_objs = storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key in all_objs:
                print(all_objs[key])
            else:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on class name and id."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1 or not args[1]:
            print("** instance id missing **")
            return
        if args[0] in HBNBCommand.class_dict:
            all_objs = storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key in all_objs:
                del all_objs[key]
                storage.save()
            else:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints all string rep of all inst based or not on class name."""
        args = arg.split()
        obj_list = []
        for obj in storage.all().values():
            if not arg or args[0] == obj.__class__.__name__:
                obj_list.append(obj.__str__())
        if obj_list:
            print(obj_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates inst based on class name and id by add or updating attr."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        if args[0] in HBNBCommand.class_dict:
            all_objs = storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key in all_objs:
                obj = all_objs[key]
                setattr(obj, args[2], args[3])
                obj.save()
            else:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")

    class_dict = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review
    }


if __name__ == '__main__':
    HBNBCommand().cmdloop()
