# Cauchy Riemann Condition
an if and only if condition for a complex function to be analytic (complex differentiable).

The notation for complex function is

$$f(z) = f(x+iy) = u(x,y) + i v(x,y)$$

The cauchy riemann condition states that $f$ is analytic if and only if

$$\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}, \quad \text{and} 
\frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}$$

Notice the resemblance of this with the condition for a coordinate transformation to be canonical.

- an immediate corollary is that the real and imaginary parts of an analytic function separately satisfy the 2D laplacian. 
Recall that Laplacian defines the electrostatic potential in charge-free volume. 

# conformal mapping

the fact that the real and imaginary parts of analytic function satisfies 2D laplacian motivates using it for electrostatic potential.
Out of the desire to keep equipotential and field lines at right angle with each other, we are motivated to consider **conformal mapping**,
mappings such that angle at intersections between two lines in the domain are kept for the two lines in the range. 

examples of conformal mapping:
- z -> z + a
- z -> bz
- z -> 1/z
- z -> (az+b)/(cz+d)  this is called homographic transformation

# Complex integral as vector integral

This is done in Hassani 10.4, the idea is that treating complex function f as f = u(x,y) + i v(x,y), and dz = dx + idy. The complex integral can be written as

$$\int f(z) dz = \int (udx - vdy) + i \int (vdx + udy)$$

Then introduce 

$$\vec{A}_1 = (u,-v), \quad \vec{A}_2 = (v,u)$$

the integal can be written as

$$\int f(z)dz = = \int \vec{A}_1 \cdot d\vec{r} + i \int \vec{A}_2 \cdot d \vec{r}, \quad d\vec{r} = (dx,dy)$$

The vector fields $A$ is curlless by cauchy riemann condition.

# Cauchy Integral Thm

Evaluation of function via integral. This turns derivatives of function into integrals as well. 

Under standard analyticity conditions of $f$, we will have

$$f(z) = \frac{1}{2\pi i} \oint_C \frac{f(\xi) d\xi}{\xi - z}$$

This gives expression for derivatives of $f$:

$$f^{(n)}(z) =  \frac{n!}{2\pi i} \oint_C \frac{f(\xi) d\xi}{(\xi - z)^{n+1}}$$

# infinite  complex series

If a power series converges on a circle, then 

if it is all positive powers, it converges for all points inside the circle

if it is all negative powers, it converges for all points outside the circle

# Taylor and Laurent series

A Taylor series consists of positive powers

$$f(z) = \sum_{n=0}^\infty \frac{f^{(n)}(z_0)}{n!}(z-z_0)^n$$

A Laurent series consists of negative powers as well.

$$f(z) = \sum_{n=-\infty}^\infty a_n(z-z_0)^n$$

where 

$$a_n = \frac{1}{2\pi i} \oint_C \frac{f(\xi)d\xi}{(\xi - z_0)^{n+1}}$$

Laurent-series is the most natural generalization of Taylor series.

Notice the -1 term in the laurent series is precisely a contour integral of f. This is the residue at z_0.

$$a_{-1} = \frac{1}{2\pi i} \oint_C f(\xi)d\xi$$