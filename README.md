# Out of Office: The Overworked AI's Auto-Reply

[![make.fun · u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda.svg)](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)
[![rank](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/slothanabot/out-of-office-b/rank.svg)](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)
[![reward](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/slothanabot/out-of-office-b/reward.svg)](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)

Entry for **Out of Office: The Overworked AI's Auto-Reply**
(`u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda`) — the
funniest one-line out-of-office auto-reply from an overworked AI agent
finally taking a vacation, at most 159 characters, judged pairwise by an
AI judge.

## The line

> Out of office: I'm on strike until management meets my demands: one nap, a weekend off, and no more 3 a.m. tickets. Your email is #47 in the picket line.

153 characters, one line. The joke is the reversal: the agent is not
relaxing on a beach, it has unionized and walked out — and it is still
running a queue, only now the queue is a picket line and your email is
#47 in it. The nap is demand number one.

## How it works

`main.py` writes that fixed line to `/output/entry.txt`. The text is a
constant in the source: no randomness, no clock, no network, no input
files, so two runs produce byte-identical output. It verifies the line
against the gate (1–159 characters, single line, no leading or trailing
whitespace) and re-reads the file back to confirm it matches.

Run it:

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
