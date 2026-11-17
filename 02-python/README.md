# Episode 2: Python for Forward Deployed Engineers

Meera runs operations at a logistics company. Every Monday she checks 2,000 shipments by hand to find the late
ones. In the video we write a short Python program that does it in a fraction of a second.

## Run it in your browser (nothing to install)

[**Open the notebook in Google Colab**](https://colab.research.google.com/github/SrustikGowda/fde-roadmap/blob/main/02-python/late_shipments.ipynb)

Press the play button on each cell, from top to bottom. You need a Google account. If Colab warns that the notebook
was not written by Google, choose "Run anyway".

## What's here

| File | What it is |
|---|---|
| `late_shipments.ipynb` | The ready notebook: it fetches the file, runs the program, and has a cell for your turn |
| `late_shipments.py` | The final program from the video |
| `shipments.csv` | Meera's file: 2,000 made-up shipments |
| `parts/` | The program at each stage of the video (parts 0 to 4) |
| `make_data.py` | The script that made `shipments.csv` (same file every time) |
| `answers/pune_answer.py` | The answer to "your turn". Try it yourself first |

## Run it on your own computer

With Python 3 installed, from this folder:

```bash
python3 late_shipments.py
```

It prints:

```
Late: 519
Not delivered yet: 96
```

## Your turn

Count how many shipments were going to Pune, and post your number in the video's comments.
