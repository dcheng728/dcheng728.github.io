## quantum mechanics
-  physical states are represented by rays (normalized vectors that differ only by a phase) in HIlbert space, a hilbert space is an infinite dimensional complex vector space with inner/scalar product defined
- observables are represented by **hermitian** operators.
- Important concepts of Hilbert space operators/vectors include **unitary**, **linearity**, **antiunitary**, **antilinearity**, and **adjoint**
- For all Hilbert space vectors: 

$$(\phi,\psi) = (\psi,\phi)^*, \quad (\phi,a\psi_1+b\psi_2) = a(\phi,\psi_1) + b(\phi,\psi_2)$$
$$(a\phi_1+b\phi_2,\psi) = a^*(\phi_1,\psi) + b^*(\phi_2,\psi)$$
- Wigner proved that for any symmetry transformation, there is a corresponding operator $U$ in Hilbert space that is either unitary and linear or **antiunitary** and **antilinear**
- differential probability $\Leftrightarrow$ amplitude squared
## symmetries
- a **symmetry transformation** is a change in POV that does not change the result of possible experiments
- wigner proved that symmetry transformations must be reflected in hilbert space by **unitary and linear**, or **antiunitary and antilinear** operators
    Unitary and Linear means $$(U\psi,U\phi) = (\psi,\phi) \quad
    U(a\psi_1 + b\psi_2) = aU\psi_1 + bU\psi_2$$antiunitary and antilinear means $$\braket{U\psi}{U\phi} = \braket{\psi}{\phi}^* \quad
    U(a\psi_1 + b\psi_2) = a^*U\psi_1 + b^*U\psi_2$$
    the adjoint for unitary is defined as $$(\phi,A\psi) = (A^\dagger \phi,\psi)$$while the adjoint for antiunitary operator is defined as $$(\phi,A\psi) = (A^\dagger \phi,\psi)^*$$
- symmetry transformations that can be made continuously into the identity must be **unitary and linear**, because the identity is unitary and linear.
- observables and infinitesmal transformations: the generators of infinitesmal symmetry transformations must be **hermitian** (adjoint equals itself) and **linear** for such transformation to be unitary, which makes them candidates for observables. Indeed, most perhaps all of the physical observables, such as **angular momentum**, **momentum**, **energy** arise from symmetry transformation.
- the transformations in hilbert space that corresponds to a given symmetry transformation is said to furnish a **representation** of the symmetry transformation group $$\textbf{Rep}(\Lambda_1)\textbf{Rep}(\Lambda_2)= N(\Lambda_1, \Lambda_2)\textbf{Rep}(\Lambda_1 \Lambda_2) \simeq \textbf{Rep}(\Lambda_1 \Lambda_2)$$in other words, representations of symmetry transformations tell us how the states transform in response to this symmetry transformation in the hilbert space.
- [❤️] we are looking for Poincare-invariant theories thus we are interested in **unitary representations of the Poincare group**. 
## quantum lorentz trans
- the **Poincare group** is also known as the **inhomogeneous lorentz group**, while the group of **boosts and rotations** are known as the **homogeneous poincare group**, or the **lorentz group**.
- the subgroup of lorentz transformations with determinant 1 and $\Lambda^0_0\ge 1$ is known as the **proper orthochronous lorentz group**
    >The proper orthochronous Lorentz group SO(1,3) consists of all Lorentz transformations that preserve the orientation and direction of time and are connected to the identity transformation.
- any lorentz transformation can be constructed with the proper orthocho. lorentz group together with a discrete transformation. 
 > any lorentz transformation is either proper and orthochronous, or may be written as the product of an element of the proper orthochronous lorentz group with a discrete transformation parity or time-reversal
- [❤️] the study of the whole lorentz group reduces to the study of its **proper orthochronous subgroup** $+$ **parity and time-reversal**
## the poincare algebra
- much of the information about any Lie symmetry group is contained in properties near the identity, ie infinitesmal transformations
- the condition that $\Lambda g \Lambda = g$ requires that the infinitesmal transformation $\omega_{\mu \nu}$ obeys   $$\omega_{\mu \nu} = -\omega_{\nu \mu}$$
- [❤️] we find the **Lie algebra** for the Poincare grp
$$
    i[J^{\mu\nu}, J^{\rho \sigma}] = \eta^{\nu \rho} J^{\mu \sigma} - \eta^{\mu \rho}J^{\nu \sigma} - \eta^{\sigma \mu} J^{\rho \nu} + \eta^{\sigma \nu} J ^{\rho \mu} \\
    i[P^\mu, J^{\rho \sigma}] = \eta^{\mu \rho} P^{\sigma} - \eta^{\mu \sigma} P^{\rho}\\
    [P^\mu, P^\rho] = 0
