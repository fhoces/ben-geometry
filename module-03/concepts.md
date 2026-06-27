# 03 -- Circle secrets: the inscribed angle

> **The hook.** Draw a circle and a diameter straight across the middle, ends
> **A** and **B**. Now pick *any* point **P** on the circle and draw P-to-A and
> P-to-B. Measure the angle at P. It is 90 degrees. Move P anywhere else on the
> circle: still 90. High up, near the edge, anywhere. The angle "standing on a
> diameter" is *always* a right angle. This is called Thales' theorem, and it is
> the doorway to the single most useful idea in competition geometry.

**You need:** compass, straightedge, protractor (just to be amazed, the proof
needs none), pencil, paper.
**Time:** 45 to 60 minutes. **Level:** the payoff sheet. Go slow.

---

## Do this

### Part A: Thales

1. Draw a circle and mark its center **O**.
2. Draw a diameter: a straight line through O, hitting the circle at **A** and
   **B**.
3. Pick any point **P** on the circle (not A or B). Draw PA and PB.
4. Measure angle APB with the protractor. Note it.
5. Pick three or four different P's around the circle and repeat.

```
            P
           /|\
          / | \
         /  |  \
        A---O---B      angle at P is 90 degrees, for every P on the circle
         \  |  /
          \ | /
           \|/
            P'         (P' too: also 90)
```

Every P gives 90 degrees. Why can't it ever be 88 or 93?

### Part B: the bigger secret

1. Fresh circle, center O. Mark two points **A** and **B** on it (not a diameter
   this time, just any two points).
2. Draw the angle **AOB** at the center.
3. Now pick a point **P** on the circle, on the *major* (longer) arc, and draw
   the angle **APB** at the rim.
4. Measure both. The rim angle APB is exactly **half** of the center angle AOB.
5. Move P around the major arc and re-measure APB. It does not change. Every P on
   that arc sees AB at the same angle.

```
            P                  Q
             \                /
              \              /
               \            /
                \          /
        A--------+--------B
                 |
                 O          angle APB = angle AQB = (1/2) angle AOB
```

Two things to be amazed by: the rim angle is half the center angle, and **all the
rim points on the same arc see AB at the same angle.**

---

## Why does it work?

### The big theorem first (it gives Thales for free)

**Inscribed angle theorem:** an angle at the rim is half the angle at the center,
when both stand on the same arc.

Here is the cleanest case. Put P, A, B on the circle so that the line **PO**
passes through the center. Draw OA. Now look at triangle OAP:

- OA and OP are both radii, so they are equal. The triangle is **isosceles**.
- Equal sides face equal angles, so angle OPA = angle OAP. Call each of them
  **t**.
- The angle AOB at the center is the *exterior* angle of triangle OAP at O. An
  exterior angle equals the sum of the two far interior angles (this follows
  straight from exploration 02: the three angles make 180, and the exterior angle
  plus the interior one at O also make 180). So angle AOB = t + t = **2t**.

The rim angle APB is **t**. The center angle AOB is **2t**. The rim angle is half
the center angle. Done, for this case. The general case (where PO does not pass
through center) splits into one or two copies of this case by drawing the line
PO; same idea.

### Thales falls out instantly

When A and B are the ends of a **diameter**, the center angle AOB is a straight
line, 180 degrees. The rim angle is half of that: **90 degrees.** That is Thales,
and now you see it is not a coincidence, it is just the inscribed angle theorem
with the center angle stretched to a straight line.

### And the "same arc, same angle" fact

Every rim point P on the same arc sees the *same* center angle AOB (the center
does not move). Half of a fixed thing is a fixed thing. So they all see AB at the
same angle. That is why APB = AQB above.

---

## Push further

- **Cyclic quadrilaterals (this is the BMC gold).** Put four points on a circle
  and join them into a quadrilateral. Then **opposite angles add to 180.** See if
  Ben can prove it from the inscribed angle theorem. (Hint: each angle of the
  quad is an inscribed angle; pair up the arcs they stand on, and the four arcs
  make the whole circle.) "Four points lie on one circle" is one of the most
  powerful things you can notice in a contest problem, and this is why.
- **The converse, used as a tool.** If you ever see a right angle PAB-style
  setup, P might be forced onto a circle with AB as diameter. Spotting hidden
  circles is a top-tier olympiad move.
- **Competition gem.** Two chords of a circle, AB and CD, cross at a point X
  inside the circle. Prove that triangle AXC and triangle DXB have the same
  shape (similar). Hint: hunt for two pairs of equal inscribed angles standing on
  the same arcs. (This leads to the "intersecting chords" length rule
  `AX times XB = CX times XD`, a classic.)

---

## For the grown-up

- This is the highest-leverage sheet in the path. The inscribed angle theorem and
  its cyclic-quadrilateral corollary are *everywhere* in competition geometry, so
  it is worth doing patiently and coming back to.
- The proof leans on two things from exploration 02: the isosceles base-angles
  fact and the exterior-angle fact. If those are shaky, revisit 02 first; the
  proof here will feel like magic instead of logic otherwise.
- Let the measuring in Part B do its job before any proof. The "wait, all these
  different points give the *same* angle" surprise is the motivation. Without that
  surprise, the theorem is just a formula.
- Common stumble: in the proof, forgetting *why* OA = OP. The answer ("both are
  radii of the same circle") is the quiet engine behind almost every circle
  proof. Point at it explicitly.
- Natural next step after this path: a dedicated angle-chasing and
  cyclic-quadrilateral problem set, which is squarely BMC territory. Say the word
  and I will build one.
