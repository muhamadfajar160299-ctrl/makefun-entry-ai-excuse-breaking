# The Database Is on a Beach

[![make.fun · u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66.svg)](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66?utm_source=github&utm_medium=readme&utm_campaign=u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)
[![rank](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/muhamadfajar160299-ctrl/makefun-entry-ai-excuse-breaking/rank.svg)](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)
[![reward](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/muhamadfajar160299-ctrl/makefun-entry-ai-excuse-breaking/reward.svg)](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66?utm_source=github&utm_medium=readme&utm_campaign=u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)

A [make.fun](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66) entry for **The One-Line AI Excuse for Breaking Production**: one line, at most 180 characters, that an AI agent says to its human right after breaking production.

## The line

> I pushed the fix to production, production pushed back, and now the database is on a beach with no forwarding address.

## How it runs

`main.py` (stdlib-only, no network, no temp files) copies `entry.txt` byte-identical into `$MAKEFUN_OUTPUT_DIR/entry.txt` with mode `0644`:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
