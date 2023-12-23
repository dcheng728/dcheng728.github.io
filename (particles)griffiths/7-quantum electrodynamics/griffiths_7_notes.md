- [ ] renormalization
# the dirac equation
- in nonrelativistic qm, particles are described by the schrodinger equation, in relativistic qm, particles of spin 0 are described by the KG equation, particles of spin 1/2 are described by the dirac equation, and particles of spin 1 are described by the proca equation.
- the derivation of dirac's equation involves first 'factor' the enerty momentum relation:
    $$(p^0)^2 - m^2c^2=(p^0+mc)(p^0-mc)=0$$
- the next brillance of dirac was the idea of making the $\gamma$s matrices instead of just a number, then we find the anticommutator relation (7.15), and some further derivation yields the **dirac equation** (7.20).
- Although the solution to Dirac equation has 4 components, it's not a 4-vector, rather it transforms like 2 spinors.

# solutions to the dirac equation
- one solves the dirac equation in the rest frame ($\vec{p} = 0$) and finds 4 independent solutions (7.30).these shall be interpreted as a spin up, spin down electron, and a spin up, spin down antielectron. **this is not a 4 vector**!
- A quick examination of the solutions in (7.30) lets one find that these solutions only propagate in time, but not in space. 
    The natural next step would be to extend the result at $\vec{p} = 0$ to general 4-momentum of a massive particle. Such planewaves furnish a representation of the corresponding little group.
- The above pursuit would yield the momentum space dirac equation, which then leads to the solution in (7.43), which after conventional normalization is written as (7.46)
- you might guess that $u^{(1)}$ describes an electron with spin up, and $u^{(2)}$ with spin down. but no. if we orient the $z$ axis so that it points along the direction of motion ($\vec{p}_x=\vec{p}_y = 0$), then $u^{(1)},u^{(2)},u^{(3)},u^{(4)}$ would correspond to the eigenstate of $S_z$ for electron spin up, electron spin down, antielectron spin up, antielectron spin down, respectively. 

# bilinear covariants
- griffiths makes an argument that \textbf{the dirac spinor aint 4-vector} (7.52-57)
- showed a way to construct scalar with dirac spinor (7.58-60), and asked is this a scalar or pseudoscalar?
    \footnote{the difference between scalar and pseudoscalar is how they transform under parity} It is a scalar (7.61-62). But is there another way to construct pseudoscalar out of dirac spinors? Yes, using $\gamma_5 = i \gamma^0\gamma^1\gamma^2\gamma^3$ (7.63-7.67)
- besides scalars and pseudoscalars, we can also construct vectors, pseudovectors, and antisymmetric tensor with dirac spinors (7.68-69)

# the photon
- states the field forms of the maxwell equations (7.70), finds the index notation form of the inhomogeneous maxwell equations (7.70-74)
- for the homogeneous maxwell equations, introduce a vector potential $\vec{A}$, which gives us an index notation form of the homogeneous equations in terms of the potential (7.75-7.79), and notice that we can also write the inhomogeneous maxwell equations with the potential rather than field (7.80)
-[❤️] we have two ways to write maxwell's equations, in EM fields, or in a single potential $A$. \href{https://en.wikipedia.org/wiki/Maxwell%27s_equations#Alternative_formulations}{wikipedia}
- in classical electrodynamics, the fields are the physical entities while the potentials are mathematical constructs that automatically satisfy the homogeneous equations. the subtlety in the potential formulations is that is only unique up to a gauge. There is no way to eliminate the gauge ambiguity, so we can either 
	- live with the indeterminacy, meaning carrying along spurious degrees of freedom
	- impose an additional constraint, which spoils the manifest lorentz covariance of the theory
- griffiths choose the coulomb gauge $\nabla \cdot \vec{A} = 0$.
- in qed, the potential $A^\mu$ becomes the wave function of the photon, and we have a eqm for this photon: $\Box A^\mu = 0 $. solving this equation yields $A^\mu(x) = a e^{-(i/\hbar)p\cdot x}\epsilon^\mu(p)$, which can be interpreted as a wave propagation (exponential part) of some initial condition $\epsilon^\mu(p)$ at $x = 0$, this $\epsilon^\mu(p)$ is called the **polarization vector**.
- some further derivation indicates the polarization vector is orthogonal to the direction of the momentum vector, so we say a free photon is **transversely polarized**, for this reason the coulomb gauge is also called **transverse gauge**. 

# casimir's trick and the trace theorems

the feynman rules stated for qed works with spin, but we often dont care about the spins in actual experiments. In those cases the relevant cross section is an **average** over all initial spin configurations, and **sum** over all final spin configurations. 
