"""
Linear algebra - Linear behavior makes things simpler

1. Vectors - Concrete and abstract, a list of objects
- Geometric and algebraic perspectives
- Dimensions = length
- Transformation of a point into another point in the 2d space
- Operations
Vectors can be added and multiplied (by numbers(*) and other vectors(+))
Vectors (a + b + c => point D, sum = AD)
Vector v(A, B) * (-3) = -3v(B, A), change of direction
Two vectors are co-linear if they lie on  parallel segments (one way co-linear, different way co-linear)
No such thing as parallel vectors

Scalar product (inner product) of vectors:
vector a * vector b = |a||b|cos(theta) or sum(ax*bx + ay*by)

Outer product: (3d)
|a X b|sin(theta)n <= Vector of normal direction (3rd vector top)
Result of vector c is _|_ (orthogonal) to both a and b and has direction
Determining the direction if angle < 180 degrees after translating a to b (Counter clockwise rotation)
a * b =>, b * a <= as direction, a*b is not equal to b*a in this case
Wedge product graph

- Vector spaces => Axioms
A set of elements and a field, usually R or C
- Functional analysis

- Basis vectors (except co-linears, n independent vectors)


2. Matrices n * n, row vector, column vector
All m * n matrices form a vector space
- Definition

- Properties

- Operations
Sum - element by element for n * n matrix
Multiplication - number of columns from the first to be equal to number of rows from the second,
the result from multiplication is a matrix of size number of rows from the first * number of columns from the second
e.g. 2x3 * 3*4 => result 2 * 4
Transposition => Turning row into columns and vice versa

3. Linear transformations
Linear transformations => Transforming the space, a single point remains the same (streching)
N.B.! If we know how the basis vectors are transformed, we can transform every other vector

Transformation matrix
Determinant - A measure of how much the unit area changes
4. Linear systems
"""