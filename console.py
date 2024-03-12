#!/usr/bin/python3
"""
Entry point of the command interpreter.
"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User  # Import the User class


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
        """Create a new instance, save it, and print the id."""
        if not arg:
            print("** class name missing **")
            return
        try:
            if arg not in ['BaseModel', 'User']:
                print("** class doesn't exist **")
                return
            new_instance = eval(f"{arg}()")
            new_instance.save()
            print(new_instance.id)
        except Exception as e:
            print(e)

    def do_show(self, arg):
        """Show an instance based on class name and id."""
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
        """Delete an instance based on class name and id."""
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
        """Print instances based on class name or not."""
        args = arg.split()
        all_objs = storage.all()
        class_names = [cls.__name__ for cls in BaseModel.__subclasses__()]
        class_names += ['BaseModel', 'User']
        if not arg or args[0] in class_names:
            filtered_objs = [str(obj) for obj in all_objs.values()
                             if not arg or type(obj).__name__ == args[0]]
            print(filtered_objs)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Update an instance based on class name and id."""
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
