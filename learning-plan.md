# ben-geometry -- learning plan

The authoritative scope for the course. Self-contained modules that, in order,
climb from *seeing* to *proving* to *competing*. Ben has done BMC, so every
module ends at a real proof or a contest-flavored problem.

Modules 01 through 05 are built (full trio each: concepts, slides, worksheet).
Part 3, a dedicated BMC-style problem set, is the planned next step.

## Part 1 -- See it (build with your hands)

### Module 01 -- Compass and Straightedge: the oldest game in math
- **Hook:** build a perfect equilateral triangle and a six-petal flower without
  measuring anything.
- **Built:** Euclid I.1 (equilateral triangle), perpendicular bisector, the
  regular hexagon from a fixed compass width.
- **Proved:** the triangle's sides are *forced* equal (all radii); the flower
  closes in exactly six steps because a regular hexagon's side equals the
  circumradius (six 60-degree central angles).
- **Competition gem:** recover the erased center of a circle from chords.
- **Aside that hooks:** what is and is not constructible (pentagon yes; heptagon,
  angle-trisection, squaring the circle no).

## Part 2 -- Prove it

### Module 02 -- Why every triangle adds to 180
- **Hook:** tear the corners off any triangle; they always make a straight line.
- **Proved:** the parallel-line proof using alternate ("Z") angles. The key leap:
  from "I tried three" to "it must hold for all."
- **Extends:** polygon angle sums `(n-2) x 180`; the walking-turtle exterior-angle
  argument (always 360).
- **Competition gem:** the five points of any five-pointed star sum to 180.

### Module 03 -- Circle secrets: the inscribed angle
- **Hook:** any diameter, any point on the circle: always a right angle (Thales).
- **Proved:** the inscribed angle theorem (rim angle = half central angle) via
  isosceles radii + the exterior-angle fact; Thales falls out as the diameter
  case.
- **Extends:** all rim points on an arc see a chord at the same angle; cyclic
  quadrilaterals (opposite angles sum to 180), the BMC workhorse.
- **Competition gem:** intersecting chords give similar triangles (and the
  `AX*XB = CX*XD` length rule).

### Module 04 -- Tilings: why only three shapes fill the floor
- **Hook:** which regular shapes cover the floor with no gaps, and why only three?
- **Proved:** at any vertex the corner angles must total exactly 360, so a regular
  n-gon tiles only when its interior angle `(n-2) x 180 / n` divides 360. That
  leaves only 60, 90, 120: the triangle, square, and hexagon. Uses Module 02's
  polygon angle sum directly.
- **Extends:** semiregular (Archimedean) tilings, where mixed regular polygons
  still total 360 at every vertex (exactly eight of them).
- **Competition gem:** which multisets of regular-polygon corner angles sum to 360
  at a point, and which of those extend to a full tiling.
- **Cross-link:** Isa's pattern-block module finds the same pentagon gap by hand,
  with no angle arithmetic.

### Module 05 -- Pythagoras: proofs you can see
- **Hook:** `a^2 + b^2 = c^2`, shown three ways you watch rather than memorize.
- **Proved:** the rearrangement / tilted-square proof, President Garfield's
  trapezoid, and the similar-triangles (altitude-to-hypotenuse) proof.
- **Extends:** generating Pythagorean triples with `(m^2 - n^2, 2mn, m^2 + n^2)`;
  the converse as a right-angle test; the 3D space-diagonal version.
- **Competition gem:** prove the converse, or generate several triples from the
  m, n machine.

## Part 3 -- Compete with it *(planned)*

Each module already ends with a competition gem. The dedicated next step is a set
of BMC-style problem sheets (angle chasing, cyclic quadrilaterals, constructions)
once Parts 1 and 2 are solid.

## Prerequisites

Module 01 needs nothing. Module 03 leans on the isosceles-triangle and
exterior-angle facts from Module 02, so do 02 before 03. Module 04 uses Module
02's polygon angle sum. Module 05 stands largely on its own. A sensible order is
simply 01, 02, 03, 04, 05.
