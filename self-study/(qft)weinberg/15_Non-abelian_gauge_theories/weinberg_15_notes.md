# non-abelian gauge theories
- qed uses U(1) as its gauge group, but the qft that have proved successful in describing the real world are all non-abelian gauge theories.
- it is natural that local gauge invariance should be extended to invariance under local non-abelian gauge transformations

# gauge invariance
- in generalizing qed to non-abelian gauge symmetry, we begin with a general, non-abelian gauge symmetry group with nontrivial generators
    $$\delta \psi_l (x) = i\epsilon^\alpha(x)(t_\alpha)_l^m \psi_m(x)$$
- by assuming that these transformations can be made infintesmal, this non-abelian group has to be a lie group and we derive the commutator relations (structure constants) $[t_\alpha, t_\beta]  = i C^\gamma_{\alpha \beta}t_\gamma$, and find its adjoint representation 
- from the need to make the lagrangian gauge invariant with derivative couplings, **we have to include a gauge field** $A_\mu$, with gauge terms $\partial_\mu \epsilon$ in order to cancel non-gauge-invariant terms in the lagrangian. This naturally introduces $D_\mu \psi$ , which transforms just like $\psi$ under gauge transformations. 
    The $\partial_\mu \epsilon$ terms in $A$ introduces $\partial_\nu \partial_\mu \epsilon$ terms in $\partial_\mu A_\mu$, which calls for an antisymmetric tensor $F = \partial_\mu A_\nu-\partial_\nu A_\mu$ as definition of the derivative of $A$. But this antisymmetric tensor has its own problem of having $\partial_\mu \epsilon-\partial_\nu \epsilon$ terms, which is resolved by finding its covariant version
    $$[D_\nu, D_\mu]\psi = -i(t_\gamma) F \psi, \quad F \cong \partial_\nu A - \partial_\mu A + C A\nu A\mu$$
    we find that $F$ must transform like a matter field that happens to belong to the adjoint representation of the gauge grp.
- we find that by choosing lorentz transformation $\Lambda$ to act on the state in hilbert space, we can make the gauge field $A^\alpha_{\mu \Lambda(x)}$ vanish at any one point. Furthermore, $\Lambda$ can be chosen such that one component of $A$ vanishes completely, so we'll do that.
- a field is **pure gauge** if it can vanish purely from a choice of gauge

# connections to gr
- **connection** on a fiber bundle is a device that defines a notion of parallel transport on the bundle; that is, a way to "connect" or identify fibers over nearby points. 
$$\textbf{gauge:} \quad \partial_\mu\psi \xrightarrow{A_\mu (x)} \text{cov. derivative of } \psi$$
$$\textbf{gr:} \quad ? \xrightarrow{\Gamma^\mu_{\nu \lambda}(x)} \text{cov. derivative of } T$$
- $F \sim R$ (Riemann-christofell curvature tensor)
# gauge theory lagrangians and simple lie groups
- just as in electrodynamics, for any massless particle of unit spin, the lagr must contain a free-particle term quadratic in $\partial_\mu A^\alpha_\nu - \partial_\nu A^\alpha_\mu$
> for the 4-momentum reason
-  it is not possible to introduce a kinematic term for the gauge field $A^\alpha_\mu(x)$ without also including self-interactions fo the field: 
    $$\mathscr{L}'_A = -\frac{1}{4}g_{\alpha \beta}F^\alpha_{\mu \nu} F^{\beta \mu \nu}$$
    this is another place where non-abelian gauge theories resemble general relativity, where the field self-interaction takes place via $\frac{-\sqrt{g}R}{8 \pi G}$ in the einstein-hilbert lagr density. This can be explained by observing the gauge field interacts with anything that transforms according to a nontrivial representation of the gauge group, including itself. 
