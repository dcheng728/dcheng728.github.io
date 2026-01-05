- ordinary optical refraction happens at 500A in crystals

- bragg diffraction (crystal diffraction) can be used to select a special spectrum of beam

- bragg law: $2d \sin{\theta} = n \lambda$, this is the recurring theme of this chapter and will be echoed in the next chapter

# reciprocal lattice and fourier
- in the fourer expansion of a function on the lattice, periodicity only allows terms with the same periodicity as the lattice in phase space. This defines the **reciprocal** lattice. Thus we can say the function is expanded on the reciprocal lattice in phase space:
$$n(x) = \sum_p n_p \exp{i \frac{2 \pi p}{a} x}$$
where $\frac{2 \pi p}{a}$ is a point in the *reciprocal lattice*, with dimension of inverse distance. 

- periodicity is the realm of fourier analysis

- If $\vec{a}_1, \vec{a}_2, \vec{a}_3$ are primitive vectors of the crystal lattice, the primitive vectors of the reciprocal lattice $\vec{b}_1, \vec{b}_2, \vec{b}_3$ are give by 
$$\vec{b}_i = 2 \pi \frac{\vec{a}_j \times \vec{a}_k }{\vec{a}_i \cdot \vec{a}_j \times \vec{a}_k}$$

- the diffraction pattern of the crystal is a map of the reciprocal lattice
- a reciprocal lattice vector $G=h b_1 + kb_2 + lb_3$ is normal to the plane (hkl) planes of direct lattice

# brillouin zones
- a brillouin zone is defined as a wigner-seitz primitive cell in the reciprocal lattice
- only waves whose wavevector $\vec{k}$ drawn from the origin terminates on the surface of the brillouin zone can be diffracted by the crystal

- sc has reciprocal of sc
- bcc and fcc are reciprocals of each other

# some fourier analysis
- by assuming refraction amplitude proportional to electron density, the total amplitude of the scattered wave in direction $k'$ from original wave in direction $k$ can be written as a function modulo the lattice with a function of the directions, such as below
$$n(\vec{r})dV \times \exp{[i(\vec{k} - \vec{k}') \cdot \vec{r}]}$$
scattering amplitude for crystal with $N$ cells can be written as 
$$F_G = N \int_{cell} dV n(\vec{r}) \exp{-i\vec{G} \cdot \vec{r}} = N s_G$$
where $s_G$ is the structure factor. 
- the structure factor contains single-cell information 
- atomic form factor is integrated over all space

# TODO:
- understand structure factor and form factor
