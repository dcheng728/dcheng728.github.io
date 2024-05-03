## 1st route to get to geodesic eq.

How do we formulate the kinematics of bodies in curved spacetime?

Go to LLF, consider a "test mass": no charge, no spatial extent, no spin - just a pure point mass. Only "force" is gravity, which we no longer consider to be a force in the usual sense.

In this frame, trajectory is obvious: particles move in a "straight line" !

$$
x^\alpha = x^\alpha_0 + u^\alpha \tau
$$

What does "straight" mean? Trajectory keeps goign in the direction it started in: it **parallel transports** its tangent vector.

Consider trajectories parameterized by $\lambda$: $u^\alpha \equiv dx^\alpha /d\lambda$ is the tangent to the trajectory.

A curve which parallel transports its own tangent vector satisfies

$$
u^\alpha \nabla_\alpha u^\beta = 0
$$

$$
\nabla_{\vec{u}}\vec{u} = 0
$$

$$
D \vec{u} / d \lambda = 0
$$

Expand:

$$
u^\alpha \frac{\partial u^\beta}{\partial x^\alpha} + \Gamma^\beta_{\alpha \mu} u^\alpha u^\mu = 0
$$

or

$$
\frac{du^\beta}{d\lambda} + \Gamma^\beta_{\alpha \mu} u^\alpha u^\mu = 0
$$

$$
\frac{d^2 x^\beta}{d \lambda^2} + \Gamma^\beta_{\alpha \mu} \frac{\partial x^\alpha}{\partial \lambda} \frac{\partial x^\mu}{\partial \lambda} = 0
$$

These are known as the "Geodesic Eq". Curves that solve them are known as geodesics. 65% of scott's papers are on variants of this equation related to black holes.

This is the leading piece of the motion related to motion.

Aside: more general form, move vector in a parallel fashion, but allow its normalization to change (of course this is still parallel transport by definition above):

$$
\frac{D u^\alpha}{d \lambda^*} = K(\lambda^*) u^\alpha
$$

We can always reparameterize such that the RHS is zero:

Imagine $v^\alpha = \frac{ d x^\alpha }{ d \lambda } \quad v^\alpha \nabla_\alpha v^\beta = 0$

Parameterization with RHS = 0 is called **affine parameterization**.

Intuition: affine parameters corresponds to uniformly spread ticks on geodesics in the LLF. For timelike trajectories, very natural choice is proper time $\tau$

reparameterization that leaves it affine:

$$
\lambda' = a \lambda + b
$$

which corresponds to shifting the origin and changing tick spacing.

This is the only class of affine-preserving reparameterization.

## 2nd route to get to the geodesic eq.

consider all curves which begin at P and end at Q. Proper time elapsed by an observer who follows one of the paths is

(...)

Now, consider motions in path:

define the action Imagine

As an action for particle motion!

Here, Hughes went through the procedure of varying the path and demand the time elapsed is extremized.

Hit with $g^{ \mu \gamma}$, we obtain

$$
\boxed{\frac{ d d^\mu }{ d \tau } + \Gamma^{ \mu }_{ \alpha \beta } u^\alpha u^\beta = 0}
$$

Recap: geodesics generalize "straight" trajectories to curved spacetime.

Parallel transport: no force acts, so tangent moves parallel to itself.

Extremization: geodesics generalize motion of "shortest distance between 2pts".


Side note: can rewrite in terms of momentum:


$$ u^\alpha \nabla_\alpha u^\beta = 0 \rightarrow p^\alpha \nabla_\alpha p^\beta = 0$$


$$\rightarrow m \frac{ d p^\beta }{ d \tau } + \Gamma^{ \beta }_{ \alpha \gamma } p^\alpha p^\gamma = 0$$

useful rewriting: define an affine parameter by

$$\Delta \lambda \equiv \Delta \tau /m$$

Then $ p^\alpha = \frac{ d x^\alpha }{ d \lambda }$

can take limit $ m \rightarrow 0 $, $ \Delta \tau \rightarrow 0$, 
but $\Delta\tau \rightarrow \text{constant}$ gives us a geodesic equation that is suitable for null geodesics!

### one further trick: rewrite geodesic eq. for downstairs momentum:

$$p^\alpha(\nabla_\alpha p_\beta) = 0$$

this is ok because metric commutes with $\nabla_\alpha$. This is really important and will be used alot!

$$\rightarrow m \frac{ d p_\beta }{ d \tau } - \Gamma^{ \gamma }_{ \beta \alpha } = 0$$

$$\rightarrow \boxed{m \frac{ d p_\beta }{ d \tau } = \frac{ 1 }{ 2 } \partial_\beta g_{\alpha\beta} p^\alpha p^\gamma}$$

utility: if metric is independent of $x^\beta$, then $p_\beta$ is a conserved constant on the geodesic! This is usually the easiest way to find conserved quantities.

Further, there exists a killing vector $\vec{\xi}^\beta$. 
Examine how scalar $p_\beta \xi_\beta$ evolves on geodesic:

$$p^\alpha \nabla_\alpha (p^\beta \xi_\beta) = ...$$

$$= 0 $$
killing's eq.!

$p^\beta$ is constant on trajectory!

### examples in action:

$$\partial_t g_{\alpha \beta} = 0 \rightarrow \text{ there exists a time like killing vector} \vec{\xi}^T$$

$$\rightarrow p_0 = -E$$

conserved energy!

$$= - p^\beta \xi^T_\beta$$

coord. invariant expression





