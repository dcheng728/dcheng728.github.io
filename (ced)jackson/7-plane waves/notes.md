
# polarization
When complex notation is used, keep in mind that we are only talking about the real part.

- The wave equation 
$$\nabla^2 \vec{E} = c^{-2} \frac{d^2}{dt^2}\vec{E}$$
gives 3 wave equations in x,y,z components of E, they all travel at speed c. 
Yet these 3 components are not independent, Maxwell equation dictates the wave be transverse.
So let $k$ = wave vector, $e_1,e_2$ two mutually orthogonal bases in transverse plane. 
- The **polarization** vector gives the direction of E, which is a linear combination of $e_1, e_2$.
If the direction of $\vec{E}$ is constant (see caution), we say the wave is **linearly** polarized, otherwise it's **elliptically** polarized. 
- CAUTION: elliptical polarization is written by Jackson as 
$$\vec{E} (\vec{x},t) = (E_+ e_+ + E_- e_-)e^{i \vec{k} \cdot \vec{x} - i \omega t}$$ 
where $e_{\pm} = \frac{1}{\sqrt{2}}(e_1 \pm ie_2)$ represent circularly polarized waves of positive and negative helicity 
(check: fix $\vec{x} = 0$, Re($e_+e^{-i \omega t}$) $\propto \cos[\omega t] e_1 + \sin [\omega t] e_2$). 
The quantity $E_+ e_+ + E_- e_-$ is a constant, **complex** number. 
It does not mean the direction of $\vec{E}(\vec{x},t)$ is constant; 
for the real part of $(E_+ e_+ + E_- e_-)e^{i \vec{k} \cdot \vec{x} - i \omega t}$ may change. 
- In the for  of the elliptical polarized wave form $$\vec{E} (\vec{x},t) = (E_+ e_+ + E_- e_-)e^{i \vec{k} \cdot \vec{x} - i \omega t}$$ 
if the $E_+, E_-$ have same phase then the principal axes don't get a phase, 
if they differ by some phase $e^{i\alpha}$, this phase difference can be canceled out by the transformation
$e_+ \rightarrow e^{i\alpha/2}e_+$, $e_- \rightarrow e^{-\alpha/2}$ which corresponds to 'rotating the ellipse'.
See jackson's fig 7.4. 

# boundary value problems
- Use boundary conditions of maxwell equations to set up, **the entire wave must be considered as a whole! e.g. you can not consider a wave propagating from A to B to C by successively applying result of A to B, then B to C, see exercise 7.2.** 

# model for dispersive media

**dispersive:**  whenever the speed of wave depends on its frequency, the medium is dispersive

- any small displacement near equilibrium is SHO <=> any function at local min resembles a quadratic polynomial
