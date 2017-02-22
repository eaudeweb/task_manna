import argparse
from task_manna.api import Manna
from task_manna.log import Logger


PARSER = argparse.ArgumentParser()

PARSER.add_argument(
    'url', type=str,
    help='Site url, e.g. https://redmine.eaudeweb.ro.'
)
PARSER.add_argument('apikey', type=str, help='API Key.')
PARSER.add_argument('uid', type=int, help='User ID.')
PARSER.add_argument(
    '--debug', dest='debug', action='store_true',
    help='Show DEBUG messages.'
)
PARSER.set_defaults(debug=False)


def run_cli():
    args = PARSER.parse_args()

    if args.debug:
        Logger.set_level('DEBUG')

    manna = Manna(args.url, args.apikey, args.uid)
    idx = 0

    for idx, task in enumerate(manna.tasks):
        assigned_to = task.assigned_to or dict(name='NOBODY')

        line = '#{} [{}] {}'.format(
            task.id,
            assigned_to['name'],
            task.subject
        )

        print(line)

    print('{} total tasks for uid {}'.format(idx, args.uid))
