example geodesic: a spacetime we will soon derive,

$$ds^2 = - (1+2\phi) dt^2 + (1-2\phi)(dx^2 + dy^2 + dz^2)$$


consider slow motion in the spacetime::

$$p^\alpha = (E,P)$$

what does free fall look like in this spacetime?

geodesic equation:

$$m \frac{ d p^\beta }{ d \tau } + \Gamma^{ \beta }_{ \mu \nu } = 0$$

the second term will be dominated by $$\mu = \nu = 0$$

$$\rightarrow \Gamma^{ i }_{ 0 0 } = -\frac{ 1 }{ 2 } (1-2\phi)^{-1} \delta_{ij} \partial_j(-2\phi)$$

$\rightarrow \boxed{\frac{ d p^i }{ d \tau } = -m \delta^{ij} \partial_j \phi}$

$\phi$ is newtonian gravitational potential: 
motion in this spacetime is equiv to motion under influence of newtonian gravitational force

einstein screwed up a lot

### quantifying curvature: 

curvature tells us about the breakdown of parallelism: two initially parallel trajectories do not remain parallel. will manifest as geodesic deviaiton.

this operation is called a **holonomy**

human as a holonomy:

https://mathworld.wolfram.com/HolonomyGroup.html

consider parallel transport of a vector $V^\alpha$ around this loop:

basically same illustration as schutz



$$\boxed{
R^\alpha_{\mu \lambda \sigma} 
\equiv 
\partial_\lambda \Gamma^{ \alpha }_{ \sigma \mu }
-
\partial_\sigma \Gamma^{ \alpha }_{ \lambda \mu }
+
\Gamma^{ \alpha }_{ \lambda \nu}
\Gamma^{ \nu }_{ \sigma \mu}
-
\Gamma^{ \alpha }_{ \sigma \nu}
\Gamma^{ \nu }_{ \lambda \mu}s
}$$

"**Tje Riemann Curvature Tensor**"

note: truly tensorial, despite construction from $\Gamma$s!

Equivalent definition: commutator of covariant derivatives

$$[\nabla_\lambda,\nabla_\sigma] V^\alpha = R^\alpha_{\mu\lambda\sigma} V^\mu$$

$$[\nabla_\lambda,\nabla_\sigma] p^\alpha = -R^\alpha_{\mu\lambda\sigma} p^\mu \leftarrow this is written wrong in schutz$$

#### more about Riemann tensor

- 4 index tensor, 4 values each, 256 values
- it has a lot of symmetries. In fact, for $n$ dimensional manifold, it will have DOF

$$\frac{ n^2(n^2-1) }{ 12 }$$


### more general approach

"curvature coupling": when we examine processes that occur over an extended region, the urvature tensor plays an important role.

discussion of geodesics, strictly holds only for test bodies: zero size monopoles (that dont generate gravity)

more general bodies: motion involves coupling to riemann essentially, the body with enough extent that different pts in the body have different tangent spaces

#### example: 

earth's extent couples to riemann tensors of the sun + moon changes the motion slightly, just precession of equinoses.

#### another example:

spin angular momentum constitutes "structure" beyond monopole, couples to curvature. find equation of motion

$$p^\alpha \nabla_\alpha p^\beta ~ R^\beta_{\mu\nu\sigma} u^\mu S^{\nu \sigma}$$



## The Riemannian tensor

$$\Gamma^\lambda_{\mu\nu} = \frac{1}{2} g^{\lambda \sigma} (\partial_\nu g_{\sigma \mu} + \partial_\mu g_{\sigma \nu} - \partial_\sigma g_{\mu \nu})$$





#### LLF
Go to LLF, the christoffel symbols vanish (derivatives do not) 

$$R_{\alph \mu \lambda \sigma} = g_{\alpha \nu} [\partial_\lambda \Gamma^\nu_{\sigma \mu} - \partial_\sigma \Gamma^\nu_{\lambda \mu} ]$$

$$=\partial_\lambda \Gamma_{\alpha \sigma \mu} - \partial_\sigma \Gamma_{\alpha \lambda \mu}$$

after staring for a while, "notice" the following symmetries

1. $R_{\alpha \mu \lambda \sigma} = - R_{\alpha \mu \sigma \lambda}$
2. $R_{\alpha \mu \lambda \sigma} = - R_{\mu \alpha \lambda \sigma}$
3. $R_{\alpha \mu \lambda \sigma} = R_{\lambda \sigma \alpha \mu}$
4. $R_{\alpha \mu \lambda \sigma} + R_{\alpha \lambda \sigma \mu} + R_{\alpha \sigma \mu \lambda } = 0$
4'.

riemann normal coordinates

poisson, "a relativist' toolkit", sec 1.11.


