[ben-geometry home](../README.md)  |  [< Prev: Module 03 -- Circle secrets: the inscribed angle](../module-03/concepts.md)  |  [Next: Module 05 -- Pythagoras: proofs you can see](../module-05/concepts.md)

# 04 -- Tilings: why only three shapes fill the floor

> **The hook.** Look at a tiled bathroom floor or a honeycomb. The tiles cover
> everything with no gaps and no overlaps. If every tile has to be the *same*
> regular shape, which shapes work? Equilateral triangles work. Squares work.
> Regular hexagons work. Regular pentagons do **not**, no matter how you turn
> them. Only those three regular shapes tile the floor, and there is a one-line
> reason why. Can you find it before you read it?

**You need:** paper, scissors, a pencil; ideally several cut-out copies of a
regular triangle, square, pentagon, and hexagon (or pattern blocks).
**Time:** 30 to 45 minutes. **Level:** hands first, then a clean proof.

**In this module:** [Do this](#do-this) - [Why it works](#why-does-it-work) - [Push further](#push-further) - [For the grown-up](#for-the-grown-up)

---

## Do this

### Move 1: try to tile with each shape

Cut out a stack of identical copies of one regular shape and try to surround a
single point with them, corner to corner, no gaps, no overlaps. Then try to keep
going outward. Do this for each shape.

1. **Triangles.** Equilateral triangles snug up around a point. Count how many fit
   before you close the loop.
2. **Squares.** Four squares meet at a corner like graph paper. Easy.
3. **Hexagons.** Regular hexagons lock together like a honeycomb.
4. **Pentagons.** Now try regular pentagons. Fit them around one point as tightly
   as you can. Something goes wrong. *What* goes wrong, exactly?

You will find the pentagons leave a thin wedge of gap, or they start to overlap.
They never close up neatly. Hold onto that gap; it is the whole secret.

### Move 2: measure the corner you are crowding around

The key question is what happens **at a meeting-point**, a single vertex where
corners come together. For the floor to have no gap and no overlap there, the
corners that meet must fill the full turn exactly: they must add to **360
degrees**.

```
        \   |   /
         \  |  /        the corners meeting at one point
    ______\ | /______   must sweep out the whole turn:
          / | \         their angles add to exactly 360.
         /  |  \
        /   |   \
```

So count the corners that fit around your point and ask: do their angles total
exactly 360, or do they fall short (gap) or run over (overlap)?

### Move 3: fill in the angle for each shape

A regular shape's corner angle is fixed. Fill this in (you proved the formula in
Module 02):

| shape | corners (n) | each corner angle | does it divide 360? | tiles? |
|-------|-------------|-------------------|---------------------|--------|
| triangle | 3 | 60 | 360 / 60 = 6 | yes |
| square | 4 | 90 | 360 / 90 = 4 | yes |
| pentagon | 5 | 108 | 360 / 108 = 3.33... | **no** |
| hexagon | 6 | 120 | 360 / 120 = 3 | yes |
| heptagon | 7 | 128.57... | 360 / 128.57 = 2.8 | no |

The pattern is staring at you: a shape tiles exactly when its corner angle
divides 360 evenly. Three regular shapes do that, and only three.

---

## Why does it work?

**The corner angle of a regular n-gon.** From Module 02, the angles inside any
n-sided polygon add up to `(n - 2) * 180`. A *regular* polygon spreads that total
evenly over its n equal corners, so each corner is

```
interior angle = (n - 2) * 180 / n
```

For n = 3 that is 60, for n = 4 it is 90, for n = 5 it is 108, for n = 6 it is
120. (You can read it as "180 minus the exterior angle 360/n".)

**The rule at a vertex.** Around any meeting-point, the corners that come together
must sweep the full turn: they add to exactly 360. If you use **k** identical
copies of one regular shape, the corners meeting there are `k` equal angles, so

```
k * (interior angle) = 360
```

That means the interior angle has to **divide 360 evenly** (k has to be a whole
number; you cannot place 3.33 tiles).

**Now just check.** Which regular corner angles divide 360?

