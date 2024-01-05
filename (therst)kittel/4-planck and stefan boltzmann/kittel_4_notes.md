- "mode" = specific vibration angular frequency modulo addition of $2n\pi$, in other words, a specific $\omega$ constitutes a "mode"
- "black" in a frequency = all radiations in such frequency range are absorbed

# planck ditribution and stefan-boltzaman law
assuming lattice vibrational excitations: $\epsilon = s\hbar \omega$. Consider only mode $\omega$. 

$$Z_\omega = \sum_s \exp(-s\hbar \omega / \tau) = \frac{1}{1- e^{-\hbar \omega/ \tau}}$$

$$<s>_\omega = \frac{<\epsilon>_\omega}{\hbar \omega} = \sum_s (s) \exp(-s\hbar \omega / \tau) =  \frac{1}{e^{\hbar \omega / \tau} - 1}$$

> for bosons, particle # need not be conserved, and $<s>_\omega$ can be interpreted as the thermal equilibrium expec number of $\omega$-energy photons/phonons in the system. *This formalism is completely general to all bosons*

In the realm of therst, $<\epsilon>_\omega$ **"IS"** $\epsilon_\omega$. So lifting our discussion to all $\omega$:

$$U = \sum_\omega D(\omega) \epsilon_\omega$$

Now transition to phase space with a standard treatment of degeneracy gives 

- the **stefan-boltzmann** law for spatial energy density

$$\frac{U}{V} = \frac{\pi^2}{15 \hbar^3 c^3} \tau^4$$

- the **the planck radiation law** for spectral density

$$u_\omega = \frac{\hbar}{\pi^2 c^3} \frac{\omega^3}{ e^{\hbar \omega / \tau} - 1}$$

> Kittel claims this is where all quantum theory began

# debye phonons
- the distribution function for phonon/photon is the same:

$$<s(\omega)> = \frac{1}{\exp (\hbar \omega / \tau) - 1}$$

- the form $x = A e^{i\omega t}$ for hamonic oscillators leads us to assume amplitude and frequency are independent for phonons

- N coupled oscillators have 3N modes (reference: goldstein 6.4), so phonons have 3N modes in contrary to $\infty$ for photons. **A bound is thus introduced for the integration in phase space**, given by the ***debye frequency***. 
- Debye phonon is characterized by $C_V \propto \tau^3$ at low temperatures. 