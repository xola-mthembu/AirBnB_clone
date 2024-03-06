# AirBnB Clone - The Console

## Description

This group project is part of the AirBnB Clone; the first step towards building a full web application: the console.
It is a command interpreter to manage your AirBnB objects.

## Command Interpreter

### How to start it:

1. Clone the repository: `git clone [https://github.com/SIHLE-MTSHALI/AirBnB_clone.git]`
2. Navigate to the project directory: `cd AirBnB_clone`
3. Run the console (interactive mode): `./console.py`
4. Or run the console (non-interactive mode): `echo "[command]" | ./console.py`

### How to use it:

You can use the console to manage the objects of your application:

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database, etc.
- Do operations on objects (count, compute stats, etc.)
- Update attributes of an object
- Destroy an object

### Examples:

```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) create BaseModel
1234-1234-1234
(hbnb) quit
$
