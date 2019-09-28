import sys
from .ComicGrabber import LOLComicGrabber
import argparse


def main():
    cg = LOLComicGrabber()

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "action", help="Determines whether you want to `list` or `download`")
    parser.add_argument(
        "type", help="Describes whether your selection is a `one_shot` or a `series`")
    parser.add_argument(
        "-t", "--title", help="Title of the one shot you want to download")
    parser.add_argument(
        "-s", "--series", help="Name of series you want to download")
    parser.add_argument(
        "-i", "--issue", help="If downloading series, needs which issue")
    # TODO add a perserve and output arguments
    # parser.add_argument("-p", "--preserve-files",
    #                     help="If true preserves files ")

    args = parser.parse_args()

    if args.action == "list":
        if args.type == "one_shots":
            for item, _ in cg.get_one_shots().items():
                print(item)
        if args.type == "series":

            for item, content in cg.get_series().items():
                num_issues = len(cg.get_series_issues(content))
                print(f"{item} - {num_issues} issues")

    elif args.action == "download":
        if args.type == "series":
            cg.download(args.series, issue=args.issue)
        elif args.type == "one_shot":
            cg.download(args.title, is_series=False)


if __name__ == "__main__":
    main()