$$
    or equivalently with $P=\{P^1,P^2,P^3\}$, $J=\{J^{23},J^{31},J^{12}\}$, $K=\{J^{01},J^{02},J^{03}\}$, 
    we have 
$$
	[J_i, J_j] = i \epsilon_{ijk} J_k, \quad
	[J_i, K_j] = i \epsilon_{ijk} K_k, \quad
	[K_i, K_j] = -i \epsilon_{ijk} J_k, \quad
	[J_i, P_j] = i \epsilon_{ijk} P_k$$$$ [K_i, P_j] = - i H \delta_{ij}, \quad
	[K_i, H] = -i P_i, \quad
	[J_i, H] = [P_i, H] = 0 
$$
## 1particle states
In this section, we consider the representation of the lorentz group, and classify the states by their little group, and we find that such classification corresponds to that of massive and massless particles. 
- We begin with a general statement of how representation of a lorentz transformation should act on a state (2.5.3)
- no matter how we lorentz transform, we can never transform a time-like particle into a massive particle, so we can classify the particle  by their momentum into 'cliques', where momenta from two different cliques are never related by a lorentz transformation. 
- we pick a standard momentum in each 'clique', we define a standard transformation that takes the standard momentum to any other momentum within the clique
- The standard momentum and standard transformation above allows us to factor a general operator induced by a lorentz transformation into an operator induced by the standard transformation and some other operator reduced by a transformation that fixes the momentum, we call this 'other transformation' the 'little group' 
- On Lil grp: $p^\mu = L^{\mu}_{\nu} p^\nu(p) k^{\mu}$ with $k^\nu$ being the standard momentum, along with $\psi_{p,\sigma} \equiv N(p) U(L(p))\psi_{k \sigma}$ gives
    $U(\Lambda) \psi_{p,\sigma} = N(p) U(L^{-1}\Lambda L(p)) \psi_{k\sigma}$
    Observe that $L^{-1}\Lambda L(p)$ belongs to the subgrp of the homogeneous lorentz group that fixes $k$, this is a more rigorous definition of the Wigner's little group. 
- Some simple further derivation leads quickly to (2.5.11), which turns the problem of finding the representation of lorentz group into finding representation of the little group. At a more fundamental level, what (2.5.11) says is that the representation of a general $\Lambda$ can be written as scaling by some number $\frac{N(p)}{N(\Lambda p)}$ together with a representation of the little group $D(W, p)$. 
- we fix the normalization factor in (2.5.11), shown in (2.5.18) 
- [❤️] the little group is **SO(3)** and **ISO(2)** for massive and massless particles}
## parity and time reversal
- Parity and time-reversal are only conserved without the context of weak-nuclear force, the inclusion of which puts them at approximately conserved
### Properties of P and T on the Poincare generators}
        $$P \JJ P^{-1} = \JJ \quad
        P \KK P^{-1} = -\KK \quad
        P \PP P^{-1} = -\PP $$
$$T \JJ T^{-1} = -\JJ \quad
        T \KK T^{-1} = \KK \quad
        T \PP T^{-1} = -\PP$$
#### massive 1particle states
- $P \Psi_{\vec{p}, \sigma} = \eta \Psi_{P\vec{p}, \sigma}$
- $T \Psi_{\vec{p}, \sigma} = \xi(-)^{j-\sigma} \Psi_{P\vec{p}, -\sigma}$    
#### massless 1particle states}
- $P \Psi_{\vec{p}, \sigma} = \eta_{\sigma} \exp{\mp i \pi \sigma} \Psi_{P\vec{p}, -\sigma}$ this happens because parity inverts momentum but not the direction of angular momentum, thus the helicity is inverted, the state also gains a phase factor dependent on the helicity. the sign in $\mp$ is dependent on whether the two-component of $\vec{p}$ is positive or negative. 
- this also tells us that the existence of a symmetry under parity requires that any species of massless particle with non-zero helicity be accompanied with another of opposite helicity.
- We know that $T$ changes both the direction of angular momentum and momentum, so its logical that it doesnt change helicity, indeed it doesnt.
        $$T \Psi_{\vec{p}, \sigma} = \xi_{\sigma} \exp{\pm i \pi \sigma} \Psi_{P\vec{p}, \sigma}$$
    again the $\pm$ depends on whether the two component of $\vec{p}$ is positive or negative