- [$\rightarrow$] the term $-\frac{1}{4}F^2$ in qed does not entail interactions, it's purely a kinematic term for the photon. when the gauge group is nontrivial, however, it is a self-interaction. 
- we find that in order for things to work, the lie algebra has to be the direct sum of commuting compact simple and U(1) subalgebras.

# field equations and conservation laws
- we determine the full lagrangian in ordinary derivatives (15.3.1), solves its eqm (15.3.2), and find a conservation law $\partial_\nu \mathscr{J}^\nu_\alpha$ where $\mathscr{J}^\nu_\alpha = -\partial_\mu F^{\mu\nu}_\alpha =$ for the current with ordinary derivatives rather than gauge covariant derivatives. 
- the gauge invariance of the eqm is made manifest by replacing the ordinary derivatives in the eqm with gauge-covariant ones (15.3.5-8), this gives a gauge-covariant conservation law $D_\nu J^\nu_\alpha = 0$ with $\mathscr{J}^\nu_\alpha = -D_\mu F^{\mu\nu}_\alpha =$
- weinberg makes a connection to gr
# quantization
- in quantizing gauge-invariant theory, we encounter the same problem as we did in electrodynamics where it's not clear that we can satisfy all eqms at once. A similar approach to before (choosing the right gauge) is warranted, and for the moment we choose the **axial gauge**.
- after identifying the canonical variables, we write the path integral for th amplitude, and with some criterion checking (hamiltonian being quadratic in $p$, $A_{\alpha0}$ being independent variable of integration) we find that the exponent in the path integral is just the **action**. 
    $$<T\{O...\}> \propto \int_{\psi \text{ pth}} \int_{A \text{ pth}} (O...) e^{iI + \epsilon \text{ terms}}$$
# dewitt-faddeev-papov method
- the axial gauge picked earlier hides the inherent lorentz and rotational invariance of the amplitude, in order to make that manifest, a change of gauge is warranted.
- something important stated in chapter 9: field-independent factors in the functional path integral affect only the vacuum fluctuation part of expectation values and S-matrix elements, and so are irrelevant to the calculation of the connected parts f the S-matrix. 
- recognize that the functional integral in gauge qft is a special cause of a more general functional integral (15.5.1):
    $$\mathscr{J} = \int[\prod_{n,x}d\phi_n(x)]\mathscr{G}B[f[\phi]]\det \mathscr{F}[\phi]$$
    $f[\phi]$ a non-gauge-invariant gauge-fixing functional, $B$ some functional. 
- [$\rightarrow$] **theorem**: the integral (15.5.1) is actually independent of the gauge-fixing functional $f_\alpha[\phi;x]$ and depends on the choice of the functional $B[f]$ only through an irrelevant constant factor. and we get (15.2.21) as a powerful formula, whose effect on the lagr can be written as adding a term to the **effective lagrangian**
    $$\mathscr{L}_{\text{EFF}} = \mathscr{L} - \frac{1}{2\zeta}f_\alpha f_\alpha$$
- this is a powerful theorem that lets us derive feynman rules in a more convenient gauge. As our purpose is to make the amplitude manifestly lorentz invariant, the simplest choice is the lorenz gauge: $\partial_\mu A_\mu = 0$
- then the lorentz gauge is chosen to derive the feynman rules in this gauge invariant theory, which makes this theory manifestly lorentz invariant.

# ghosts
- the determinant term in equation (15.5.21) may have non-trivial interpretations, in this context of non-abelian gauge theory.
- recall from section 9.5 that the determinant of any matrix $\mathscr{F}_{\alpha x, \beta y}$ can be written as a path integral over fermionic fields (15.6.1-2). 
- the $\omega^*$ and $\omega$ in (15.6.2) are not necessarily complex conjugates of each other, because they are to be interpreted as separate path integrals.
- Thus the determinant of $\mathscr{F}$ term in (15.5.21) can be accounted for by path integrating over some effective action over $\omega, \omega^\star$ fields given by (15.6.2,4)
- the fields $\omega, \omega^\star$ are lorentz scalars so they are spin 0, but in order for the determinant $\rightarrow$ integral procedure to work they have to be grassman numbers (obeying fermi statics, or equivalently, anticommute), so it would appear that spin and statics is broken.
    yet we are fine because no particles described by these fields can appear in initial or final states. Thus $\omega, \omega^\star$ are called the **ghost** and **antighost** particles.
