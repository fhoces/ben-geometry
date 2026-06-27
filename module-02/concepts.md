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

### First, a smaller fact: the "Z" rule (alternate angles)

Draw two **parallel** lines (use both edges of your ruler, that guarantees they
are parallel). Now draw one slanted line crossing both. It makes a "Z" shape.

```
   ===========\=========   line 1
               \
                \           the two marked angles, inside the Z,
   ==============\=======   line 2  are EQUAL
```

The two angles tucked inside the Z (one at the top line, one at the bottom, on
opposite sides of the slant) are equal. This is the alternate angles rule, and it
is *the* fact about parallel lines. Convince yourself with the ruler: slide one
angle along the slant line until it lands on the other; they match.

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

---

## For the grown-up

- The single most important moment here is *not* the proof. It is the question
  "we tried three, why does that settle infinitely many?" Sit in that discomfort
  with him before reaching for the parallel line. The need for proof should feel
  *earned*, like the experiment left a gap that only an argument can fill.
- The Z rule (alternate angles) is the one piece we take on faith from the
  hands-on sliding. If he wants to know *why* alternate angles are equal, that is
  a deeper question about what "parallel" even means, and it is fine to say "we
  will take this one as our trusted starting block for today." Real geometry is
  built on a small number of trusted starting blocks (axioms); picking them is
  part of the game.
- Common stumble: drawing the helper line through A but *not* parallel to BC. The
  whole proof hinges on parallel. Use the two edges of the ruler so it is exactly
  parallel.
- If the star problem clicks, that is a strong signal he is ready for a dedicated
  angle-chasing problem set. Next stop after this path is exploration 03, where
  angles meet circles.
