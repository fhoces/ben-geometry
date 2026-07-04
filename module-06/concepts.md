[ben-geometry home](../README.md)  |  [< Prev: Module 05 -- Pythagoras: proofs you can see](../module-05/concepts.md)  |  _(last module)_

# 06 -- The contest toolkit: angle chasing and hidden circles

> **The hook.** Here is an angle problem. Triangle ABC has a 50 degree angle at
> A. Draw the two lines that split angle B and angle C exactly in half; they
> cross at a point I inside the triangle. What is the angle BIC? It looks like
> you would need to know B and C. You do not. The answer is forced by the 50
> alone, and it comes out in two lines. By the end of this sheet Ben can walk up
> to a problem like that, and to a picture with four points that "happen" to sit
> on a circle, and knock it over on purpose.

**You need:** compass, straightedge, protractor (to check answers, not to find
them), pencil, paper. **Time:** this is a set, not a sitting. Do a few problems
at a time over a week. **Level:** Part 3, the contest sheet. Everything here is
built from Modules 01 to 05; nothing new is assumed.

**In this module:** [The toolkit](#the-toolkit) - [The problems](#the-problems) - [Full solutions](#full-solutions) - [For the grown-up](#for-the-grown-up)

---

## The toolkit

Every problem below is solved with facts Ben already proved. No new theorems.
Keep this list next to the sheet:

1. **Angles in a triangle add to 180.** (Module 02.)
2. **Isosceles = equal base angles.** Equal sides face equal angles, and the
   reverse: equal angles force equal sides. (Module 02.)
3. **Exterior angle = the two far interior angles added.** (Module 02.)
4. **Inscribed angle = half the center angle** on the same arc; and every rim
   point on one arc sees a chord at the **same** angle ("same segment"). (Module
   03.)
5. **Thales, and its reverse.** An angle standing on a diameter is 90. Backwards:
   if a point sees a segment at 90, it sits on the circle that has that segment
   as diameter. (Module 03.) This is how you *find a hidden circle*.

Two habits matter more than any single fact:

- **Name every angle you know, in the picture, before you try to find the
  target.** Fill the figure with what is forced. The answer usually appears on
  its own.
- **When two angles are equal for no obvious reason, suspect four points on a
  circle.** Concyclic points are the contest's favorite hidden structure.

---

## The problems

Statements only here. Full worked solutions are in the next section, so the
grown-up can steer without spoiling. Let Ben struggle first.

### Warm-ups (angle chasing)

**W1.** Triangle ABC has AB = AC and angle A = 50. (a) Find angles B and C. (b)
Draw the line that splits angle B in half, hitting AC at D. Find angle ABD and
angle ADB.

**W2.** A five-pointed star has tip angles 30, 25, 40, and 45 at four of its
points. What is the fifth tip angle? (You proved in Module 02 that the five tips
of any star add to 180.)

### Angle chasing, the real thing

**A1 (the hook).** Triangle ABC has angle A = 50. The bisector of angle B and the
bisector of angle C meet at the point I (this point is called the *incenter*).
(a) Find angle BIC. (b) Now prove that for *any* triangle, angle BIC = 90 + A/2.
Notice your answer to (a) never used B or C on their own.

**A2 (the golden triangle).** Triangle ABC has AB = AC and angle A = 36, so angles
B and C are each 72. Draw the bisector of angle B, meeting AC at D. Prove that
BD = BC and that AD = BD. (So AD = BD = BC: one bisector makes three equal
lengths appear. This triangle hides the golden ratio, and it is the engine behind
the regular pentagon from Module 01.)

### Cyclic quadrilaterals and hidden circles

**C1.** Put four points A, B, C, D in order on a circle and join them into a
quadrilateral. Prove that opposite angles add to 180: angle A + angle C = 180.
(Hint: each corner of the quad is an inscribed angle. Use the "half the center
angle" fact, and remember the arcs around the whole circle add to 360.)

**C2.** Points A, B, C, D sit in order around one circle. You measure angle CAD =
28 (the angle at A looking across to C and D). (a) What is angle CBD, the angle at
B looking at the same two points C and D? (b) In the same picture angle ADB = 35.
What is angle ACB? Explain in one sentence each.

**C3 (find the hidden circle).** Quadrilateral ABCD has a right angle at B and a
right angle at D: angle ABC = angle ADC = 90. (a) Explain why all four points must
lie on a single circle, and say which segment is its diameter. (b) Use that to
prove angle ACB = angle ADB.

### Constructions (compass and straightedge)

**D1 (cut an angle in half).** Given an angle, construct its exact bisector with
compass and straightedge only. Write the steps, then prove the line you drew
really splits the angle into two equal halves. (No protractor, and no "it looks
even.")

**D2 (the circle through three points).** Given any triangle, construct the one
circle that passes through all three of its corners. (a) Give the construction.
(b) Prove that the three perpendicular bisectors of the sides all pass through a
single point, so the construction always works.

### The challenge (a real BMC gem)

**E1.** Triangle ABC is drawn inside its circumcircle (the circle through all
three corners). The bisector of angle A is extended until it hits the circle
again at a point M. (a) Prove MB = MC (so M is the exact middle of the arc BC).
(b) **Hard.** Let I be the incenter (from A1). Prove MI = MB as well. So M is the
same distance from B, from C, and from I. Hint for (b): show triangle MBI has two
equal angles by chasing angle MBI and angle MIB separately. This fact is nicknamed
"Fact 5" among olympiad students because it turns up constantly.

---

## Full solutions

### W1
(a) AB = AC makes the triangle isosceles, so B = C. They share 180 - 50 = 130
between them, so **B = C = 65**.
(b) The bisector cuts angle B (65) in half, so **angle ABD = 32.5**. In triangle
ABD the angles are A = 50, ABD = 32.5, so **angle ADB = 180 - 50 - 32.5 = 97.5**.

### W2
The five tips always add to 180 (Module 02). So the fifth tip is
180 - (30 + 25 + 40 + 45) = 180 - 140 = **40**.

### A1
(a) Call B and C the full angles at those corners. The bisectors make angle IBC =
B/2 and angle ICB = C/2. In triangle BIC the three angles add to 180:
angle BIC = 180 - B/2 - C/2 = 180 - (B + C)/2. But B + C = 180 - A = 130, so
angle BIC = 180 - 65 = **115**.
(b) The same two lines prove the general rule: angle BIC = 180 - (B + C)/2, and
since B + C = 180 - A, this is 180 - (180 - A)/2 = 180 - 90 + A/2 = **90 + A/2**.
With A = 50 that is 90 + 25 = 115, matching (a). The point of the problem: BIC
depends only on A, never on how B and C split the rest.

### A2
Label the angles. B = C = 72. The bisector splits B into angle ABD = angle DBC =
36. 

*Triangle DBC:* its angles are DBC = 36, C = 72, so angle BDC = 180 - 36 - 72 =
72. Now DBC has two equal angles (72 at C and 72 at D), so the sides facing them
are equal: the side facing C is BD, the side facing D is BC, hence **BD = BC**.

*Triangle ABD:* its angles are A = 36 and ABD = 36, two equal angles again. The
sides facing them are BD (faces A) and AD (faces ABD), so **AD = BD**.

Putting them together, AD = BD = BC. One extra line (the bisector) forced three
segments to be equal. That cascade of 36-72 triangles is exactly what builds the
regular pentagon.

### C1
Each corner of the quadrilateral is an inscribed angle. Angle A stands on the arc
BCD (the arc from B to D not containing A), so angle A is half that arc. Angle C
stands on the arc DAB (the arc from D to B not containing C), so angle C is half
*that* arc. Those two arcs together are the whole circle, 360. So
angle A + angle C = (1/2)(arc BCD) + (1/2)(arc DAB) = (1/2)(360) = **180**. The
same argument gives angle B + angle D = 180.

### C2
(a) Angle CAD (at A) and angle CBD (at B) both stand on the same chord CD. Because
the four points are in order around the circle, A and B fall on the same arc of
CD, so this is the same-segment case. Same segment, same angle: **angle CBD = 28**.
(b) Angle ADB (at D) and angle ACB (at C) both stand on the chord AB from the same
arc, so they are equal: **angle ACB = 35**.

### C3
(a) Point B sees the segment AC at a right angle, so by the reverse of Thales, B
lies on the circle that has **AC as diameter**. Point D also sees AC at a right
angle, so D lies on that *same* circle. A and C are its endpoints. So all four
points A, B, C, D lie on one circle.
(b) Now they are concyclic, so "same segment" applies. Angle ACB (at C) and angle
ADB (at D) both stand on the chord AB, and C and D are on the same arc, so
**angle ACB = angle ADB**.

### D1
*Construction.* Put the compass point on the vertex V and draw an arc that crosses
both rays of the angle, at points P and Q. Now widen (or keep) the compass, put
the point on P and draw an arc inside the angle; keeping the same width, put the
point on Q and draw another arc; call where they cross R. Draw the line VR. That
is the bisector.

*Why it works.* Look at triangles VPR and VQR. VP = VQ (both are the first arc's
radius). PR = QR (both are the second arc's radius). VR is shared. So the two
triangles have the **same three sides**, which means they are exact copies of each
other. Copies have equal matching angles, so angle PVR = angle QVR: the line VR
splits angle PVQ into two equal halves. No measuring anywhere.

### D2
*Construction.* Build the perpendicular bisector of side AB (Module 01: two equal
arcs from A and from B, join the crossings). Build the perpendicular bisector of
side BC the same way. They meet at a point O. Put the compass point on O, pencil
on A, and draw the circle. It passes through B and C too.

*Why it works.* The key fact: a point is on the perpendicular bisector of a
segment exactly when it is the same distance from the two ends. (A point M on the
perpendicular bisector of AB makes two right triangles that are copies, so
MA = MB.) 

So O, being on AB's bisector, has OA = OB. And O, being on BC's bisector, has
OB = OC. Chaining these, OA = OB = OC: O is the same distance from all three
corners. That common distance is the radius, so one circle centered at O hits all
three. And since OA = OC, that same O also lies on the perpendicular bisector of
CA. So all three perpendicular bisectors pass through the single point O (called
the *circumcenter*), which is why the construction never fails.

### E1
Set A = angle at A, B = angle at B, C = angle at C, with A + B + C = 180.

(a) AM bisects angle A, so angle BAM = angle CAM = A/2. These are inscribed
angles: angle BAM stands on arc BM, angle CAM stands on arc CM. Equal inscribed
angles cut off equal arcs, so arc BM = arc CM, which makes the chords equal:
**MB = MC**. (Equal arcs, equal chords. So M is the midpoint of arc BC.)

(b) We show triangle MBI is isosceles by finding angle MBI and angle MIB
separately and seeing they are equal.

- *angle MBI.* Split it: angle MBI = angle MBC + angle CBI. Now angle MBC is an
  inscribed angle on arc MC, and angle MAC (= A/2) is an inscribed angle on that
  *same* arc MC, so angle MBC = A/2. And angle CBI = B/2 because BI bisects angle
  B. So angle MBI = A/2 + B/2.
- *angle MIB.* This is the exterior angle of triangle ABI at the vertex I (the
  straight line A-I-M). An exterior angle equals the two far interior angles
  added: angle MIB = angle IAB + angle IBA = A/2 + B/2.

Both equal A/2 + B/2, so angle MBI = angle MIB. A triangle with two equal angles
has the two opposite sides equal, so **MI = MB**. Combined with (a),
MB = MC = MI: the arc-midpoint M is equidistant from B, C, and the incenter I.

---

## For the grown-up

- **This is a set to return to, not a worksheet to finish.** Ten problems that
  climb from a 30-second isosceles check to a genuine olympiad lemma (E1). Doing
  two or three well beats rushing all ten. The worksheet has room to draw; the
  real work is Ben filling a figure with every angle he can name before hunting
  the target.
- **The one habit to coach:** label first, solve second. On A1, W1, C2, the answer
  falls out the moment the known angles are written on the picture. If Ben stares
  at the target angle trying to "see" it, redirect him to mark everything he
  already knows.
- **Where the leap is.** W1, W2, C2 are confidence-builders (one step). A1, A2,
  C1, C3, D1, D2 are the real content: each is a short proof, not just a number.
  E1 is a stretch and is meant to be; it is a named olympiad fact ("Fact 5"). If
  it stalls, do part (a) only, and treat part (b) as something to come back to
  after another pass through Module 03.
- **Constructions are proofs in disguise.** D1 and D2 both end with "and here is
  why the picture is forced, not lucky." That "same three sides means exact
  copies" move (D1) and "on the perpendicular bisector means equidistant" move
  (D2) are the same style of argument as everything in Part 2. Do not let them
  become button-pushing recipes; the proof is the point.
- **What "hidden circle" trains.** C3 is small but it is the single most useful
  contest instinct: two right angles on the same segment, or two equal angles for
  no clear reason, should make Ben reach for a circle. Nearly every hard BMC angle
  problem hides one.
- **Answer-checking.** The protractor is for confirming a found answer, not
  finding it. Every number here is exact and comes from the toolkit facts; if a
  measured angle disagrees, the drawing is off, not the theorem.
- **Correctness note (for you).** The pentagon-building 36-72 triangle in A2 is
  genuinely constructible; the regular pentagon is a compass-and-straightedge
  shape (unlike the heptagon or a general angle trisection, which are impossible).
  So A2 connects honestly back to Module 01.

---

[ben-geometry home](../README.md)  |  [< Prev: Module 05 -- Pythagoras: proofs you can see](../module-05/concepts.md)  |  _(last module)_
