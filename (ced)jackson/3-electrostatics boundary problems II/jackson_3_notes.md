- finite element analysis (FEA) encompasses a variety of numerical approaches for the solution of a boundary value problem in physics and engineering
- jackson uses galerkin's method as illustrations, in 2D

- legendre polynomials form a complete set of orthogonal functions on [-1,1]. Thus any function in this range can be expanded in legendre polynomials:
$$f(x) = \sum_{l=0}^{\infty} A_l P_l(x), \quad A_l = \frac{2l+1}{2}\int_{-1}^{1} f(x) P_l(x) dx$$
- problems possessing azimuthal symmetry have solutions of form
$$\Phi(r,\theta) = \sum_{l=0}^\infty [A_l r^l + B_l r^{-(l+1)}] P_l (\cos \theta)$$
- if the range of $\theta$ is restricted, then we might need a special set of legendre polynomials

# 3.5 associated legendre functions and spherical harmonics
- to have finite solutions on [-1,1] the parameter $l$ must be nonzero integer, and integer $m$ takes on $2l+1$ values between $\pm l$. These legendre polynomial are called associated legendre functions $P^m_l (x)$,
$$P^m_l (x) = (-1)^m (1-x^2)^{m/2} \frac{d^m}{dx^m} P_l(x)$$, in rodriguez form: 
$$P^m_l (x) = \frac{(-1)^m}{2^l l!} (1-x^2)^{m/2} \frac{d^{l+m}}{dx^{l+m}}[(x^2-1)^l]$$
- for fixed $m$, $P^m_l$ furnishes an orthogonal set in $l$ on $[-1,1]$: 
$$\int^1_{-1} P^m_{l'}(x) P^m_l(x) dx = \frac{2}{2l+1} \frac{(l+m)!}{(l-m)!} \delta_{l'l}$$
- together with the radial function, we can build a set of function that are orthonormal over $l,m$, on the surface of of a sphere
$$Y_{lm}(\theta,\phi) = \sqrt{\frac{2l+1}{4\pi} \frac{(l-m)!}{(l+m)!}} P^m_l (\cos \theta) e^{im\phi}$$
- $Y_{l-m}(\theta,\phi) = (-1)^m Y^*_{lm}(\theta, \phi)$
$$\int^{2\pi}_0 d\phi \int^\pi_0 (\sin \theta d\phi) Y^*_{l'm'} Y_{lm} = \delta_{l'l} \delta_{m'm}$$
$$\sum_{l=0}^\infty \sum_{m=-l}^l Y^*_{lm}(\theta',\phi') Y_{lm}(\theta,\phi) = \delta(\phi-\phi')\delta(\cos \theta - \cos \theta')$$
- an arbitrary function over the surface of the sphere can be expanded in spherical harmonics
$$g(\theta,\phi) \sum_{l=0}^\infty \sum_{m=-l}^l A_{lm} Y_{lm}(\theta,\phi)$$
$$A_{lm} = \int d \Omega Y^*_{lm}(\theta,\phi) g(\theta,\phi)$$
- the general solution for boundary-value problem in spherical coordinates can be written in terms of spherical harmonics and powers of r in generalization of (3.3)
$$\Phi(r,\theta,\phi) = \sum_{l=0}^\infty \sum_{m=-l}^{l} [A_{lm}r^l + B_{lm} r ^{-(l+1)}]Y_{lm}(\theta,\phi)$$
# 3.6 additional theorems for spherical harmonics
the addition theorem expresses a legendre polynomial of order $l$ in the angle $\gamma$ in terms of products of the spherical harmonics of the angle $\theta,\phi$ and $\theta',\phi'$
$$P_l(\cos \gamma) = \frac{4\pi}{2l+1} \sum_{m=-l}^{l} Y^*_{lm}(\theta',\phi') Y_{lm}(\theta,\phi)$$
