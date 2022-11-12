"""
1. Polynomials - Sum of monomials - ax**2 + bx + c (bx**1 + cx**0)
lists => Saving the data from ascending order of X in monomial [1, 2, 3] => 1x**0 +2 2x**1 + 3x**2
the power of X is >=0, irrational equations less than 0

-Sum of polynomials:
import numpy.polynomial.polynomial as p
p.polyadd([-8, 5, 2], [-2, 0, 0, 0, 3])

-Multiplication of polynomials:
multiplication_result = p.polymul([-8, 5, 2], [-2, 0, 0, 0, 3])

-Ordering the polynomial using sympy:

import sympy
multiplication_result = p.polymul([-8, 5, 2], [-2, 0, 0, 0, 3])
x = sympy.symbols("x")
sympy.Poly(reversed(multiplication_result), x)

2. Sets (Множества) {x e R | x >= 0} - Създаване на подмножество на множеството на реалните числа, >=0, с код
{x for x in range(-50, 50 if x >=0}
- subsets, union, difference, symmetric difference

Binary operators: (Union vs Intersection (-) relationship) => De Morgan
set1 & set2
set1 | set2

3. Functions - Mapping from one thing to another
Math notation f: x->y
Domain - > A set of inputs X
Codomain (range) -> A set of outputs Y
The function is the relationship between the domain and the codomain

ONE INPUT -> ONE OUTPUT in maths

f(g(x))

4. Complex numbers (x ** 2 - a = 0), a = -1, square roots of negatives
- Number fields - A collection of values with operations "Plus" and "Times"
i - imaginary unit, possible solution of x ** 2 = -1

- Geometric interpretation - Same thing, different approach
x - Real, y - Imaginary
Decart coordinates of a point - (x, y)
Polar coordinates of a point - (x + b*y)

Z = a + bi = p(cos(fi) + i * sin(fi)) => Polar form, Euler's

5. Fundamental theorem of Algebra - If an equation is of power of X, the roots are X count
"""