- the ghost action is
    $I_{GH} = \int d^4x d^4y \omega^\star \omega \mathscr{F}$, $\mathscr{F}$ is the matrix whose determinant we wish to evaluate.
    the modified action is
    $I_{MOD} = \int d^4x [\mathscr{L} - \frac{1}{2\zeta}f_\alpha f_\alpha] + I_{GH} = I_{EFF} + I_{GH}$
- Further inspection of (15.6.2) shows that the action respects the conservation of 'ghost number', equal to +1 for ghost, and -1 for antighost. 
- to see what ghost vertices look like in feynman diagrams, we pick the simplest $\mathscr{F}$ (15.6.5), derive its interaction lagrangian density along with propagator term (15.6.5-13. we find that in this simplest theory the ghost vertex looks like a vector bosonic line with a ghost line and an antighost line. 

# brst
- when we made the amplitude lorentz invariant with dewitt-faddeev-papov method we had to pick a specific gauge, this would hide the gauge-invariance of the theory.
- this is a serious problem in proving renormalizability, as gauge invariance places restrictions on the counterterms available. so it's up to us to determine what kind of freedom we have in picking counterterms for canceling what kinds of infinities.
- we take the $I_{MOD} = I_{EFF} + I_{GHOST}$ and fourier transform the gauge fixing condition $B[f]$ in $\mathscr{L}_{MOD}$ and to find ourselves having to integrate over some new fields $h_\alpha$ (Nakanishi-Lautrup fields), weinberg creatively picks the name $I_{NEW}$ for the new action:
    $$I_{NEW} = \int d^4x(\mathscr{L} + \omega_\alpha^* \Delta_\alpha + h_\alpha f_\alpha + \frac{1}{2} \zeta h_\alpha h_\alpha)$$
    $\omega$ is ghost field, $h$ is the nakanishi-lautrup field
- this action is not gauge invariant, yet it is invariant under brst:
    $$\delta_\theta \psi = i t_\alpha \theta \omega_\alpha \psi, \quad
    \delta_\theta A_{\alpha \mu} = \theta D_\mu \omega_\alpha, \quad
    \delta_\theta \omega_\alpha^* = - \theta h_\alpha,$$
    $$\delta_\theta \omega_\alpha = - \frac{1}{2}\theta C_{\alpha \beta \gamma} \omega_\beta \omega_\gamma, \quad
    \delta_\theta h_\alpha = 0$$
- **nilpotentcy** in general is $A^N = 0$ (useless power), here means if $\delta_\theta F \cong \theta s F$, then $\delta_\theta(sF) = 0$
- weinberg shows in terms of nilpotency, 
    $$I_{NEW} = \int d^4x \mathscr{L} + s\psi$$
    and subsequently the brst symmetry of $I$. 
    Notice that this equation indicates that the physical content of any gauge theory is in the kernel of the brst operator. The kernel modulo the image of any nilpotent transformation is said to form the **cohomology** of the transformation.
- btst symmetry will be useful in proving renormalizability as we will use the brst-invariance of the divergent terms in feynman diagrams
- brst transformation is not real
    $$<\alpha|Q = Q|\beta> = 0$$
    physical states differ by $Q\ket{\beta}$ are indistinguishable physically, thus independent physical states correspond to states in the kernel of $Q$, modulo the image of $Q$, in other words, they correspond to the cohomology of $Q$. 
- [cohomology = reversing arrows](https://www.youtube.com/watch?v=ZTgnSPYRCDk)



