## 8 more transport

## Lie Transport and Lie Derivative

recap: introduced motion of parallel transport, needed to compare vectors/tensors at different points in manifold

there are two approaches:

1. rigorous: noting that naive partial derivative contaminates result with terms that don't leave us with tensorial results, we define a derivative operator with a "connection":

$$
\nabla_\beta A^\alpha = \partial_\beta A_\alpha + \Gamma^\alpha_{\beta\mu}A^\mu
$$

requirement that $\nabla_\beta g_{\mu \nu} = 0 \rightarrow \Gamma^\alpha_{\beta \mu} A^\mu$ is the christoffel defined earlier => this derivative is just the covariant derivative.

2. physical: go to LLF (locally lorentz frame). parallel transport reduces to just requiring components to slide along curve in manifold without change; just $\partial_\beta A^\alpha$ is good enough in LLF.

In LLF, the $\partial_\beta A^\alpha = \nabla_\beta A^\alpha$ since the christoffel symbol vanish in LLF.
This means $\nabla_\beta A^\alpha$ is tensorial. then invoke what is tensorial in 1 frame is tensorial in all.

## another notion of transport

suppose we are comparing vectors at two points $x^\alpha$ and $x'^\alpha = x^\alpha + u^\alpha d\lambda$ (note this is the form of a linear approximation), where $u^\alpha = \frac{\partial x^\alpha}{\partial \lambda}$. we now regard the shift as a coordinate transformation.

$$
A^\alpha_{LT}(P \rightarrow Q) = \frac{\partial x'^\alpha}{\partial x^\beta} A^\beta
$$

$$
=(\delta^\alpha_\beta + (\partial_\beta u^\alpha)d\lambda)A^\beta(P)
$$

$$
\rightarrow A^\alpha_{LT}(P \rightarrow Q) = A^\alpha(P) + (\partial_\beta u^\alpha)A^\beta(P)d\lambda)
$$

Meanwhile vector field at $Q$ can be obtained by Taylor expansion:

$$
A^\alpha(Q) = A^\alpha (x^\beta + dx^\beta)
$$

$$
=A^\alpha(x^\beta) + dx^\beta(\partial_\beta A^\alpha)|_P
$$

$$
=A^\alpha(P) + (u^\beta d\lambda)(\partial_\beta A^\alpha)
$$

Define **lie derivative** as difference between the two

$$
L_{\vec{u}} A^\alpha \equiv [A^\alpha(Q)-A^\alpha_{LT}(Q)]/d\lambda
$$

$$
= u^\beta \partial_\beta A^\alpha - A^\beta \partial_\beta u^\alpha
$$

It's not hard to show that

$$
L_{\vec{u}} A^\alpha = u^\beta \nabla_\beta A^\alpha - A^\beta \nabla_\beta u^\alpha
$$

the connection coefficients (christoffel symbols) just cancel out

this means that this object - "the lie derivative of $\vec{A}$ along $\vec{u}$" - is itself tensorial

Common notation: $L_{\vec{u}} \vec{A} \equiv [\vec{u}, \vec{A}]$

Repeat exercise for a scalar:

$$
L_{\vec{u}} \phi = u^\alpha \nabla_\alpha \phi
$$

1 form: use $p^\alpha A_\alpha = $ scalar, take Lie derivative of total, find

$$
L_{\vec{u}} p_\alpha = u^\beta \partial_\beta p_\alpha + p_\beta \partial_\alpha u^\beta
$$

$$
= u^\beta \nabla_\beta p_\alpha + p_\beta \nabla_\alpha u^\beta
$$

tensor:

$$
L_{\vec{u}} T^\alpha_\beta = u^\mu \partial_\mu T^\alpha_\beta - T^\mu_\beta \partial_\mu u^\alpha + T^\alpha_\mu \partial_\beta u^\mu
$$

## utility

First define **Lie transport**: curve $\gamma$ with tangent $\vec{u} = d\vec{x}/d\lambda$. A tensor is "Lie transported along $\vec{u}$ if $L_{\vec{u}}(\text{tensor}) = 0$. (used a lot in fluids: $\vec{u}$ defines a flow line)

If a tensor is lie transported, here we can define the following coordinates: $x^0 = \lambda$ on the curve; $x^1, x^2, x^3 = $ constant on the curve.

Then, $u^\alpha \equiv \frac{dx^\alpha}{d \lambda} \equiv \delta^\alpha_0 \rightarrow \partial_\mu u^\alpha$

