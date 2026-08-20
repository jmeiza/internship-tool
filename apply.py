import argparse

# Note: This file helps us to read arguments from the command line.

# Note: "Internship application tool is shown when someone types python apply.py --help"
parser = argparse.ArgumentParser(description="Internship application tool")

# Note: subparsers allow us to create distinct sub-commands
subparsers = parser.add_subparsers(dest="command")

new_parser = subparsers.add_parser("new")
list_parser = subparsers.add_parser("list")
update_parser = subparsers.add_parser("update")

new_parser.add_argument("--file", type=str, default="job_posting.txt")

update_parser.add_argument("id", type=int)
update_parser.add_argument("--status", type=str)
update_parser.add_argument("--follow-up-date", type=str)

args = parser.parse_args()

if args.command == "new":
    ...
elif args.command == "list":
    ...
elif args.command == "update":
    print(args.id, args.status)
