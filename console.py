#!/usr/bin/python3
"""Command interpreter for the AirBnB clone project."""

import cmd
import re
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command interpreter class."""

    prompt = "(hbnb) "
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def do_quit(self, line):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, line):
        """EOF signal to exit the program."""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty line."""
        pass

    def do_create(self, line):
        """Create a new instance of a class."""
        if not line:
            print("** class name missing **")
        elif line not in self.classes:
            print("** class doesn't exist **")
        else:
            obj = self.classes[line]()
            obj.save()
            print(obj.id)

    def do_show(self, line):
        """Show an instance based on class name and id."""
        if not line:
            print("** class name missing **")
        else:
            args = line.split()
            if args[0] not in self.classes:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, line):
        """Destroy an instance based on class name and id."""
        if not line:
            print("** class name missing **")
        else:
            args = line.split()
            if args[0] not in self.classes:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, line):
        """Show all instances based on class name (optional)."""
        if not line:
            print([str(obj) for obj in storage.all().values()])
        elif line not in self.classes:
            print("** class doesn't exist **")
        else:
            print([str(obj) for obj in storage.all().values() if obj.__class__.__name__ == line])

    def do_update(self, line):
        """Update an instance based on class name and id."""
        if not line:
            print("** class name missing **")
        else:
            args = line.split()
            if args[0] not in self.classes:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
                if key not in storage.all():
                    print("** no instance found **")
                elif len(args) < 3:
                    print("** attribute name missing **")
                elif len(args) < 4:
                    print("** value missing **")
                else:
                    obj = storage.all()[key]
                    setattr(obj, args[2], args[3])
                    obj.save()

    def default(self, line):
        """Default behavior for unknown commands."""
        match = re.search(r"^(\w+)\.(\w+)(?:\(([^)]*)\))$", line)
        if not match:
            super().default(line)
            return

        class_name, method, args = match.groups()
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        if method == "all":
            self.do_all(class_name)
        elif method == "count":
            count = sum(1 for obj in storage.all().values() if obj.__class__.__name__ == class_name)
            print(count)
        elif method == "show":
            self.do_show("{} {}".format(class_name, args))
        elif method == "destroy":
            self.do_destroy("{} {}".format(class_name, args))
        elif method == "update":
            match = re.search(r"^(\S+)\s+(\S+)\s+(\S+)$", args)
            if match:
                obj_id, attr_name, attr_value = match.groups()
                self.do_update("{} {} {} {}".format(class_name, obj_id, attr_name, attr_value))
            else:
                print("** invalid syntax **")
        else:
            print("** invalid command **")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