Then, $L_{\vec{u}}(\text{tensor}) = 0 \rightarrow \frac{\partial \text{tensor}}{\partial x^0} = 0$

In these coordinates, the tensor is ocnstant as we slide along the curve! lie derivative gives us a covariant, **frame independent** way to discuss a symmetry of a tensor field.

### example

example: suppose the tensor is the metric. Let us say there is some vector $\vec{\xi}$ such that the metric is Lie transported along $\vec{\xi}$:

$$
L_{\vec{\xi}} g_{\alpha \beta} = 0
$$

1. there exists a coordinate $x^0$ such that $\frac{\partial g_{\alpha \beta}}{\partial x^0} = 0$: metric is constant wrt that coord. (converse also holds: if the metric is constant wrt some coord, then a vector $\vec{\xi}$ exists such that the metric is Lie transported along $\xi$)
2. expand the lie derivative:

$$
L_{\vec{\xi}} g_\alpha\beta = 0
$$

$$
\rightarrow \xi^\gamma \nabla_\gamma g_{\alpha \beta} + g_{\alpha \gamma} \nabla_\beta \xi^\gamma = 0
$$

$$
\nabla_\alpha \xi_\beta + \nabla_\beta \xi_\alpha = 0
$$

This is Killing's Equations, named after Wilhelm Killing.

$\vec{\xi}$ is called killing vector - describes a symmetry of spacetime. (note: used fact that metric commutes with $\nabla_\alpha$)

### Tensor densities

 quantities that transform, almost but not quite, like tensors. Off by a factor that looks like a determinant of a transformation matrix.

Most important tensor densities: levi-civita symbol, metric determinant.

#### levi-civita

$$
\begin{aligned} \tilde{\epsilon}_{\alpha \beta \gamma \delta} &= +1 &\text{for 0123 and even perm.} \\
&= -1 &\text{for odd perm.} \\
&= 0 &\text{for any repeated index}\end{aligned}
$$

Theorem: For any 4x4 matrix,

$$
\tilde{\epsilon}_{\alpha \beta \gamma \delta} M^\alpha_\mu M^\beta_\nu M^\gamma_\rho M^\delta_\sigma = \tilde{\epsilon}_{\mu\nu\rho\sigma} |M| \leftarrow \text{determinant of }M
$$

