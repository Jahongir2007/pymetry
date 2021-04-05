### How to use in Pymetry
With this python library, you can draw shapes in just one line of code from the turtle module.
## Pymetry 1.1.0 (new version)
### How to calc perimeter square and triangle (in pymetry 1.1.0 version)
```markdown
import pymetry
pym = pymetry

#Calc perimeter square
pym.perm(12, 25)

#Calc peimeter triangle
pym.pert(10, 14, 12)
```
### How to calc square side and triangle side (in pymetry 1.1.0 version)
```markdown
import pymetry
pym = pymetry

#Calc square side
pym.sqside("unknown", 12, 25, 70)

#Calc triangle side
pym.trside("unknown", 14, 12, 42)
```
### What is it ```"unknown"```?
```"unknown"``` is the keyword that specifies the value to be found in this pymetry
### What is it ```aboutme()``` (in pymetry 1.1.0 version)?
```markdown
import pymetry
pym = pymetry

#aboutme()
pym.aboutme()
#value: Pymetry python library. Author: Jahongir Sobirov.License: MIT. Version: 1.1.0
```
### How to calc adjacent corners (in pymetry 1.1.0 version)
```markdown
import pymetry
pym = pymetry

#Calc adjacent corners
pym.adjaccor("unknown", 135)
```
### How to calc value of triangle degrees (in pymetry 1.1.0 version)
```markdown
import pymetry
pym = pymetry

#Calc value of triangle degrees
pym.valtri("unknown", 50, 120)
```
### Draw square in Pymetry
```markdown
import pymetry
pym = pymetry
pym.square(100, "orange", 5)
#100 => distance
#"orange" => color line
#5 => line size
```
### Draw triangle in Pymetry
```markdown
import pymetry
pymetry.triangle(90, 135, 100, "orange", 0)
#90 => corner
#135 => corner
```
### Draw corner in Pymetry
```markdown
import pymetry
pym = pymetry
pym.corner(20, 100, "black", 2)
#20 => corner
```
### Draw rectangle in Pymetry
```markdown
import pymetry
pym = pymetry
pym.rect(100, "gray", 7)
```
### Draw circle in Pymetry
```markdown
import pymetry
pymetry.circle(60, "brown", 4)
```
### Draw pentagon in Pymetry
```markdown
import pymetry
pym = pymetry
pym.pentagon(150, "yellow", 8)
```
### Draw hexagon in Pymetry
```markdown
import pymetry
pym = pymetry
pym.hexagon(200, "yellow", 8)
```
### Draw heptagon in Pymetry
```markdown
import pymetry
pym = pymetry
pym.heptagon(100, "yellow", 8)
```
### Draw octagon in Pymetry
```markdown
import pymetry
pym = pymetry
pym.octagon(150, "yellow", 8)
```
### Draw polygon in Pymetry
```markdown
import pymetry
pym = pymetry
pym.polygon("blue", 3)
```
### Turtle shape in Pymetry
```markdown
import pymetry
pym = pymetry
pym.trsize("1, 20, 15)
```
