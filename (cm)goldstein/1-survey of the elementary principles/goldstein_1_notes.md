- conservative force: work done independent of path taken in configuration space, $\vec{F} = -\vec{\nabla} V(\vec{r})$
- (*A* exerting force on *B*) = (*A* transferring its momentum to *B*)
- force on systems of particles are distinguished as **external** and **internal**
- weak, strong **law of action and reaction** come hand in hand with conservation of total momentum and total angular momentum, for a system of particles
- total kinetic energy decomposes into COM kinetic energy and kinetic energy of individual particles about COM

# constraints
- **holonomic** constraints: $$f(\vec{r}_1,...,\vec{r}_n,t) = 0$$
- constraints introduce dependence between coordinates, decoupling of such facilitates the introduction of generalized coordinates.
- **holonomic** constraints are more tractable

# d'alembert's principle
- the **generalized coordinates** form a manifold (configuration space), the motion of the particle traces a curve on the surface parameterized by affine parameter $t$
- **virtual displacement**: the displacement is consistent with current displacements and forces applied, yet the virtual displacement does not result in modification of applied force or constraint (as an actual indinitesmal displacement would)
- **principle of virtual work**: virtual work as of applied forces vanishes
- principle of virtual work + $\vec{F}_i - \dot{\vec{p}}_i$ = **d'Alembert's principle**:
$$\sum_i [\vec{F}_i^{(a)} - \dot{\vec{p}}_i] \cdot \delta \vec{r}_i = 0$$
- transforming d'Alembert's principle into generalized coordinates gives Lagrange's equation.
- Lagrange's equation is not unique
# velocity-dependent potentials
- lorentz force in EM is derivable from a velocity-dependent potential
- when not all forces acting on the system are derivable from a potential, Lagrange's equation can be written in a more generalized form

$$\frac{d}{dt}(\frac{\partial L}{\partial \dot{q}_j}) - \frac{\partial L}{\partial q_j} = Q_j$$

for some generalized force $Q_j$ that can be put into

 $$Q_j = - \frac{\partial U}{q_j} + \frac{d}{dt}(\frac{\partial U}{\partial \dot{q}_j})$$
 
 Notice the velocity dependence.

- frictional force is derivable from Rayleigh's dissipation function, a 2nd order equation in velopcity

- The lagrangian is invariant under 
$$L \rightarrow L' = L + \frac{dF(q_1, ..., q_n, t)}{dt}$$
- the EM field is invariant under
$$\vec{A}\rightarrow \vec{A} + \nabla \psi, \quad \phi \rightarrow \phi - \frac{1}{c}\frac{\partial \psi}{\partial t}$$
