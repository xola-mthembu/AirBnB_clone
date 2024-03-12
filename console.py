#!/usr/bin/python3
"""
Console module.
"""
import cmd
from models import storage, BaseModel,
User, State, City, Amenity, Place, Review


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    class_dict = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        print("")
        return True

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it, and prints the id."""
        if not arg:
            print("** class name missing **")
            return
        if arg in HBNBCommand.class_dict:
            instance = HBNBCommand.class_dict[arg]()
            instance.save()
            print(instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance."""
        # similar logic for 'show' command
        # ...

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        # similar logic for 'destroy' command
        # ...

    def do_all(self, arg):
        """Prints all string representation of all instances."""
        # similar logic for 'all' command
        # ...

    def do_update(self, arg):
        """Updates an instance based on the class name and id."""
        # similar logic for 'update' command
        # ...


if __name__ == '__main__':
    HBNBCommand().cmdloop()
