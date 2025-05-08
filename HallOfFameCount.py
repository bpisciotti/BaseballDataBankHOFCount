import pandas as pd
import argparse

def count_inductees(startYear = 2000, endYear = 2016):
    df = pd.read_csv("HallOfFame.csv")
    inducted = df[
        (df.yearid.between(startYear, endYear)) &
        (df.inducted == "Y")
    ]
    return inducted.playerID.nunique()

def main():
    parser = argparse.ArgumentParser(
        description="Count HOF inductees between two years"
    )

    parser.add_argument(
        "-s", "--start",
        type=int,
        default=2000,
        help="Start year (inclusive)."
    )

    parser.add_argument(
        "-e", "--end",
        type=int,
        default=2016,
        help="End year (inclusive)."
    )

    args = parser.parse_args()

    total = count_inductees(args.start, args.end)
    print(f"Player inducted between {args.start} and {args.end}: {total}")

    

if __name__ == "__main__":
    main()