Choose $M = \frac{\partial x^\mu}{\partial x^{\mu'}}$ -- coord trans matrix:

$$
\tilde{\epsilon}_{\alpha' \beta' \gamma' \delta'} = |\frac{\partial x^{\mu'}}{\partial x^\mu}| \tilde{\epsilon}_{\alpha \beta \gamma \delta} 
\frac{\partial x^\alpha}{\partial x^{\alpha'}} 
\frac{\partial x^\beta}{\partial x^{\beta'}}
\frac{\partial x^\gamma}{\partial x^{\gamma'}}
\frac{\partial x^\delta}{\partial x^{\delta'}}
$$

NOT a tensor trans. law! off by a factor of the jacobian.

We call this "Tensor density of weight 1"

Now look at metric:

$$
g_{\alpha' \beta'} = \frac{\partial x^\alpha}{x^{\alpha'}} \frac{\partial x^\beta}{x^{\beta'}} g_{\alpha \beta}
$$

$$
\rightarrow g' = |\frac{\partial x^\alpha}{x^{\alpha'}}|^{-2} g \leftarrow \text{determinant of }g_{\alpha \beta}
$$

Tensor density of weight -2.

To convert a tensor density of weight $w$ into a tensor, just multiply by $|g|^{w/2}$

#### example:

$$
\epsilon_{\alpha \beta \gamma \delta} \equiv \sqrt{|g|} \tilde{\epsilon}_{\alpha \beta \gamma \delta}
$$

$$
\epsilon^{\alpha \beta \gamma \delta} \equiv 1/\sqrt{|g|} \tilde{\epsilon}^{\alpha \beta \gamma \delta}
$$

This is an important example: use these tensors to form covariant volume operators:

$$
dV \equiv \sqrt{|g|} \tilde{\epsilon}_{\alpha \beta \gamma \delta} dx_0^\alpha dx_1^\beta dx_2^\gamma dx_3^\delta
$$

$$
= \sqrt{|g|} dx^0 dx^1 dx^2 dx^3
$$

$$
ds^2 = dr^2 + r^2 d\theta^2 + r^2 \sin^2 \theta d \phi^2
$$

if basis is orthogonal.

Intuition: In 3-D, spherical coordinates:

$$
g_{\alpha \beta} = \text{diag}(1, r^2, r^2 \sin^2 \theta)
$$

$$
dV = \sqrt{r^4 \sin^2 \theta} dr d\theta d\phi = r^2 \sin \theta dr d\theta d\phi
$$

---

### party trick: computing some components of christoffel symbol

Determinant of metric extremely useful!

$$
\begin{align}
\Gamma^\mu_{\mu \alpha} &= g^{\mu \beta} \Gamma_{\beta \mu \alpha} \\
&= 1/2 g^{\mu \beta} (\partial_\mu g_{\alpha \beta} + \partial_\alpha g_{\beta \mu} - \partial_\beta g_{\mu \alpha}) \\
&= 1/2 g^{\mu \beta} g_{\mu \beta,\alpha}
\end{align}
$$

TOSHOW: the above is also given by

$$
= 1/\sqrt{|g|} \partial_\alpha(\sqrt{|g|})
$$

$$
= \partial_\alpha (\ln \sqrt{|g|})
$$

Proof:

Consider some matrix $M$. consider the following variation:

$$
\delta \ln (\text{det} M) = \ln \left[ \text{det}(M + \delta M) \right] - \ln (\text{M})
$$

$$
= \ln [ \frac{\text{det}(M +\delta M)}{\text{det} M}
$$

$$
= \ln [\text{det} [1 + M^{-1} \cdot \delta M]]
$$

last line, used $(\text{det} M)^{-1} = \text{det} M^{-1}$ and $(\text{det} M) (\text{det} N) = \text{det} (M \cdot N)$.

Useful identity: If $\epsilon$ is a "small" matrix, then

$$
\text{det}  [1 + \epsilon] \cong 1 + \text{Tr} (\epsilon)
$$

where $\text{Tr} (\epsilon) = g^{\alpha \beta} \epsilon_{\alpha \beta} = \epsilon^\alpha_\beta$, a scalar.

so,

$$
\delta \ln (\det M ) = \ln [ 1 + \text{Tr} (M^{-1} \cdot \delta M)]
$$

$$
\cong \text{Tr} (M^{-1} \cdot \delta M)
$$

now $M \rightarrow g_{\alpha \beta}$:

$$
\delta \ln |g| = \text{Tr} [g^{\mu \beta} \delta g_{\beta \gamma}]
$$

$$
= g_{\mu \beta} \delta g_{\beta \mu}
$$

$$
\rightarrow \partial_\alpha \ln |g|  = g^{\mu \beta} \partial_\alpha g_{\beta \mu}
$$

$$
\rightarrow \Gamma^\mu_{\mu \alpha} = \frac{1}{2} g^{\mu\beta} \partial_\alpha g_{\beta \mu}
$$

$$
= \partial_{\alpha} \ln |g|^{1/2}
$$

TADA

### Utility: spacetime divergence of vectors

$$
\nabla_\alpha A^\alpha + \Gamma^\alpha_{\alpha \beta} A^\beta = \partial_\alpha A^\alpha + \Gamma^\beta_{\beta \alpha} A^\alpha
$$

$$
= \partial_\alpha A^\alpha + \frac{A^\alpha}{\sqrt{|g|}} \partial_\alpha (\sqrt{|g|})
$$

$$
\rightarrow \boxed{\nabla_\alpha A^\alpha = \frac{1}{\sqrt{|g|}} \partial_\alpha (\sqrt{|g|} A^\alpha)}
$$

Only involves partial derivatives! "This is awesome" -Hughes

Also gives a nice gauss's theorem:

$$
\int_V (\nabla_\alpha A^\alpha) \sqrt{|g|} d^4 x = \int \partial_\alpha (\sqrt{|g|} A^\alpha) d^4 x
$$

$$
= \int_{\partial V} A^\alpha \sqrt{|g|} dZ_\alpha
$$

can we do this for tensors?

1. NO: $\nabla_\alpha A^{\alpha \beta} = \partial_\alpha A^{\alpha \beta} + \Gamma^{\alpha}_{\alpha \gamma} A^{\gamma \beta} + \Gamma^\beta_{\alpha \gamma} A^{\alpha \beta}$. The first term with $\Gamma$ can be exploited because it has an contraction. But the second term is ugly, unless $A^{\alpha \beta}$ is antisymmetric - the 2nd term dies.
2. Not useful! $\nabla_\mu T^{\mu \nu}$ is a 4-vector. Can't integrate this up to make a conservation law: comparing data at different tangent spaces. There is something interesting here. $\nabla_\mu T^{\mu \nu}$
   is a local conservation law, in GR we can not take a local conservation law and promote it to a global one.
