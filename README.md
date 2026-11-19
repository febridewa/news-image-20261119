# The World in One Day — Thursday 19 November 2026

One image summing up the world news of Thursday 19 November 2026, built for
make.fun's daily news-image bounty
([news-image-20261119](https://make.fun/bounty/news-image-20261119)).

## The image

A 1024×1024 front page with **50 stories** — 4 drawn picture leads, 12 icon
cards, 34 one-line briefs, a dotted world map with numbered pins, and a
by-the-numbers strip:

1. **GTA VI is out at last** — Rockstar's epic launches at midnight worldwide,
   first in New Zealand; 99 Metascore, eight Game Awards nominations.
2. **Trump, Xi and Putin meet as a trio** — the first three-way summit of the
   nuclear powers, in Shenzhen on the APEC sidelines.
3. **Iran hits a US base in Kuwait** — Tehran's first strike on the Gulf ally
   since September; Bahrain shelters again.
4. **Cyclone Akvan bears down on India** — landfall on the Andhra–Odisha
   coast by noon Friday; schools shut, 21 cm of rain feared.

Plus Voyager 1 one light-day from Earth, Jeffries nominated 251–11, Fed
minutes pointing to more hikes, Anthropic's $83 IPO, Nvidia's slide, the Pew
faiths study, Gaza's "yellow line", Duckett's 133, Somalia vs the UAE, the
EU's €45bn Ukraine loan, Modi meets William and Kate, and Microsoft's
ByteDance AI talks — and 34 more briefs from every region.

Every story, headline, number and date was verified against reporting
published on 19 November 2026 (Reuters, AP, AFP, BBC, NASA and others). All
art is drawn in code; every letter is rendered in real fonts, so nothing is
garbled.

## How it runs

`main.py` (Python 3.13, standard library only) copies `entry.png` to
`$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`). The image is
deterministic: two runs write the same bytes.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Referral

Built with make.fun — referral code `6etrfz79`.

## License

MIT — see [LICENSE](LICENSE).
