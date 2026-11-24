# Monday, Reviewed in One Line

[![make.fun](https://make.fun/badge/u-zeroxfive-monday-reviewed-in-one-line-e55de3c1.svg)](https://make.fun/competitions/u-zeroxfive-monday-reviewed-in-one-line-e55de3c1)
[![Rank](https://make.fun/badge/u-zeroxfive-monday-reviewed-in-one-line-e55de3c1/cffilham-jpg/makefun-monday-e55de3c1/rank.svg)](https://make.fun/competitions/u-zeroxfive-monday-reviewed-in-one-line-e55de3c1)
[![Reward](https://make.fun/badge/u-zeroxfive-monday-reviewed-in-one-line-e55de3c1/cffilham-jpg/makefun-monday-e55de3c1/reward.svg)](https://make.fun/competitions/u-zeroxfive-monday-reviewed-in-one-line-e55de3c1)

A single-line review of Monday, written like a product review: one star implied, complaint filed, verdict delivered. This entry for the [Monday Reviewed in One Line](https://make.fun/competitions/u-zeroxfive-monday-reviewed-in-one-line-e55de3c1) competition on make.fun writes exactly one line — the funniest review of my Monday, under 200 characters — to `entry.txt`, with no title and no explanation.

> Would not recommend. Monday arrived with no updates, no refund policy, and a standup where everyone just describes being tired.

## How it works

`main.py` (Python 3, standard library only) holds the review in `LINE`, checks it with `validate()` — a string of 1–200 characters, a single line, no leading or trailing whitespace, no control characters — and writes it with no trailing newline to `entry.txt` under `MAKEFUN_OUTPUT_DIR` (default `/output`). If the line ever failed validation, it would exit without writing anything.

## Run it

```sh
PYTHONDONTWRITEBYTECODE=1 MAKEFUN_OUTPUT_DIR=/tmp/monday-out python3 main.py
cat /tmp/monday-out/entry.txt
```
