
# WHY?

- I can't find any civil engineering library...
- Build a quick and cheap demo to see how it works
- Automate Automate Automate Automate Automate Automate Automate
- Optimize material usage

Date: 20190412

Author: Curtis

Version: 0.1

# FEATURES
-  class oriented
-  basic geometry input
-  basic loading input
-  Code to be packaged for portability

## TODO
- SFD, BMD, deflection
- columns
- frames
- conenctivity
- section capacity check
- load factors (euro code?)
- load as a class, not as a dict
- visualize

#  INPUT:
-  P,L

# OUTPUT:
-  A,B, any point at X
-  reactions
-  shear
-  bending


```python
from civpy import Beam

B1 = Beam.Beam_Simple('B1',20)
B1.show_units()
```

    
            All units in SI
            Load: kN
            Length: meter
    


```python
B1.add_point_load(6400,15)
B1.add_point_load(3200,4)

# quick check internal forces of 1 point load
B1.cal_reaction(B1.loads[0])
```

    4800.0 1600.0
    


```python
B1.cal_all_reactions()
B1.__dict__
```




    {'name': 'B1',
     'L': 20,
     'loads': [{'load_type': 'point', 'load_value': 6400, 'distance_from_a': 15},
      {'load_type': 'point', 'load_value': 3200, 'distance_from_a': 4}],
     'SFD': [],
     'BMD': [],
     'R_a': 5440.0,
     'R_b': 4160.0,
     'reactions': (5440.0, 4160.0),
     'P': 3200,
     'a': 4}



# Rewrite this in python

### a typical day of a small civil engineering potato

1.  read drawing
-  input geometry
-  calculate reaction
-  calculate SFD,BMD
-  section capacity check
-  repeat

![beam](https://structx.com/Beam_Pictures/008-Simple_Beam_Formulas_PL_Resultant_Shear_Moment_Deflection.png)

https://structx.com/Beam_Formulas_008.html

-   FBD = free body diagram
-   SFD = shear force diagram
-   BMD = bending moment diagram

-   a & b = distance to point load, in or m
-   E = modulus of elasticity, psi or MPa
-   I = second moment of area, in4 or m4
-   L = span length under consideration, in or m
-   M = maximum bending moment, lbf.in or kNm
-   P = total concentrated load, lbf or kN
-   R = reaction load at bearing point, lbf or kN
-   V = maximum shear force, lbf or kN
-   ∆ = deflection or deformation, in or m
-   x = horizontal distance from reaction point, in or m
