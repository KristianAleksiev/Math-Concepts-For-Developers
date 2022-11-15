"""
1. Limits
Lim от ф(х), при х клонящо към а
When the functions is changed, how the output of it changes
delta distance > 0

2. Derivatives
- The rate of change of a function f(x) as its argument x changes,
is called the first derivative of f(x) with respect to x

- Geometrically, the derivative at a given point is equal to the slope of the tangent line to the function at this point
f'(x) = tg(l)

- Chain rule for a derivative of a function composition
f(g(x))' = f'(g(x)).g'(x) - Neural networks, forward/backward propagation

if f'(x) = 0 => Local extrema (max or min), the extrema is determined by the second derivative of f(x)

3. Integrals - Areas and accumulation
- Antiderivative (primitive function) of f(x) or => F'(x) = f(x)

- Fundamental theorem of Calculus =>
The indefinite integral of a function is related to its antiderivative and can be reversed via differentiation &
The definite integral of a function can be computed using one of its infinitely many antiderivatives.
Differentiation and integration are inverse functions

4. Calculus in many dimensions
- Partial derivatives and a combination of them (vector of derivatives) => Gradient

5. Gradient descent - Градиентен метод
- Optimization method, used for finding local extrema
- In which direction the function is rising the most
- The gradient shows where the steepest rise in the slope is
- Positive gradient takes us the the maximum, vice-versa
- Not guaranteed to find the global extrema
"""