variants of the curvature tensor

1. take the trace on the 1st and 3rd indices:

the ricci curvature tensor.

the only traces that make sense are between 1st and 3rd or between 2nd and 4th because of symmetries/antisymmetries

$R_{\mu \nu}$



$$R_{\mu \nu} = \partial_\alpha \Gamma^\alpha ...$$

trace on any other pair of indices is either zero or related using symmetry

10 components in 4d, sort of like "half" of the riemann tensor

1'. traces of Ricci: 

$$g^{\mu \nu} R_{\mu \nu} \equiv R = R^\mu_\mu$$

**Ricci scalar** or **curvature scalar**

2. **Weyl Tensor**

$$C_{\alpha \mu \lambda \sigma} \equiv R_{\alpha \mu \lambda \sigma} - ... + ... $$

- only defined for $n \ge 3$ 
- has the same symmetries as riemann, but designed such that *trace on any pair of indices is zero*.

number of independent components:

> heuristically, by counting number of indepdent components, Riemann Tensor = Weyl Tensor (10) + Ricci Tensor (10)

- Ricci is closely related to sources of gravity (in non vacuum)
- Weyl describes gravity in vacuum

### Trick for Weyl: conformal transformation (not that important RN)

### Breakdown of parallelism

Initially parallel geodesics, characterize how they deviate as one moves along.

Consider two nearby geodesics, each parameterized by affine parameter $\lambda$:

- $\vec{u}$ = tangent vector to 
-

$\vec{\xi}$ points from events at a particular \lambda on \gamma_{\vec{u}} to events at some 

$$\vec{\xi} = \vec{x}(\gamma_\vec{v}, \lambda) - \vec{x}(\gamma \vec{u},\lambda)$$

assume the curves begin parallel:

$$\vec{u}(\lambda_0) = \vec{v} (\lambda_0) $$

This implies 

$$(p^\alpha \nabla_\alpha \xi^\beta)|_{\lambda_0} = 0$$

use as a boundary condition

goal now: develop an "acceleration eq." for \xi^\alpha by comparing geodesics along \gamma

...

Different between geodesic equations give us an acceleration of the difference:

...

Not bad! however, not tensorial. EG, d/d\lambda = u^\alpha \partial_\alpha we want to reexpress as much as possible using covariant derivatives. try to get something that will be invariant in all reference frames

$$\frac{ D  }{ d \lambda } \equiv u^\alpha \nabla_\alpha$$

\frac{ D \xi^\alpha  }{ d \lambda^2 } = u^\beta \nabla_\beta \xi^\alpha = u^\beta \partial_\beta \xi^\alpha + u^\beta \Gamma^\alpha_{\beta \mu} \xi^\mu


...

\rightarrow 

(eq. of geodesic deviation)

we get the riemann curvature tensor!

Equation of geodesic deviation: gives us a covariant tensorial! notion of the aciton of tides. 

The second derivative of the metric is the truly important part. this ends up being the key equaiton describing tides. In FFF, there is no gravitaitonal acceleration, then you'd say then what does gravity do? TIDES!

### recap

recap: riemann is commutator of covariant derivatives

\rightarrow equivaltn to our holonomic definition.

A. [\nabla_\alpha, \nabla_\beta] \nabla_\gamma p_\delta = - R^\mu_\gamma\alpha\beta \nabla_\mu p_\delta - R^\mu \delta_{\alpha \beta} \nabla_\delta p_\mu
B. \nabla_\alpha [\nabla_\beta, \nabla_\gamma] p_\delta = \nabla_\alpha(-R^\mu_{\delta\beta\gamma} p_\mu)



you add up all even premutations, and subtract off odd permutations

= LHS of B, antisymmetrized


antisymmetrization makes the equations equal! LHSs are clear, now examine RHSs:


\nabla_{[ \alpha} R_{\beta \gamma] \mu \delta} = 0

$$
nabla_\alpha R_{\beta \gamma \mu \delta} 
+ nabla_\beta R_{ \gamma \alpha \mu \delta}
+ nabla_\gamma R_{\alpha \beta \mu \delta} 
= 0
$$