- triangle, 60: `360 / 60 = 6`. Six triangles around a point. **Works.**
- square, 90: `360 / 90 = 4`. Four squares. **Works.**
- pentagon, 108: `360 / 108 = 3.33...`. Three pentagons give `324` (a 36-degree
  gap); four give `432` (overlap). **No whole number fits.** That is your gap.
- hexagon, 120: `360 / 120 = 3`. Three hexagons. **Works.**

**Why nothing past the hexagon can ever work.** For n = 7 or more, the corner
angle is bigger than 120 but smaller than 180 (it climbs toward 180 as the
polygon gets rounder). So at most **two** could meet at a point, and two angles
each under 180 add to under 360: they can never reach a full turn. Below 7 we
already checked every case by hand. So the only regular corner angles that divide
360 are **60, 90, and 120**, giving exactly **three** regular tilings: triangle,
square, hexagon. That is the entire theorem.

---

## Push further

- **Mix the shapes (semiregular tilings).** Drop the rule that every tile is the
  same. Keep two rules: the corners at each vertex still add to 360, and every
  vertex looks the same. Now you can blend regular polygons. Each pattern is
  named by the shapes going around one vertex:
  - **4.8.8**: a square and two octagons. `90 + 135 + 135 = 360`. (Octagon corner
    is `(8-2)*180/8 = 135`.) This is the classic "stop sign" tiling.
  - **3.6.3.6**: triangle, hexagon, triangle, hexagon. `60 + 120 + 60 + 120 = 360`.
  - **3.3.3.3.6**: four triangles and a hexagon. `60*4 + 120 = 360`.
  - **3.4.6.4**: triangle, square, hexagon, square. `60 + 90 + 120 + 90 = 360`.

  There are exactly **eight** of these semiregular (Archimedean) tilings. Hunting
  them is a great afternoon.
- **Competition gem.** Here is the search that BMC loves: *which multisets of
  regular-polygon corner angles add to exactly 360 at a single point?* It is a
  finite hunt, because once you use a big-angle polygon you have little room
  left. For example `3.4.4.6` works as a vertex: `60 + 90 + 90 + 120 = 360`. So
  does `3.12.12`: `60 + 150 + 150 = 360`. The twist: **not every valid vertex
  extends to a full tiling.** `3.4.4.6` passes the angle test at one point but you
  cannot grow it to cover the whole plane with every vertex matching. So the real
  two-part problem is: (1) list all corner-angle multisets that sum to 360, then
  (2) decide which actually tile. The first part is pure arithmetic; the second
  is where the geometry bites.

---

## For the grown-up

- **Let the pentagon fail in his hands first.** The surprise is the hook. Have Ben
  push pentagons around a point and *feel* the gap before any angle is computed.
  Then the question writes itself: "why does that gap show up?"
- **The load-bearing idea is one sentence:** the corners meeting at a point must
  add to 360, so the corner angle has to divide 360. Everything else is checking
  cases. If he gets that sentence, he has the theorem.
- **Where kids stick:** confusing the corner (interior) angle with the angle at
  the center, or with the exterior angle. Anchor on "the angle of the actual
  pointy corner of the tile," and reuse the `(n-2)*180/n` he already proved in
  Module 02 rather than re-deriving it.
- **Common wrong guess:** "a big enough regular polygon will eventually tile."
  Push on it: the corner angle only grows toward 180 and never comes back down, so
  past the hexagon there is no room for even three corners. The door closes at six
  sides and stays closed.
- **Cross-link to Isa.** Isa's pattern-block module finds this exact pentagon gap
  by hand, just by trying to ring a point with blocks, with no angle arithmetic at
  all. Same discovery, two ages: she sees the gap, Ben proves the gap is forced.
- **Next up (Module 05):** Pythagoras, where `a^2 + b^2 = c^2` gets proved by
  pictures you can watch, not formulas you memorize.

---

[ben-geometry home](../README.md)  |  [< Prev: Module 03 -- Circle secrets: the inscribed angle](../module-03/concepts.md)  |  [Next: Module 05 -- Pythagoras: proofs you can see](../module-05/concepts.md)
