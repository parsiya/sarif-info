import argparse
import traceback
from commands import split, stats

def parser():
    """
    Create and parse arguments then return the parser.
    """
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(help="sub-command help", dest="subcmd")

    parser_stats = subparsers.add_parser("stats",
        help="display a table with rule ID and number of findings")
    parser_stats.add_argument("file", help="the SARIF file or a directory with one or more SARIF files")
    # store_false means the value is True if it's not included and False when
    # the flag is present.
    parser_stats.add_argument("--asc", "--ascending", action='store_false',
        help="sort the table by the number of findings")

    parser_split = subparsers.add_parser("split",
        help="split the sarif file by rule ID")
    parser_split.add_argument("file", help="the SARIF file or a directory with one or more SARIF files")

    parser_help = subparsers.add_parser("help", help="display help usage")
    return parser


def main():
    """
    Entry point.
    """
    parsed = parser()
    args = parsed.parse_args()

    try:
        if args.subcmd == "help":
            parsed.print_help()
            return

        if args.subcmd == "stats":
            print(stats(args.file, sorted=args.asc))
            return
        
        if args.subcmd == "split":
            # split the file
            split(args.file)
            return

    except Exception as e:
        print(traceback.format_exc())
        return

    # print the help if nothing is passed
    parsed.print_help()

if __name__ == "__main__":
    main()

