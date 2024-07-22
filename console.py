#!/usr/bin/python3
""" that contains the entry point of the command interpreter """
import cmd


class HBNBCommand(cmd.Cmd):
    """ my class definition """
    prompt = "(hbnb)"

    def do_quit(self,arg):
        """ to exit the program"""
        return True

    def help_quit(self, arg):
        """ (this action is provided by default) """
        print("Quit command to exit the program")

    def do_EOF(self, arg):
        """ end of file """
        print()
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()
