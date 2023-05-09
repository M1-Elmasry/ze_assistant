#!/bin/python

import sys
import sqlite3
from actions import *
from exec import *

def main() -> None:
    
    home_dir = os.getenv("HOME")
    con = sqlite3.connect(f"{home_dir}/data.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS data(alias, commands)")

    argv = sys.argv[:]
    actions = {"add" : add, "remove" : remove, "list" : list,
               "browser_workspace" : workspace, "help" : help}

    if len(argv) < 2:
        print("invalid use no arguments")
        actions['help'](argv, cur)

    else:
        if (argv[1] in actions.keys()):
            actions[argv[1]](argv, cur)

        elif (execute(argv, cur) == -1):
            print(f"unkown action or unknown alias \"{argv[1]}\"")
            print("\"ze list\"")
            actions['help'](argv, cur)

    con.commit()
    con.close()

if __name__ == "__main__":
    main()
