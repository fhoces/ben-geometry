[ben-geometry home](../README.md)  |  [< Prev: Module 04 -- Tilings: why only three shapes fill the floor](../module-04/concepts.md)  |  _(last module)_

# 05 -- Pythagoras: proofs you can see

> **The hook.** You already know `a^2 + b^2 = c^2` for a right triangle. The
> point of this module is *not* the formula. The point is that you can **watch**
> it happen. We are going to see three different proofs, three pictures that each
> force the formula to be true, instead of memorizing one. By the end you will be
> able to *make a right angle appear out of nowhere* just by checking three
> numbers.

**You need:** grid paper, a pencil, scissors (optional but fun), a ruler.
**Time:** 45 to 60 minutes. **Level:** the payoff module, real proofs.

**In this module:** [Do this](#do-this) - [Why it works](#why-does-it-work) - [Push further](#push-further) - [For the grown-up](#for-the-grown-up)

A **right triangle** has one 90-degree corner. The two short sides touching that
corner are the **legs**, `a` and `b`. The long side across from it is the
**hypotenuse**, `c`. The claim is that the square built on the hypotenuse has the
same area as the two squares built on the legs, added together.

---

## Do this

### Move 1: build the three squares

1. On grid paper, draw a right triangle with legs 3 and 4 squares (the
   hypotenuse will come out to exactly 5, you will see why soon).
2. On the side of length 3, draw the square that sticks out away from the
   triangle. Count its little boxes: `3 x 3 = 9`.
3. On the side of length 4, draw its square sticking out. Count: `4 x 4 = 16`.
4. On the slanted side, draw *its* square sticking out. This one is tilted, so
   count its area by the trick below.

Now add the two leg squares: `9 + 16 = 25`. Look at the big tilted square. Its
area is also **25**. The two small squares fill up the big one exactly.

```
                 +-----+
                 | 9   |   leg square, 3 x 3
                 |     |
        +--------+-----+
        |       /|
        |      / |   right triangle, legs 3 and 4
        | c   /  |
        |    /   |        +----------+
        |   /    |        |          |
   c^2  |  /     |        |   16     |  leg square, 4 x 4
 tilted | /      |        |          |
 square |/       |        +----------+
        +--------+
   (real picture is in the slides; this is just a reminder)
```

### Move 2: count a tilted square's area

The big square on the hypotenuse is tilted, so you cannot just read off a side
length. Trick: draw the smallest *upright* square that surrounds it. For our
3-4-5 triangle, the tilted square fits inside a 7-by-7 box (area 49). Sitting in
the four corners of that box are four copies of your right triangle, each with
area `(1/2)(3)(4) = 6`. So the tilted square is `49 - 4 x 6 = 49 - 24 = 25`.
There it is again: **25**.

### Move 3: make a right angle with a rope

Tie 12 evenly spaced knots in a loop of string (ancient Egyptian builders really
did this). Peg it into a triangle with sides 3, 4, and 5 knots. The corner
between the 3-side and the 4-side is a **perfect right angle**, every time. You
just built a 90-degree angle with nothing but counting. Hold onto why that works;
it is the competition gem.

---

## Why does it work?

One formula, three different pictures. Pick the one you like; each one is a full
proof.

### Proof 1: the rearrangement (the tilted square)

Take a big square with side `a + b`. Drop one copy of the right triangle into
each of the four corners. The four triangles leave a square-shaped hole in the
middle, and that hole has side `c` (each of its sides is a hypotenuse).

Now find the big square's area two ways.

- **As one square:** `(a + b)^2 = a^2 + 2ab + b^2`.
- **As its pieces:** four triangles plus the hole `= 4 x (1/2)ab + c^2 = 2ab + c^2`.

These are the same area, so set them equal:

```
a^2 + 2ab + b^2 = 2ab + c^2
```

Cancel the `2ab` from both sides and you are left with `a^2 + b^2 = c^2`. The
`2ab` was just the four triangles hiding in plain sight.

### Proof 2: President Garfield's trapezoid

James Garfield found this in 1876, five years before he became US president.
Take two copies of the right triangle and lean them together into a right
**trapezoid** (a four-sided shape with two parallel sides). The parallel sides
have lengths `a` and `b`, and the distance between them is `a + b`. The slanted
top edge, plus the two hypotenuses meeting at the bottom, leave a clean right
angle in the middle, so the middle piece is a right triangle with both legs `c`.

Area two ways again.

- **As a trapezoid:** `(1/2)(a + b)(a + b)` (average of the parallel sides, times
  the height).
- **As three triangles:** `(1/2)ab + (1/2)ab + (1/2)c^2`.

Set them equal and multiply everything by 2:

```
(a + b)^2 = ab + ab + c^2  =>  a^2 + 2ab + b^2 = 2ab + c^2  =>  a^2 + b^2 = c^2
```

Same finish as Proof 1, but from half the picture. That is the elegant part: a
president's doodle and Euclid's tilted square land in the exact same place.

### Proof 3: similar triangles

Drop a straight line from the right-angle corner down onto the hypotenuse, hitting
it at a right angle. It splits the hypotenuse `c` into two pieces, call them `p`
and `q`, so `p + q = c`.

Here is the magic: each of the two small triangles you just made is a *shrunk
copy* of the whole original triangle (same three angles). Matching the
corresponding sides of similar triangles gives two clean facts:

```
a^2 = c * p        (the triangle on the a side)
b^2 = c * q        (the triangle on the b side)
```

Add them: `a^2 + b^2 = c*p + c*q = c(p + q) = c * c = c^2`. No squares to cut out,
no areas to count, just two similar triangles and one addition.

---

## Push further

- **Pythagorean triples.** Whole-number right triangles like 3-4-5 are called
  Pythagorean triples. The next few: 5-12-13, 8-15-17, 7-24-25. Check one:
  `5^2 + 12^2 = 25 + 144 = 169 = 13^2`. They feel rare, but there are infinitely
  many, and there is a machine that spits them out.
- **The triple machine.** Pick any two whole numbers `m > n`. Then
  `(m^2 - n^2, 2mn, m^2 + n^2)` is *always* a triple. Try `m = 2, n = 1`:
  `(3, 4, 5)`. Try `m = 3, n = 2`: `(5, 12, 13)`. Try `m = 4, n = 1`:
  `(15, 8, 17)`. It never fails, because the algebra works out:
  `(m^2 - n^2)^2 + (2mn)^2 = m^4 + 2m^2n^2 + n^4 = (m^2 + n^2)^2`.
- **It only works for right triangles.** For a triangle that is not right,
  `a^2 + b^2` does *not* equal `c^2`; it overshoots or undershoots depending on
  whether the angle is sharp or wide. (The full repair is the **law of cosines**,
  `c^2 = a^2 + b^2 - 2ab cos C`. When `C = 90` degrees, `cos C = 0` and the extra
  term vanishes, handing Pythagoras right back.)
- **One more dimension.** The space diagonal of a box with edges `a`, `b`, `c`
  has length `d`, where `d^2 = a^2 + b^2 + c^2`. It is just Pythagoras used twice:
  once on the floor of the box, once standing up.
- **Competition gem.** Prove the **converse**: if a triangle has sides with
  `a^2 + b^2 = c^2`, then the angle opposite `c` *must* be a right angle. (That is
  the real reason the 3-4-5 knotted rope makes a right angle, and why builders
  trust it.) One clean way: build a brand-new right triangle with legs `a` and
  `b`; its hypotenuse is `sqrt(a^2 + b^2) = c` by the theorem, so it has the exact
  same three side lengths as your triangle, so the two triangles are congruent,
  so your triangle's third angle is the right angle too. As a second challenge,
  use the triple machine to generate five different triples and check each one.

---

## For the grown-up

- The whole module rests on one idea: a single fact can have many proofs, and
  *seeing* one is better than reciting the formula. If Ben already "knows
  Pythagoras," that is the perfect setup. Ask him to prove it. The blank look is
  the hook.
- Proof 1 (rearrangement) is the most physical; cutting four paper triangles and
  shuffling them inside an `(a + b)` square makes it land. Proof 2 (Garfield) is
  the slickest once Proof 1 is understood. Proof 3 (similar triangles) is the most
  grown-up and needs Module 03's comfort with similar shapes; save it for last or
  skip it if similarity is not solid yet.
- Common stumble: counting the tilted square by trying to measure its slanted
  side. Steer to the surrounding-box trick (area of box minus four triangles)
  instead. That move is the heart of Proof 1.
- Common stumble: thinking the converse is "obvious" or the same as the theorem.
  It is not. The theorem says right angle => `a^2 + b^2 = c^2`; the converse runs
  the arrow the other way, and it is what makes the rope trick work. Getting Ben
  to feel that the two directions are different statements is a real logic win.
- Where this course goes next: every module has ended with a competition gem.
  The dedicated finish line is a set of BMC-style problem sheets (angle chasing,
  cyclic quadrilaterals, constructions) that braid Modules 01 through 05 together.
  This module is the last of the build-and-prove set; the next step is to compete.

---

[ben-geometry home](../README.md)  |  [< Prev: Module 04 -- Tilings: why only three shapes fill the floor](../module-04/concepts.md)  |  _(last module)_
