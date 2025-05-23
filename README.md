# Hall of Fame Count

**Question:** How many players were inducted into the Baseball Hall of Fame between 2000 and 2016?

This repository contains a simple Python script that reads the `HallOfFame.csv` dataset from the Baseball Databank and prints the number of unique players inducted into the Hall of Fame within the specified year range.

## Files

* `HallOfFameCount.py` — Python script that loads the CSV, filters by induction year (2000–2016), and prints the count.
* `HallOfFame.csv` — The CSV file from the Baseball Databank (not included; download separately).

## Requirements

* Python 3.7 or higher
* pandas library

## Installation

1. **Clone or download** this repo:

   ```bash
   git clone https://github.com/bpisciotti/BaseballDataBankHOFCount.git
   cd BaseballDataBankHOFCount
   ```

2. **Download the dataset**:

   * Visit the [Baseball Databank on Kaggle](https://www.kaggle.com/datasets/open-source-sports/baseball-databank?select=HallOfFame.csv)
   * Download `HallOfFame.csv` and place it in this project folder.

3. **Install dependencies**:

   ```bash
   python3 -m pip install --user pandas
   ```

> **Optional:** Create a virtual environment for isolation:
>
> ```bash
> python3 -m venv venv
> source venv/bin/activate     # bash/zsh
> pip install pandas
> ```

## Usage

```bash
# Default year range (2000–2016):
python3 HallOfFameCount.py

# Custom year range:
python3 HallOfFameCount.py --start 1980 --end 1990
# (or use the short flags)
python3 HallOfFameCount.py -s 1980 -e 1990
```

## Customization

* **Year range via CLI flags:** Pass `--start` (`-s`) and `--end` (`-e`) on the command line to specify your desired inclusive range without editing the script.

* **Changing defaults:** To update the default years, edit the `default` values in the `argparse` setup in `HallOfFameCount.py`:

  ```python
  parser.add_argument("-s", "--start", type=int, default=2000, help="Start year (inclusive).")
  parser.add_argument("-e", "--end",   type=int, default=2016, help="End year (inclusive).")
  ```

* To change the year range, edit the default parameters in `HallOfFameCount.py`:

  ```python
  def count_inductees(start_year=2000, end_year=2016):
      ...
  ```

* You can also import and call `count_inductees()` from another script or notebook.

## License

This project is released under the MIT License. Feel free to use and modify it for your own learning and data exploration.
