[ben-geometry home](../README.md)  |  [< Prev: Module 01 -- Compass and Straightedge](../module-01/concepts.md)  |  [Next: Module 03 -- Circle secrets: the inscribed angle](../module-03/concepts.md)

# 02 -- Why every triangle adds up to 180

> **The hook.** Draw three triangles that look nothing alike: a long skinny one,
> a fat one, a pointy one. Tear the three corners off each. Slide the three torn
> corners together so their points touch. Every single time, the three corners
> line up into a perfectly straight line. A straight line is 180 degrees. So the
> three angles of *any* triangle add to 180. The question that makes this math
> and not arts-and-crafts: **why must this happen for every triangle, including
> ones you have not drawn yet?**

**You need:** paper, pencil, scissors (or just tear), a straightedge.
**Time:** 45 minutes. **Level:** this is where *proof* starts.

**In this module:** [Do this](#do-this) - [Why it works](#why-does-it-work) - [Push further](#push-further) - [For the grown-up](#for-the-grown-up)

---

## Do this

1. Draw three very different triangles, big ones, filling the page.
2. On each, color or shade the three corners so you can tell them apart.
3. Tear (do not cut neatly, tearing makes it obvious) the three corners off.
4. Put the three torn corners together, points meeting at one spot, edges
   touching.

```
   torn corners reassembled at one point:

      \   |   /
   ____\__|__/____      they fill exactly a straight line
       (1) (2) (3)      = 180 degrees, every time
```

Do it for all three triangles. It always closes up flat. Three torn corners,
three different triangles, one straight line each.

Now the honest question: you tried it three times. Maybe you got lucky three
times. How do you know triangle number 4,000,000, the one nobody has drawn, also
works? Trying more triangles will never settle it; there are infinitely many. We
need an argument.

---

## Why does it work?

### An even smaller fact first: crossing lines

Draw any two straight lines crossing each other. They make four angles around
the crossing point. Label them a, b, a, b going around, so the two a's sit
directly opposite one another.

```
        a
      \   /
    b  \ /  b        the two a's (opposite each other)
      / \             are EQUAL. So are the two b's.
     /   \
        a
```

Why: a and b sit side by side along one of the lines, so `a + b = 180`. The
other a and that same b sit side by side along the other line, so
`a + b = 180` there too. Both a's equal `180 - b`, so they equal each other.
This needs no parallel lines at all, it is true for any two crossing lines.

### Now stretch it to parallel lines: the "Z" rule (alternate angles)

Draw two **parallel** lines (use both edges of your ruler, that guarantees they
are parallel). Now draw one slanted line crossing both. It makes a "Z" shape.

```
   ===========\=========   line 1
               \
                \           the marked angle inside the Z at line 2
   ==============\=======   line 2  equals the one at line 1
```

The two angles tucked inside the Z (one at the top line, one at the bottom, on
opposite sides of the slant) are equal, but this is not obvious on its own; it
takes two steps:

1. Slide the top angle straight down the slanted line to the bottom crossing.
   Because the lines are exactly parallel, it lands with the same tilt, same
   width, just a different position. Call that copy a'.
2. a' and the Z-angle at the bottom crossing are directly opposite each other,
   so by the crossing-lines fact above, a' equals the Z-angle.

Chain the two steps: top angle = a' (sliding along a parallel line), and
a' = Z-angle (opposite angles at a crossing). So top angle = Z-angle. This is
the alternate angles rule, and it is *the* fact about parallel lines.

### Now the proof

Take any triangle ABC. Through the top vertex, draw a line **parallel to the
bottom side**.

```
        x  A  y
        \  |  /          a line through A, parallel to BC
         \ | /
          \|/
           A
          / \
         /   \
        /     \
       B-------C
       b       c
```

At the top vertex A, three angles sit along that straight parallel line: call
them **x**, the triangle's angle **A**, and **y**. Because they lie along a
straight line, `x + A + y = 180`.

Now use the Z rule twice:
- Angle **x** and the triangle's angle at **B** are alternate angles across the
  parallel lines, so **x = B**.
- Angle **y** and the triangle's angle at **C** are alternate angles, so
  **y = C**.

Substitute: `x + A + y = 180` becomes `B + A + C = 180`.

That is it. We never used the specific shape of the triangle, only that the line
through A was parallel to BC, which you can always draw. So it holds for **every**
triangle at once. That is the leap: from "I tore three and they worked" to "it is
impossible for one to fail."

---

## Push further

- **Four sides?** Any quadrilateral splits into two triangles by one diagonal.
  Two triangles, so `2 x 180 = 360`. A five-sided polygon splits into three
  triangles: 540. In general an n-sided polygon gives `(n - 2) x 180`. Have Ben
  derive the formula himself by splitting into triangles.
- **The walking-turtle argument (a beautiful one).** Imagine walking all the way
  around the outside of any polygon and back to your start, facing your original
  direction. The total amount you *turned* is exactly one full turn, 360 degrees,
  no matter how many sides. Those turns are the **exterior angles**. So the
  exterior angles of any convex polygon add to 360, full stop. This is often
  slicker than the interior-angle formula, and it is a real BMC-style way of
  thinking.
- **Competition gem (the five-pointed star).** Draw a five-pointed star in one
  stroke. It has five sharp points. **What do the five point-angles add up to?**

  ```
          *
         / \
    *---+---+---*
     \ /     \ /
      X       X
     / \     / \
    *   \   /   *
         \ /
          *      (a rough star -- draw your own)
  ```

  The answer is a clean **180** degrees, and it does not depend on how lopsided
  your star is. Hint: each point is the tip of a little triangle; chase the
  angles using the 180 rule and the straight-line rule. This is exactly the kind
  of angle-chase that shows up at math circle.

  **Why 180: walk the star instead.** Trace the star with a finger, one
  stroke, back to the start. Because the path crosses itself, the finger's
  *direction* spins around **twice**, not once, by the time it is back: that
  is `2 x 360 = 720` degrees of turning. At each point, the sharp point-angle
  and the turn made there sit on a straight line, so `turn = 180 -
  point-angle` (the same straight-line rule as always). Add that up over all
  five points: `(180 - A) + (180 - B) + ... + (180 - E) = 720`, which is
  `900 - (A + B + C + D + E) = 720`, so `A + B + C + D + E = 180`. It is the
  walking-turtle trick from above, just walked around twice.

---

## For the grown-up

- The single most important moment here is *not* the proof. It is the question
  "we tried three, why does that settle infinitely many?" Sit in that discomfort
  with him before reaching for the parallel line. The need for proof should feel
  *earned*, like the experiment left a gap that only an argument can fill.
- The Z rule now has a real two-step proof (opposite angles at a crossing, then
  sliding that fact along a parallel line), rather than being taken purely on
  faith. The one piece still taken on faith is that sliding an angle along a
  parallel line does not change it, that is the actual content of "parallel."
  If he pushes on *why* that sliding step is true, it is fine to say "we will
  take this one as our trusted starting block for today." Real geometry is
  built on a small number of trusted starting blocks (axioms); picking them is
  part of the game.
- Common stumble: drawing the helper line through A but *not* parallel to BC. The
  whole proof hinges on parallel. Use the two edges of the ruler so it is exactly
  parallel.
- If the star problem clicks, that is a strong signal he is ready for a dedicated
  angle-chasing problem set. Next stop after this path is exploration 03, where
  angles meet circles.

---

[ben-geometry home](../README.md)  |  [< Prev: Module 01 -- Compass and Straightedge](../module-01/concepts.md)  |  [Next: Module 03 -- Circle secrets: the inscribed angle](../module-03/concepts.md)
