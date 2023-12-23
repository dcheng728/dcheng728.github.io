- the free electron model have the valence electrons in metals move freely through the volume of the metal
- free electron model most useful when we focus on kinematic properties of conduction electrons
- [ ] 3s conduction band
- electrons in metals can have mean free path of $10^8$ interatomic spacing. This observation is incompatible with treating particles as solid balls, so wave-theory (QM) is needed. Further, infrequency of electron-electron scattering may be interpreted by pauli xclu principle in free electron fermi gas model.
# energy levels in 1D
- **orbital** denotes solutions to the wave equation for a system of only 1 electron. The orbital formalism is relevant for when we treat N particle wave func as N x 1 particle wave func
- uses ISW model
- pauli xclu pcpl allows only one e- per orbital
- pauli xclu pcpl demand ISW orbitals are filled from bottom up in pairs
- fermi energy is the energy of topmost filled level, for N e- in GND state: 
$$\epsilon_F \frac{\hbar^2}{2m}(\frac{N \pi}{2L})^2$$
# effect of T on the fermi-dirac dist
- fermi-dirac dist gives the probability that an orbital at energy $\epsilon$ will be occupied in an ideal electorn gas in thermal equilibrium: 
$$f(\epsilon)= \frac{1}{\exp{[(\epsilon-\mu(T))/k_B T]} + 1}$$
- By imposing $f(\epsilon)$ be binary at $T = 0$, we find $\mu(T=0) = \epsilon_F$
- The $\epsilon - \mu >> k_B T$ is the classical limit (giving Boltzmann Maxwell dist)
# free electron gas in 3D
- 3D generalization of 1D is straightforward (see Kittel/Griffiths/Glazer&Wark/etc.)
- By transitioning to $k$ space, we obtain the density of state and find fermi energy $k_F = (\frac{3\pi^2N}{V})^{1/3}$, $\epsilon_F = \frac{\hbar^2}{2m}(\frac{3\pi^2 N }{V})^{2/3}$
- Density of state: 
$$D(\epsilon) = \frac{dN}{d\epsilon} = \frac{V}{2\pi^2}( \frac{2m}{\hbar^2} )^{3/2}\epsilon^{1/2}$$
# heat capacity of the electron gas
- classical mechanics predicts $\frac{3}{2}k_B$, yet the actual heat capacity is 0.01 of this value
- this is due to electrons below fermi energy being 'locked'
- only a fraction $T/T_F$ can be excited at $T$, giving energy O(kT)
- At room temp, fermi temperature is approximately $5\times10^4$ K
# experimental heat capacity of metals
- debye + free electron gas gives
$$C = \gamma T + AT^3$$ this $\gamma$ is given the name of **sommerfeld parameter**
- thermal effective mass measures discrepancy between observed and actual values of $\gamma$. This discrepancy is due to other interactions besides pauli exclu, lattice inperfection, phonon scattering, etc.
# electrical conductivity & Ohm
- use mv = $\hbar k$, a classical interperetation of electorn quantum momentum + lorentz force law
- in the absence of collisions, the fermi sphere accelerates, But the collisions and lattice imperfections introduce a 'frag'
- The collisions are measured with $\tau$, 'collision time'