import os

def execute(alias_name: str, cur: object) -> int:

    browser = os.getenv('BROWSER')
    data_tuple = cur.execute("SELECT * FROM data")

    for row in data_tuple:
        if (row[0] == alias_name):
            for command in row[1].split("?:?"):
                if (browser in command):
                    if (input("you want to close existing browser sessions y or n: ") == "y"):
                        os.system(f"killall -9 {browser}")
                os.system(command)
            return (0)
    return (-1)
