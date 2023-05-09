import os

def execute(argv: list, cur: object) -> int:

    browser = os.getenv('BROWSER')
    data_tuple = cur.execute("SELECT * FROM data")

    for row in data_tuple:
        if (row[0] == argv[1]): # argv[1] = alias_name
            for command in row[1].split("?:?"):
                if (browser in command):
                    if (input("you want to close existing browser sessions y or n: ") == "y"):
                        os.system(f"killall -9 {browser}")
                os.system(f"{command} {' '.join(argv[2:])}") # to execute any command after alias name
                # say the user type "ze add <file_name>" and "add" is equal "git add"
                # in this case ze must execute all line "ze "git add" <file_name>"
            return (0)
    return (-1)
