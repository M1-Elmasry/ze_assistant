#!/bin/python

import sys
import sqlite3
from actions import *
from exec import *

def main() -> None:

    con = sqlite3.connect("data.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS data(alias, commands)")

    argv = sys.argv[:]
    actions = {"add" : add, "remove" : remove, "list" : list,
               "browser_workspace" : workspace, "help" : help}


    if len(argv) > 2:
        print("invalid use too many arguments")

    elif len(argv) < 2:
        print("invalid use no arguments")

    else:
        if (argv[1] in actions.keys()):
            actions[argv[1]](argv, cur)

        elif (execute(argv[1], cur) == -1):
            print(f"unkown action or unknown alias \"{argv[1]}\"")
            print("\"ze list\"")
            actions['help'](argv, cur)

    con.commit()
    con.close()

if __name__ == "__main__":
    main()
