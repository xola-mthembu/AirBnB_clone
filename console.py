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

    def default(self, line):
        """Default behavior for <class name>.<command> format."""
        try:
            cls_name, command = line.split(".", 1)
            if command == "all()":
                self.do_all(cls_name)
            else:
                print("*** Unknown syntax:", line)
        except Exception as e:
            print(e)

    def do_all(self, arg):
        """Prints all instances based or not on the class name."""
        all_objs = storage.all()
        if not arg or arg in HBNBCommand.class_dict:
            filtered_objs = [str(obj) for obj in all_objs.values()
                             if not arg or type(obj).__name__ == arg]
            print(filtered_objs)
        else:
            print("** class doesn't exist **")

    # Include other command methods like do_create, do_show, etc.


# Dictionary to map class names to classes
HBNBCommand.class_dict = {
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
