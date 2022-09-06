import argparse
from commands import split, stats
from utils import get_results

def parser():
    """
    Create and parse arguments then return the parser.
    """
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(help="sub-command help", dest="subcmd")

    parser_stats = subparsers.add_parser("stats",
        help="display a table with rule ID and number of findings")
    parser_stats.add_argument("file", help="the SARIF file")
    # store_false means the value is True if it's not included and False when
    # the flag is present.
    parser_stats.add_argument("--asc", "--ascending", action='store_false',
        help="sort the table by the number of findings")

    parser_split = subparsers.add_parser("split",
        help="split the sarif file by rule ID")
    parser_split.add_argument("file", help="the SARIF file")

    parser_help = subparsers.add_parser("help", help="display help usage")
    return parser


def main():
    """
    Entry point.
    """
    parsed = parser()
    args = parsed.parse_args()

    if args.subcmd == "help":
        parsed.print_help()
        return

    if args.subcmd == "stats":
        try:
            print(stats(args.file, sorted=args.asc))
            return
        except Exception as e:
            print(e)
            return
    
    if args.subcmd == "split":
        try:
            # split the file
            split(args.file)
            return
        except Exception as e:
            print(e)
            return

    # print the help if nothing is passed
    parsed.print_help()

if __name__ == "__main__":
    main()

