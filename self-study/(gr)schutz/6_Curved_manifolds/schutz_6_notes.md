# 6. Curved Manifolds

Because Schutz does such a good job with clarity, the notes here only highlights key points and eqs. 

## Review of tensor algebra

1. a tensor field defines a tensor at every point
2. vectors and 1-forms are linear operators on each other, producing real numbers
3. tensors are linear operators on vectors and 1-forms, producing real numbers
4. If two tensors of the same type have equal components in a given basis, they have
equal components in all bases and are said to be identical (or equal, or the same). Only tensors of the same type can be equal. In particular, if a tensor’s components are all zero in one basis, they are zero in all, and the tensor is said to be zero.
5. A number of manipulations of components of tensor fields are called ‘permissible tensor operations’ because they produce components of new tensors:
    1. Multiplication by a scalar field produces components of a new tensor of the same type.
    2. Addition of components of two tensors of the same type gives components of a new tensor of the same type. (In particular, only tensors of the same type can be added.)
    3. Multiplication of components of two tensors of arbitrary type gives components of a new tensor of the sum of the types, the outer product of the two tensors.
    4. Covariant differentiation (to be discussed later) of the components of a tensor of type $\begin{pmatrix}N\\M\end{pmatrix}$ gives components of a tensor of type $\begin{pmatrix}N\\M+1\end{pmatrix}$ .
    5. Contraction on a pair of indices of the components of a tensor of type $\begin{pmatrix}N\\M\end{pmatrix}$ produces components of a tensor of type $\begin{pmatrix}N-1\\M-1\end{pmatrix}$. (Contraction is only defined between an upper and lowe rindex)
6. Ifanequationisformedusingcomponentsoftensorscombinedonlybythepermissible tensor operations, and if the equation is true in one basis, then it is true in any other. This is a very useful result. It comes from the fact that the equation (from (5) above) is simply an equality between components of two tensors of the same type, which (from (4)) is then true in any system

### Lengths and Volumes

$$l = \int_{\lambda_0}^{\lambda_1}|\vec{V} \cdot \vec{V}|^{1/2} d\lambda$$


## Covariant differentiation

### Christoffel Symbol (5.75)

$$\Gamma^\gamma_{\beta\mu} = \frac{1}{2}g^{\alpha \gamma}(g_{\alpha\beta,\mu}+g_{\alpha\mu,\beta}-g_{\beta\mu,\alpha})$$

$$V^\alpha_{,\beta} = \frac{\partial V^\alpha}{\partial x^\beta}$$

$$V^\alpha_{;\beta} = \frac{\partial V^\alpha}{\partial x^\beta} + V^\mu \Gamma^\alpha_{\mu \beta}$$

$$P_{\alpha;\beta} = P_{\alpha,\beta} - \Gamma^\mu_{\alpha \beta} P_\mu$$

$$T^{\alpha \beta}_{;\gamma} = T^{\alpha\beta}_{,\gamma} + \Gamma^\alpha_{\mu \gamma}T^{\mu \beta} + \Gamma^\beta_{\mu \gamma}T^{\alpha \mu}$$

### metric

$$g_{\alpha \beta;\gamma} = 0 $$

in any basis

### divergence

$$V^\alpha_{;\alpha} = V^\alpha_{,\alpha} + \Gamma^\alpha_{\mu\alpha} V^\mu$$

### Parallel Transport

Let vector $V$ be taken by a curve parameterized by $\lambda$, parallel transport means

$$\frac{dV^\alpha}{d\lambda} = 0 $$

### geodesic

a geodesic is parallel transport of parallel line, generalization of the idea of "staight line".

In curved space, parallel lines when extended do not remain parallel.

## curvature tensor

riemann curvature tensor: quantifying the amount of change of parallel transport of a vector around a infinitesimally small rectangular loop.

$$R_{\alpha \beta \mu \nu} = -R_{\beta \alpha \mu \nu} = -R_{\alpha \beta \nu \mu} = R_{\mu \nu \alpha \beta}$$
$$R_{\alpha \beta \mu \nu} + R_{\alpha \nu \beta \mu} + R_{\alpha \mu \nu \beta} = 0$$

it has a relationship to commutator:

$$[\nabla_{\alpha}, \nabla_{\beta}] V^{\nu} = R^{\mu}_{\nu \alpha\beta} V^{\nu}
$$


### bianchi identities

$$R_{\alpha\beta\mu\nu;\lambda} + R_{\alpha\beta\lambda\mu;\nu} + R_{\alpha\beta\nu\lambda;\mu} = 0
$$

### ricci tensor

$$R_{\alpha \beta} \equiv R^\mu_{\sigma \mu \beta} = R_{\beta\alpha}$$

### einstein tensor

$$G^\alpha \beta \equiv R^{\alpha \beta} - \frac{1}{2}g^{\alpha \beta} R = G^{\beta\alpha}$$

$$G^{\alpha \beta}_{;\beta} = 0$$

