#!/usr/bin/python3
"""
Entry point of the command interpreter.
"""
import cmd
from models import storage
from models.base_model import BaseModel


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
            new_instance = eval(f"{arg}()")
            new_instance.save()
            print(new_instance.id)
        except Exception:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Shows an instance based on class name and id."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        all_objs = storage.all()
        key = f"{args[0]}.{args[1]}"
        if key in all_objs:
            print(all_objs[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on class name and id."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        all_objs = storage.all()
        key = f"{args[0]}.{args[1]}"
        if key in all_objs:
            del all_objs[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all instances based or not on the class name."""
        args = arg.split()
        all_objs = storage.all()
        class_names = [cls.__name__ for cls in BaseModel.__subclasses__()]
        class_names.append('BaseModel')
        if not arg or args[0] in class_names:
            print([str(obj) for obj in all_objs.values()])
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on class name and id."""
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
        all_objs = storage.all()
        key = f"{args[0]}.{args[1]}"
        if key in all_objs:
            setattr(all_objs[key], args[2], args[3])
            all_objs[key].save()
        else:
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
