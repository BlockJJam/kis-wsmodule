from turtle import dot
from ws.config.parser import dotenv_parser

print(dotenv_parser.get_env('URL'))