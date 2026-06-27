[ben-geometry home](../README.md)  |  _(first module)_  |  [Next: Module 02 -- Why every triangle adds to 180](../module-02/concepts.md)

# 01 -- Compass and Straightedge: the oldest game in math

> **The hook.** With a compass and an unmarked ruler (no numbers, you only use
> the edge), the ancient Greeks built perfect shapes more than 2000 years ago.
> No measuring. No protractor. Can you make a *perfect* equilateral triangle, a
> triangle where you are sure all three sides are exactly equal, without measuring
> a single thing?

**You need:** a compass, a straightedge (a ruler is fine, but you may only use
its edge, never its numbers), a pencil, paper.
**Time:** 30 to 45 minutes. **Level:** warm-up, mostly hands.

**In this module:** [Do this](#do-this) - [Why it works](#why-does-it-work) - [Push further](#push-further) - [For the grown-up](#for-the-grown-up)

The one rule of this game: you may only do two things.
1. With the straightedge, draw a straight line through two points.
2. With the compass, draw a circle, given a center point and a radius you set by
   placing the two compass legs on two points.

Everything below is built from just those two moves.

---

## Do this

### Move 1: the perfect triangle

This is literally Proposition 1 of Euclid's *Elements*, the first thing in the
oldest geometry textbook.

1. Draw a segment. Call its ends **A** and **B**. This is your one and only ruler.
2. Put the compass point on **A**, pencil on **B**. Draw a full circle.
3. Without changing the compass width, put the point on **B**, pencil on **A**.
   Draw a second full circle.
4. The two circles cross at two points. Pick the top one, call it **C**.
5. Use the straightedge to draw **A**-to-**C** and **B**-to-**C**.

You have a triangle. Here is the question that matters: *how do you know* all
three sides are equal? You never measured. (Hold that thought for "Why does it
work?" below.)

```
        C
       / \
      /   \         both circles have the same radius = length AB
     /     \
    A-------B
   (.)     (.)      <- the two compass points
```

### Move 2: cut a segment exactly in half (perpendicular bisector)

1. Draw a segment **A** to **B**.
2. Compass point on **A**, open it to a bit more than half of AB, draw an arc
   above and below the segment.
3. *Same width*, compass point on **B**, draw arcs that cross the first two.
4. The arcs meet at two points. Draw the line through them.

That line cuts AB exactly in half **and** crosses it at a perfect right angle.
You just found the midpoint without measuring, and built a 90-degree angle for
free.

### Move 3: the six-petal flower (and a hidden hexagon)

1. Draw a circle. Do **not** change the compass width for the rest of this.
2. Put the compass point anywhere *on* the circle and make a small mark where the
   pencil crosses the circle.
3. Move the point to that new mark, make the next mark. Keep walking around.
4. Count how many steps it takes to get back to the start.

It is exactly **six**, every time. Now connect the six marks in order with the
straightedge: a perfect regular hexagon. Connect every mark to the center and
you get the six-petal flower you have probably seen drawn in margins forever.

```
        *           six marks, each one compass-width
      /   \          from its neighbors
     *     *
     |  .  |         . = center
     *     *
      \   /
        *
```

Why *exactly* six, and not "about six"? That is the best puzzle in this whole
sheet. See below.

---

## Why does it work?

**The triangle.** Side AB is the radius of *both* circles (you never changed the
width). Side AC is a radius of the circle centered at A, so AC = AB. Side BC is a
radius of the circle centered at B, so BC = AB. All three equal the same radius,
so they equal each other. It is not "close to equal." It is *forced* to be equal,
for any starting segment AB you could have drawn. That is the difference between
drawing a triangle and *proving* one.

**The six marks.** Connect three things: the center, one mark, and the next mark.
Two of those sides are radii of the circle, and the third side is your fixed
compass width, which is also that same radius. So every one of those little
triangles is equilateral, which means each one has a 60-degree angle at the
center. Angles all the way around the center add to 360. And 360 / 60 = 6. The
hexagon falls out of the fact that *the side of a regular hexagon equals the
radius of the circle around it.* That is a genuinely surprising fact, and you
just built it.

---

## Push further

- **Bisect any angle.** Given an angle, put the compass point on the corner and
  mark both arms. From those two marks, swing equal arcs that cross. The line
  from the corner through that crossing splits the angle exactly in half. (Why?
  Hint: look for two triangles that have to be identical.)
- **Build a square** using only the perpendicular-bisector move twice.
- **The 2000-year-old cliffhanger.** Some shapes *can* be built this way and some
  *cannot*, and it took until the 1800s to prove which. You **can** build a
  regular pentagon (5 sides) and a 17-sided regular polygon (Gauss did it at 19,
  and asked for it on his tombstone). You **cannot** build a regular 7-sided
  polygon, you **cannot** trisect a general angle into three equal parts with
  these tools, and you **cannot** "square the circle." Those impossibilities are
  real theorems, not "nobody has figured it out yet." Ask Ben to guess which are
  possible before you tell him; the answers surprise everyone.
- **Competition gem.** Construct the center of a circle when someone has erased
  the center and left you only the circle. (Hint: any chord's perpendicular
  bisector passes through the center. How many chords do you need?)

---

## For the grown-up

- The whole point of move 1 is the question "how do you *know* the sides are
  equal." If Ben measures with the ruler to check, gently push back: the ruler is
  only an edge here. The argument ("all three are the same radius") is the win,
  and it is his first taste of a proof that covers *every* case at once.
- For the hexagon, resist explaining first. Let him discover the count is exactly
  six, get surprised, and only then chase the "why." The equilateral-triangle
  reason is very satisfying once he sees it.
- Common stumble: changing the compass width between steps. If the flower does
  not close up neatly into six, that is almost always the cause.
- If he loves this, Euclidea (see the path README) is the perfect next hour: it
  turns these exact moves into levels.

---

[ben-geometry home](../README.md)  |  _(first module)_  |  [Next: Module 02 -- Why every triangle adds to 180](../module-02/concepts.md)
