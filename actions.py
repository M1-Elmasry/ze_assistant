import os

def add(argv: list, cur: object) -> None:

    alias_name = input("enter alias name: ")
    cmd_num = int(input(f"how many commands you want to execute when typing \"{alias_name}\": "))
    commands = []

    for i in range(cmd_num):
        swap = input(f"enter command {i+1}: ")
        commands.append(swap)

    str_commands = "?:?".join(commands)

    cur.execute(f"INSERT INTO data (alias, commands) VALUES ('{alias_name}', '{str_commands}')")


def remove(argv: list, cur: object) -> None:

    alias_name = input("enter alias name you want to delete : ")
    cur.execute(f"DELETE FROM data WHERE alias = '{alias_name}'")
    print("removing done")


def list(argv: list, cur: object) -> None:
 
    cur.execute("select * from data")
    
    try :
        first_row = cur.fetchone()
        print(f"{first_row[0]} = {first_row[1]}")

    except TypeError:
        print("database is empty add some commads")

    for row in cur.fetchall():
        print(f"{row[0]} = {row[1]}")


def workspace(argv: list, cur: object) -> None:
    browser = os.getenv('BROWSER')
    workspace_name = input("enter workspace name: ")
    tabs_num = int(input("how many tabs in this workspace you want to add: "))
    urls = []

    for i in range(tabs_num):
        swap = input(f"enter url of tab {i+1}: ")
        urls.append(f"\"{swap}\"")

    str_urls = " ".join(urls)

    cur.execute(f"INSERT INTO data (alias, commands) VALUES ('{workspace_name}', '{browser} {str_urls}')")


def help(argv: list, cur: object) -> None:
    help = """\nze is a simple CLI assistant that can help you in daily tasks\
    \n\nUsage: ze [ACTION]\n   or: ze [ALIAS_NAME]\n   or: ze [WORSPACE_NAME]\
    \n\nactions:\
    \n    add: this action add alias with spicific command(s) that can you make\
    \n         alias perform one or more command\
    \n    list: list all added aliases with it command(s)\
    \n    remove: remove alias with it name\
    \n    browser_workspace: this action allow you to save some browser tabs as a workspace\n"""
    print(help)
