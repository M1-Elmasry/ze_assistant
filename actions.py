def add(argv: list, cur: object) -> None:

    alias_name = input("enter you alias name: ")
    cmd_num = int(input(f"how many commands you want to execute when typing \"{alias_name}\": "))
    commands = []

    for i in range(cmd_num):
        swap = input(f"enter command {i}: ")
        commands.append(swap)

    str_commands = " then ".join(commands)

    cur.execute(f"INSERT INTO data (alias, commands) VALUES ('{alias_name}', '{str_commands}')")

def remove(argv: list, cur: object) -> None:
    pass

def list(argv: list, cur: object) -> None:
 
    cur.execute("select * from data")
    
    try :
        first_row = cur.fetchone()
        print(f"{first_row[0]} = {first_row[1]}")

    except TypeError:
        print("database is empty")
        print("add some commads")

    for row in cur.fetchall():
        print(f"{row[0]} = {row[1]}")

def workspace(argv: list, cur: object) -> None:
    pass

def help(argv: list, cur: object) -> None:
    pass
