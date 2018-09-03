from argparse import ArgumentParser

from data_class import UserManager
from utils.templates import get_template, render_context

parser = ArgumentParser(prog="integrate", usage="%(prog)s [options]",
	description="Run python codes for handling csv data using the commands and options")

parser.add_argument(
	"-id",
	"--user_id",
	type=int,
	help="enter the user's id for displaying user details"
)

parser.add_argument(
	"-e",
	"--email",
	type=str,
	help="enter the user's email for displaying user details"
)

parser.add_argument(
	"type",
	type=str,
	choices=['view', 'message']
)

parser.add_argument(
	"-all",
	"--all_users",
	action="store_true",
	help="sends message to all the users"
)

args = parser.parse_args()

if args.type == "view":
	print(UserManager().get_user_data(user_id=args.user_id, user_email=args.email))
elif args.type == "message":
	if args.all_users:
		print("SENDING EMAILS...")
		print(UserManager().message_all())
	else:
		print("SENDING EMAILS...")
		print(UserManager().message_user(user_id=args.user_id, user_email=args.email))
