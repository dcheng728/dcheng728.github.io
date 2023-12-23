- [ ] 1.6 
- [ ] 1.10
- [ ] 1.12
- [ ] 1.13
 

electrostatics = coulomb's law at various extents and contexts
- $\rho \rightarrow$  potential $\rightarrow \vec{E} \rightarrow$ force

|ESU|SI|
|--|--|
|k=1|$k=(4\pi\epsilon_0)^{-1}$|
|charge in units of **statcoulomb**|charge in **coulombs**|
|field in statvolts/meter|field in volts/meter|

# delta function in 8 equations
1. $\delta(x-a) = 0$ for $x\neq a$
2. $\int \delta(x-a) dx = 1$
3. $\int f(x)\delta(x-a)dx = f(a)$
4. $\int f(x) \delta'(x-a) dx = - f'(a)$, where $\delta' = \frac{\partial \delta(x-a)}{\partial x}$, $f' = \frac{\partial f(x)}{\partial x}$
5. $\delta[f(x)] = \sum_i |\frac{df}{dx}(x_i)|^{-1}\delta(x-x_i)$
6. $\delta(\vec{x}- \vec{X}) = \delta(x_1-X_1)\delta(x_2-X_2)\delta(x_3-X_3)$
7. $\int_{V}\delta(\vec{x}-\vec{X}) d^3x =$ 1 if $V$ contains $\vec{X}$ else 0
8. $\nabla^2 \frac{1}{|\vec{x} - \vec{x}'|} = -4\pi \delta (\vec{x}-\vec{x}')$
- $\delta$ has units of inverse length 

- $\vec{E}$'s gauss law depends on 1. inverse square law, 2. central force nature, 3. linear superposition

- differential form $\approx$ differential equation
- a vector field can be specified almost completely if $(\nabla \cdot)$ and $(\nabla \times)$ are specified everywhere. This introducees potential
- There is discontinuity of $\sigma/\epsilon_0$ in crossing surface for $\vec{E}$
- Green's function is developed to handle boundary conditions

# boundary conditions
- dirichlet's problem: potential specified on closed surface
- neumann's problem: normal derivatives specified

- green's function satisfy 
$$\vec{\nabla}^2 (\frac{1}{|\vec{x}- \vec{x}'|}) = - 4 \pi \delta(\vec{x}- \vec{x}')$$

## jackson 1.8
- The formula $\Phi(\vec{x}) = \frac{1}{4\pi \epsilon_0} \int \frac{\rho(\vec{x}')}{|\vec{x}-\vec{x}'|} d^3 x'$ becomes inconvenient for certain problems
- green's theorem is developed to handle complicated boundary conditions.
- green's 1st identity: 
$$\int_V (\phi \nabla^2 \psi + \nabla \phi \cdot \nabla \psi)d^3x = \oint_S \phi \frac{\partial \psi}{\partial n} da$$
- green's 2nd identity
$$\int_v (\phi \nabla^2 \psi - \psi \nabla^2 \phi)d^3x = \oint_S \left[ \phi \frac{\partial \psi}{\partial n} - \psi \frac{\partial \phi}{\partial n} \right] da$$
- letting $\psi = \frac{1}{R} \equiv \frac{1}{|\vec{x} - \vec{x}'|}$ gives a formulation for $\Phi$

## jackson 1.9
- jackson proves uniqueness of $\Phi$ using green's identity for both dirichlet and neumann conditions

## jackson 1.10
- green's function must satisfy 
$$\nabla'^2 G(\vec{x},\vec{x}') = - 4\pi \delta(\vec{x}-\vec{x}')$$
it has the most general form of
$$G(\vec{x},\vec{x}') = \frac{1}{|\vec{x}-\vec{x}'|} + F(\vec{x},\vec{x}')$$
with $F$ satisfying the laplace equation inside volume $V$: $\nabla'^2 F(\vec{x},\vec{x}') = 0$
- the freedom in $F$ can be used to eliminate one of the surface integrals in (1.36), which one depends in the type of boundary condition (dirichlet/neumann)
- ### method of images
- the total induced surface charge is the image charge, the negative of the real charge, or some combination of the two.

### Lecture 6:Advanced Electrostatics III:
Green Functions for Poisson’s Equation
Obtaining Green Functions from the Method of Images

- green operated by linear differential operators results in the delta function. see LN pg128.
- Green Function approach. The basic idea is to find the 'impulse' response function for the differential equation: the generalized potential one gets if one has a point-like source. Given the impulse response function, linearity, one can obtain the generalized potential for an arbitrary source function by convolving the impulse response function with that source function.
- The freedom F in G is crucial for satisfying nontrivial boundary conditions
- both F and G are symmetric in their arguments
- LN 3.47 discussion: pg 135 star

- the component F_D of the full Dirichlet Green Function G_D can be determined by the method of images in some cases.

## jackson 1.11
- $W = \frac{1}{2}\int \rho(\vec{x}) \Phi(\vec{x}) d^3 \vec{x} = \frac{\epsilon}{2} \int |\vec{E}|^2 d^3 x$


