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
        """Default behavior for handling commands."""
        try:
            cls_name, command_str = line.split(".", 1)
            command, args = command_str.split("(", 1)
            args = args.strip(")")
            self.parse_command(cls_name, command, args)
        except Exception as e:
            print(e)

    def parse_command(self, cls_name, command, args):
        """Parse and execute the command from the default method."""
        if command == "all":
            self.do_all(cls_name)
        elif command == "count":
            self.count_instances(cls_name)
        elif command == "show" and args:
            arg_cleaned = args.replace('"', '')  # Removes double quotes
            self.do_show(f"{cls_name} {arg_cleaned}")
        else:
            print(f"*** Unknown syntax: {cls_name}.{command}({args})")

    def do_all(self, arg):
        """Prints all instances based or not on the class name."""
        all_objs = storage.all()
        if not arg or arg in HBNBCommand.class_dict:
            filtered_objs = [str(obj) for obj in all_objs.values()
                             if not arg or obj.__class__.__name__ == arg]
            print(filtered_objs)
        else:
            print("** class doesn't exist **")

    def count_instances(self, class_name):
        """Count instances of a class."""
        count = sum(1 for obj in storage.all().values()
                    if obj.__class__.__name__ == class_name)
        print(count)

    def do_show(self, arg):
        """Show an instance based on class name and id."""
        args = arg.split()
        if len(args) < 2:
            msg = "** instance id missing **" if len(args) == 1 else "** class name missing **"
            print(msg)
        elif args[0] in HBNBCommand.class_dict:
            self.show_instance(args)

    def show_instance(self, args):
        """Show an instance based on the provided arguments."""
        all_objs = storage.all()
        key = "{}.{}".format(args[0], args[1])
        if key in all_objs:
            print(all_objs[key])
        else:
            print("** no instance found **")


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
