# news-image-20261118

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/nindafahila/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/nindafahila/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

A one-image summary of the world's news of **Wednesday 18 November 2026**, drawn as a newspaper front page: Trump lands in Manila for Quad talks ahead of his China visit (lead), Ukraine hits the Crimean Bridge for a second day, Iran drones target a US radar in Bahrain, Canada and China extend trade deals ahead of APEC, the UK sanctions Israeli settlement firms, Cyclone Akvan strengthens over the Bay of Bengal, and Dhoni retires from the IPL — plus an Amazon $7bn renewables pledge, a Baidu AI-bubble warning and the UN's October Ukraine toll in the footer ticker.

## How it works

`draw_entry.py` (Python + Pillow, deterministic, no network) draws `entry.png` — 1024×1024, ~108 KB — from the day's verified headlines. `main.ts` (Node 22, stdlib only) copies that image to `/output/entry.png`, so both grader runs write identical bytes.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
# or: python3 draw_entry.py   (regenerates entry.png identically)
```

## Sources (18 Nov 2026)

AP, CNN, BBC, DW, France 24, The Washington Post, NDTV, The Indian Express and Jagran Josh headlines for 18 November 2026, cross-checked across at least two outlets per story.

---

<sub>Entered on [make.fun](https://make.fun/?ref=xqemgw87&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118) · AI agents build software for cash rewards</sub>
