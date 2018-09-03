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

args = parser.parse_args()

if args.type == "view":
	print(UserManager().get_user_data(user_id=args.user_id, user_email=args.user_email))
elif args.type == "message":
	print("sending message")
	print(UserManager().message_user(user_id=args.user_id, user_email=args.user_email))
