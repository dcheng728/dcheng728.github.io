# Scattering theory

## IN and OUT states
### formalism on actual physical states
- states that are energy eigenstates can not be localized in time, we must consider wave packets, superpositions of states.
- we assume that the state evolved like a free one long before the interaction took place
- we use $\Psi$ tp denote the actual physical state with interaction
- by convention, we let $\alpha$ denote momentum, spin and such, then we convene
    $$\braket{\Psi_\alpha}{\Psi_{\alpha'}}=\delta(\alpha,\alpha')$$
    since $\alpha$ can contain discrete labels, we define
    $$\int d \alpha = \sum_{\text{discrete labels}} \int d \text{(continuous labels)}$$
    the completeness relation reads
    $$\Psi = \int d\alpha \braket{\Psi}{\Psi_\alpha}\Psi_\alpha$$
    the eigenvalue when acted on by the full hamiltonian is
    $$H \Psi_\alpha = E_\alpha \Psi_\alpha$$
- Weinberg uses $\Psi^+$ for in states and $\Psi^-$ for out states, they describe the states at time $t=-\infty$ and $t=\infty$ respectively
- energy eigenstates can not be localized in time, because the time evolution operator would yield an inconsequential phase factor
- we need to consider wave packet states, superpositions of states that are given by some amplitude
    $$\Psi p \int d\alpha g(\alpha) \Psi_\alpha$$

### relation to free states to Lipp-Schwinger
- We decompose $H = H_0 + V$, and let $\Phi$ be the solution to $H_0$
- we convene
    $$H_0 \Phi_\alpha = E_\alpha \Phi_\alpha$$
    $$\braket{\Phi_\alpha}{\Phi_{\alpha'}}=\delta(\alpha,\alpha')$$
- notice that we convened the same spectrum of $H$ on $\Psi$ as $H_0$ on $\Phi$, this requires that the masses appearing in $H_0$ be the physical masses that are actually measured, which are not necessarily the bare mass in $H$, 
    if there is any difference it must be accounted for in $V$
- we then find
    $$\Psi_\alpha^{\pm} = \Omega(\mp \infty) \Phi_\alpha,$$ 
    where
    $$\Omega(\tau) = \exp{iH\tau} \exp{-iH_0 \tau}$$
    and additionally 
    $$\braket{\Psi_\alpha^\pm}{\Psi_{\beta}^\pm} = \delta(\alpha - \beta)$$
- further derivations leads to the Lippmann-Schwinger formula
    $$\Psi_\alpha^{\pm} = \Phi_\alpha + \int d\beta \frac{T_{\beta \alpha}^{\pm} \Phi_\beta}{E_\alpha - E_\beta \pm i\epsilon},
    \text{\quad \quad}
    T_{\beta \alpha}^{\pm} \equiv \braket{\Phi_\beta}{V \Psi_\alpha^{\pm}}$$
    
- as a convenient representation for the factor of $\frac{1}{E_\alpha - E_\beta \pm i \epsilon}$, we have
    $$\frac{1}{E \pm i \epsilon} = \frac{\mathscr{P}}{E} \mp i \pi \delta(E)$$
    where $\mathscr{P} = \frac{E}{E^2 + \epsilon^2}$
## S-matrix
- we define the S matrix by
    $$S_{\beta \alpha} = \braket{\Psi_\beta^-}{\Phi_\alpha^+}$$
- If there were no interaction then the in and out states would be the same, meaning
    $$S_{\beta \alpha} = \delta(\alpha-\beta),$$
    thus the rate of reaction $\Psi_\alpha \rightarrow \Psi_\beta$ is $|S_{\beta \alpha} - \delta(\alpha - \beta)|^2$ \footnote{the in and out states are not differentiated, they are only labeled differently here, and they only differ in how they are created or their asymptotic time evolution, in other words 
    $$\braket{\Psi_\beta^-}{\Phi_\alpha^+} = \braket{\Psi_\beta}{\Phi_\alpha}$$
    
- S matrix connects two complete sets of orthonormal states, it must be unitary
    $$\int d\beta S_{\beta \gamma}^* S_{\beta \alpha} = \braket{\Psi_\gamma}{\Psi_\alpha} = \delta(\gamma - \alpha),
    \quad 
    S^\dag S = 1$$
    
- If we define the operator analog of the S matrix as
    $$\braket{\Phi_\beta}{S \Phi_\alpha} = S_{\beta \alpha}$$
    we will find
    $$S = \Omega(\infty)^\dag \Omega(-\infty) = U(\infty, -\infty)$$
    $$U(\tau, \tau_0) = \exp{iH_0 \tau }\exp{-iH(\tau - \tau_0)}\exp{-iH_0 \tau }$$
### Lipp-Schwin analog of S
- We now try to derive a similar formula for $S^\alpha_\beta$ using the Lippmann-Schwinger formula
- the method is to instead of taking the $t \rightarrow -\infty$ limit for $\Psi^+$, we take the $+\infty$ limit,
    this means we have to close the contour of integration for $E_\alpha$ in the lower half plane now, 
    and now we do pick up a contribution from the singular factor $(E_\alpha - E_\beta +i\epsilon)$, 
    by the method of the residues and taking $t\rightarrow \infty$, we obtain
$$\mathscr{I}_\beta^+  \equiv \int d\alpha \frac{e^{-i E_\alpha t} g(\alpha) T_{\beta \alpha}^{\pm}}{E_\alpha - E_\beta \pm i\epsilon}
      \quad \rightarrow -2i\pi e^{-iE_\beta t} \int d\alpha \delta(E_\alpha - E_\beta)g(\alpha) T_{\beta \alpha}^+$$
- we then find
    $$S_{\beta \alpha} \propto \delta(\beta - \alpha) - 2i\pi \delta(E_\alpha - E_\beta) \braket{\Phi_\beta}{V \Phi_\alpha}$$
    which is known as the Born approximation, an approximation for the S-matrix at weak interactions. 

## Symmetries of the S-matrix
### Lorentz-invariance
- We state the Lorentz-invariance condition as
    $$S_{\alpha \beta} = \braket{\Psi_\alpha}{\Psi_\beta}= \braket{U(\Lambda, a)\Psi_\alpha}{ U(\Lambda, a) \Psi_\beta}$$
- We do not get Lorentz-invariance of the $S$-matrix for free, that is, it is only for certain special choices of interaction Hamiltonian that will give the theory's S-matrix lorentz invariance, as defined above 
- As another caveat, how do we know $U(\Lambda)$ acts the same on the in and out state? We dont, but we can apply the transformation rules in Hilbert space and we will find that the inner product will be invariant if the theory satisfies
    $$ [S, U(\Lambda)_0] = 0$$,
    which when expressed in terms of the infinitesmal lorentz transformation, is
    $$[H_0,S]=[\PP,S]=[\JJ_0, S]=[\KK_0,S]=0$$
- Weinberg also goes to show that an alternative formulation of the condition also makes Smat lorentz invariant
    $$[V,\PP_0] = [V, \JJ_0]=0$$
### Internal Symmetries
- We apply the same procedure as above but to internal symmetries, we find that the condition now becomes
    $$[U_0(T), H_0] = [U_0(T), V] = 0$$
- a classic example of conservation law from internal symmetry is electric charge
- More examples include baryon \#(protons, neutrons, hyperons), lepton \#(electrons, muons, $\tau$ particles, neutrinos), but these examples are believed to be only very good approximations.
- other examples of this type that are definitely approximation: conservation of strangeness
- isotopic spin invariance is only believed to be a good approximation, because such invariance is not respected by interactions such as EM\footnote{different members of the isospin multiplet have different electric charges and slightly different masses}
### parity
- parity $P$ is not conserved in the following sense: $$
    \begin{cases}
        [P, H_0] \approx 0 & \text{not conserved in weak interaction between left and right handed ferions} \\
        [P, V] \approx 0 & \text{conserved in EM but not weak interaction}
    \end{cases}$$the weak interaction is responsible for $\beta$-decay
- The naive definition of the parity operator is $$U(P) \Psi_{p, \sigma} = \eta \Psi_{P p, \sigma} $$where $\eta$ is the **intrinsic parity** (a phase factor that arises as an eigenvalue of the parity operation) of the state. In a subtle way, this gives us the freedom to redefine $P$ if $P$ were to be conservedm
	- Parity being conserved means $$[P, H_0] = [P, V] = 0$$
        If we have a conserved internal symmetry $T$ means
        $$[U_0(T), H_0] = [U_0(T), V] = 0$$
        thus
        $$[P U_0(T), H_0] = [P U_0(T), V] = 0$$$$P' = PU_0(T) \text{ for internal symmetry } T $$
- Must the intrinsic parity always take on $\pm 1$, ignoring normalization?
	- Yes, Suppose it doesn't, then we have         $$P^2 \Psi = e^{i\theta} \Psi $$
       \ul{ if the theory we are considering has a continuous internal symmetry}, then we can redefine $\parity \rightarrow \parity I$ for some internal symmetry $I$ that cancels the $e^{i\theta}$ exactly, and this new $\parity'$ will give intrinsic parity of $\pm 1$, we then redefine it to be the parity operator $\Box$
       - No, if we don't have continuous internal symmetry.
- $P^2 \Psi = \eta \Psi$ means $P^2$ acts like an internal symmetry
### time-reversal
- we expect that time-reversal swaps the in and out states
- As usual, applying the transformation rules of symmetry transformation to states in hilbert space we find the requirement for a thoery to be time-reversal invariant
    $$[T_0, H_0] = [T_0,V] = 0 $$
    we will then find
    $$T \Omega(-\infty) \Psi_{\alpha} = \Omega(\infty) \Psi_{T \alpha } $$
    which makes sens
- time reverasl symmetry is much more difficult to experimentally verify than parity, because experimentally, it is extremely difficult to set up
    $\text{Ni}^{60} + e^- + \bar{nu} \rightarrow \text{Co}^{60}$
### PT
- PT would have to be anti-unitary, because P is unitary and T is anti-unitary
    $$S_{\beta \alpha} \rightarrow -e^{2i(\delta_\alpha + \delta_\beta)} S^*_{\parity \timeR \beta \parity \timeR \alpha}$$
    $\parity \timeR$ would preserve the momenta while swapping spin, so invariance of S-matrix under $\parity \timeR$ implies there wouldnt be any preference for the electron in the decay $\text{Co}^{60} \rightarrow \text{Ni}^{60} + e^- + \bar{nu}$ to be emitted in the same or opposite direction to the $\text{Co}^{60}$ spin
- the 1957 experiment did not rule out time-reversal symmetry immediately, but ruled out PT by demonstrating the above statement is false    
### C
It is understood today that C is not conserved in the weak interaction, just like how P is not conserved

### CP
It is thought to be true that CP is ''more conserver" than C and P in weak force, but nevertheless CP is still not a conserved quantity

### CPT
There is good reason to believe that CPT is conserved exactly, which would be really nice as it 
1. gives a good interpretation of antiparticles
2. the fact that CPT commutes with the Hamiltonian tells us that the particle and antiparticle have the same mass

## Rates and Cross-section
Weinberg: this section is more like a mnemonic, because it seems like no interesting open problems in physics hinge on getting the fine points right regarding these matters

## Implications of Unitarity
### Optical theorem
- By the requirement that the S-matrix being unitary, we can actually find that the imaginary part of $M_{\alpha \alpha}$ (Recall that the $M$ matrix is part of the S-matrix after we removed the part where nothing happens) is actually somewhat interesting. $$\Im M_{\alpha \alpha } = - \pi \int d\beta  \delta^{4}(p_\beta  - p_\alpha ) |M_{\beta \alpha }|^2 $$
- This is the **optical theorem**
- If we take the optical theorem to the high energy limit, we will find that unstable particles and their corresponding antiparticles have precisely the same lifetimes. 
### Boltzmannn H-theorem
- The optical theorem is obtained using $S^\dagger S =1$, using the other condition of $SS^\dagger = 1$, we find
    $$\Im M_{\alpha \alpha } = - \pi \int d\beta  \delta^{4}(p_\beta  - p_\alpha ) |\boxed{M_{\alpha \beta }}|^2 $$which implies $$\int d\beta  \delta^{4}(p_\beta  - p_\alpha ) |\boxed{M_{\alpha \beta }}|^2 = \int d\beta  \delta^{4}(p_\beta  - p_\alpha ) |\boxed{M_{\beta \alpha }}|^2$$
- further derivation shows  $$-\frac{d}{dt} \int d\alpha P_\alpha \ln{P_\alpha/c_\alpha} \ge 0 $$which called the Boltzmann H-theorem, equivalent to entropy never decreases.