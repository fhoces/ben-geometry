# ben-geometry

Geometry for Ben (11). He has done Berkeley Math Circle, so this does not stop at
"and that's the answer." Each module climbs from *seeing* geometry to *proving*
it to *competing* with it.

## How to use it

Each `module-XX/` has three pieces:

- **`slides.html`** -- open in a browser, introduce the topic together.
- **`worksheet.pdf`** -- print it, this is the hands-on doing and the problems.
- **`concepts.md`** -- the grown-up's full guide: the proof, plus notes on what to
  ask and where kids get stuck.

You do not need to be ahead of him; `concepts.md` tells you what to draw out.

## Modules

| # | Module | The hook | Status |
|---|--------|----------|--------|
| 01 | [Compass and Straightedge](module-01/) | Build a perfect triangle and a six-petal flower without measuring anything. | slides + worksheet ready |
| 02 | [Why every triangle adds to 180](module-02/) | Tear the corners off any triangle; they always make a straight line. Why always? | concepts ready |
| 03 | [Circle secrets: the inscribed angle](module-03/) | Any diameter, any point on the circle: always a right angle. | concepts ready |

See [`learning-plan.md`](learning-plan.md) for the full road map and what's next
(tilings, Pythagoras, a dedicated competition set).

## The path, in one line

01 is the warm-up and is mostly hands. 02 is where *proof* starts: the leap from
"I tried three triangles" to "it must hold for all of them." 03 builds the single
most useful idea in olympiad geometry (the inscribed angle), so do it slowly.

## Tools that pair well

- A real **compass** with a locking radius wheel, and an unmarked straightedge.
- **Euclidea** (euclidea.xyz): gamified compass-and-straightedge puzzles, perfect
  right after module 01.

More in the collection's [`../resources.md`](../resources.md).

## Building

```sh
RSTUDIO_PANDOC=/Applications/quarto/bin/tools/aarch64 \
  Rscript -e 'rmarkdown::render("slides.Rmd", quiet=TRUE)'   # from a module dir
xelatex worksheet.tex && xelatex worksheet.tex
```
