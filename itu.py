import argparse
import webbrowser
import json
import os

ITU_DESCRIPTION = "Command line tool for ITU related tasks."
FILENAME = "itu.json"
INIT_STRUCTURE = {"courses":{},
                  "canteen":"https://itustudent.itu.dk/Campus-Life/Student-Life/Canteen-Menu"}


def get_json() -> dict:
    with open(FILENAME, "r") as f:
        data = json.load(f)
    return data


def set_json(data) -> None:
    with open(FILENAME, "w") as f:
            json.dump(data, f, indent=4)


def learnit(args) -> str:

    course = args.course

    if args.add:
        try:
            data = get_json()
            id = input("Please specifiy the course's 7 digit ID from the LearnIT URL: ")
            data["courses"][course] = id
            set_json(data)
            return f"The course '{course}' has been added to the config file with id {id}."

        except FileNotFoundError:
            return "The config file hasn't been created yet. Use itu init to create it."
        
    elif args.delete:
        try:
            data = get_json()
            data["courses"].pop(course)
            set_json(data)
            return f"The course '{course}' has been deleted from the config file."
        
        except FileNotFoundError:
            return "The config file hasn't been created yet. Use itu init to create it."
        
        except KeyError:
            return f"The course '{course}' hasn't been added to the config file yet."

    else: 
        try:
            data = get_json()
            id = data["courses"][course]
            webbrowser.open(f'https://learnit.itu.dk/course/view.php?id={id}')
            return f"Opening '{course}..."
                    
        except FileNotFoundError:
            return "The config file hasn't been created yet. Use itu init to create it."
        
        except KeyError:
            return f"The course '{course}' hasn't been added to the config file yet."
 

def init() -> str:

    if os.path.exists(FILENAME):
        return "The config file has already been created previously."
    set_json(INIT_STRUCTURE)
    return "Config file created successfully."


def git(args) -> str:

    if args.add:
        try:
            data = get_json()
            username = input("Specify your GitHub username: ")
            data["git"] = username
            set_json(data)
            return f"'{username}' saved as GitHub username."
            
        except FileNotFoundError:
            return "The config file hasn't been created yet. Use itu init to create it."
        
    else:
        try:
            data = get_json()
            username = data["git"]
            webbrowser.open(f"https://github.com/{username}?tab=repositories")
            return f"Opening GitHub..."

        except FileNotFoundError:
            return "The config file hasn't been created yet. Use itu init to create it."

        except KeyError:
            return "Your account hasn't been added yet to the config file. Use itu git -a to add it."


def canteen() -> str:

    try:
        data = get_json()
        canteen_url = data["canteen"]
        webbrowser.open(canteen_url)
        return "Opening canteen menu..."
        
    except FileNotFoundError:
        return "The config file hasn't been created yet. Use itu init to create it."

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description=ITU_DESCRIPTION, prog="itu")

    subparsers = parser.add_subparsers(title="Subcommands", dest="subcommand")

    init_parse = subparsers.add_parser(name="init",
                                    help="Creates a .json file for storing your courses.")

    canteen_parse = subparsers.add_parser(name="canteen",
                                        help="Redirects to the canteen menu.")

    learnit_parse = subparsers.add_parser(name="learnit",
                                help="Manages your LearnIT courses.")
    learnit_parse.add_argument("course", type=str, help="Name of the course you want to open.")
    learnit_parse.add_argument("-a", "--add", action="store_true")
    learnit_parse.add_argument("-d", "--delete", action="store_true")


    git_parse = subparsers.add_parser(name="git",
                                    help="Opens your GitHub account.")
    git_parse.add_argument("-a", "--add", action="store_true")
    git_parse.add_argument("-d", "--delete", action="store_true")


    args = parser.parse_args()

    match args.subcommand:
        case "init":
            print(init())
        case "learnit":
            print(learnit(args))
        case "git":
            print(git(args))
        case "canteen":
            print(canteen())