qed

- infer the need for a principle of gauge invariance from the difficulty of formulating quantum theory of massless particles with spin
- deduce the features of electrodynamics from gauge invariance
- take gauge invariance as a starting point and deduce the existence of a vector potential for massless particles of unit spin

# gauge invariance

- there is no way to construct a 4-vector as a linear combination of the creation and annihilation operators for helicity $\pm 1$
- Instead of banishing $A_\mu$ from the action, we shall require that the part of the action $I_M$ for matter and its interaction with radiation be invariant under a gauge transformation 
    $A_\mu \rightarrow A_\mu +\partial_\mu \epsilon$
- we'd find that the lorentz invariance of $I_M$ requires $\partial_\mu \frac{\delta I_M}{\delta A_\mu (x)} = 0$ which implies $\frac{\delta I_M}{\delta A_\mu (x)}$ is a conserved current
- How to construct such current? We know that infinitesmal internal symmetries of the action implies conserved currents, in fact consider the transformation
    $$\delta \psi^l(x) = i \epsilon(x) q_l \psi^l (x)$$
    that leaves the matter action invariant for a constant $\epsilon$, when the matter field satisfies the field equations this transformation defines a conserved current $J^\mu$. 
- we can construct a lorentz-invariant theory by coupling the vector field $A_\mu$ to the conserved $J^\mu$ in the sense that $\delta I_M/\delta A_\mu(x)$ is taken to be proportional to $J^\mu$ from above:
    $$\frac{\delta I_M}{\delta A_\mu(x)} = J^\mu (x)$$
- the requirement above can be restated as a principle of invariance: the matter action is invariant under the adjoint transformations:
    $$\delta A_\mu(x) = \partial_\mu \epsilon(x), \quad
    \delta \psi_l(x) = o \epsilon(x) q_l \psi_l(x)$$

    - If $\epsilon$ is a constant, this is a global symmetry, or gauge invariance of the first kind
    - If $\epsilon(x)$ is arbitrary, then this is a local symmetry, or gauge invariance of the second kind

- Taking the radiation action to be that of (8.1.14), and imposing the equation of motion yields $0 = \frac{\delta}{\delta A_\nu} [I_\gamma + I_{M}] = \partial_\mu F^{\mu \nu} + J^\nu$, which is the inhomogeneous maxwell equations. 

# constraints and gauge conditions
- there are constraints that arise when we try to quantize the theory whose lagrangian we just studied above
- the first constraint arises from the fact that the lagrangian density is independent of the time-derivative of $A_0$, meaning $\Pi_0 = 0$. this is a primary constraint. this primary constraint leads immediately to the secondary constraint of 
    $$\partial_i \Pi^i = - J^0$$
- because of the partial arbitrariness of $A_\mu$ due to gauge invariance, it is not possible to apply the canonical quantization procedure directly, rather, we need to first choose a gauge.

# choosing coulomb gauge

choosing the coulomb gauge, and then applying dirac's method of removing second class constraints, we done.