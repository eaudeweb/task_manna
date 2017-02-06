import argparse
from task_manna.api import Manna


parser = argparse.ArgumentParser()
parser.add_argument(
    'url', type=str,
    help='Site url, e.g. https://redmine.eaudeweb.ro'
)
parser.add_argument('apikey', type=str, help='API Key')


def run_cli():
    args = parser.parse_args()
    manna = Manna(args.url, args.apikey)
    print(next(manna.tasks).id)

