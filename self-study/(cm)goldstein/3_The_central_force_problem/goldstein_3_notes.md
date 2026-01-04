## Separation of COM and relative motion

- the relative energy of two particles about their COM is 
$$T' = \frac{1}{2}m_1 \vec{r}_1^2 + \frac{1}{2}m_2\vec{r}^2_2,$$
where $\vec{r}_1, \vec{r}_2$ are polar vectors to the COM. Goldstein shows
$$T' = \frac{1}{2}\frac{m_1 m_2}{m_1 + m_2} \dot{\vec{r}}^2$$
where $\vec{r}$ is the separation between particle 1 and particle 2. Below I show an algebraic derivation.


### algebraic derivation of separation of COM kinetic energy

$$T \propto m_1 \dot{q}_1^2 + m_2 \dot{q}_2^2$$

$$=  \frac{1}{(m_1 + m_2)} \left[ m_1(m_1 + m_2) \dot{q}_1^2 + m_2(m_1 + m_2) \dot{q}_2^2 \right]$$

$$=  \frac{1}{(m_1 + m_2)} \left[ m_1^2 \dot{q}_1^2 + m_2^2 \dot{q}_2^2 + m_1m_2 \dot{q}_1^2 + m_1m_2 \dot{q}_2^2  \right]$$

$$=  \frac{1}{(m_1 + m_2)} \left[ (m_1 \dot{q}_1 + m_2 \dot{q}_2)^2 -2m_1m_2\dot{q}_1\dot{q}_2 + m_1m_2 \dot{q}_1^2 + m_1m_2 \dot{q}_2^2  \right]$$

$$=  \frac{1}{(m_1 + m_2)} \left[ (m_1 \dot{q}_1 + m_2 \dot{q}_2)^2 + m_1m_2(\dot{q}_1 - \dot{q}_2)^2  \right]$$

$$=\frac{1}{m_1+m_2}(p_1^2 + p_2^2) + \frac{m_1 m_2}{m_1 + m_2}(\dot{q_1}-\dot{q_2})^2$$

This identifies a COM term and effective mass term. 

## goldstein 3.3

- for 2 bodies under central force, examining the magnitude of the radial vector gives a 1D problem. The fictitious centrifugal force is introduced: 

$f \rightarrow f' = f + \frac{l^2}{mr^3} <=> V \rightarrow V' = V + \frac{1}{2}\frac{l^2}{2mr^2}$

## goldstein 3.4
- by considering $G = \sum_i \vec{p}_i \cdot \vec{r}_i$, and taking time average, we arrive at
$$<T> = -\frac{1}{2}<\sum_i \vec{F}_i \cdot \vec{r}_i>$$
this is the **virial theorem**
- goldstein claims that the virial theorem can be used to argue the **ideal gas law**

# 3.5 the differential equation for the orbit and integrable power-law potentials
- $l dt = mr^2 d\theta \Rightarrow \frac{d}{dt} = \frac{l}{mr^2}\frac{d}{d\theta}$ 
- [ ] make sense of the equation above, in terms of the differentials
- goldstein argues that if $\theta$ satisfies the eqm, $-\theta$ does as well
- not every power of $r$ in $V = ar^{n+1}$ can be solved by integration. Only for $n=1,-2,-3$ have trig solns. For $n=5,3,0,-4,-5,-7$ have elliptic soln. 

# 3.7
- $$\theta = \theta' - \arccos \left[\frac{\frac{l^2 u}{mk}-1}{\sqrt{1+\frac{2El^2}{mk^2}}} \right]$$
- finds eqm for inverse square central force
- for elliptic orbits the major axis depends solely upon the energy, this is argued by solving a quadratic formula
- eccentricity (semiminor axis) governed by angular momentum
- [ ] eccentricity
## intuition for semimajor and semiminor axis
- $$E = \frac{1}{2}m\dot{r}^2 + \frac{1}{2}\frac{l^2}{mr^2} - \frac{k}{r}$$
is the energy of the system, when $\dot{r} = 0$, this defines a purely algebraic, quadratic equation, the roots of which gives 2 exterme points of $r$, the bigger one is semimajor, smaller one is semiminor.
- angular velocity $\dot{\theta}$ attains its max value at perihelion, minimum at aphelion

# 3.8 motion in time in kepler problem
- it is customary to measure polar angle by setting $\theta=0$ at perihelion (point of closest approach, highest angular velocity) 

# 3.10 scattering in central force fields
$$\sigma(\Omega) d\Omega = \frac{\# \text{particles scattered into solid angle } d\Omega \text{ per unit time}}{\text{incident intensity}}$$
$d\Omega = 2\pi \sin \theta d \theta$
