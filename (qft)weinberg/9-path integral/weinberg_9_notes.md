path integral methods

- the awkwardness in obtaining simple results in the last chapter hinders canonical formalism from being applied to more complex theories (non-abelian gauge, general relativity, etc)
- (1960s) fadeev, popov and dewitt showed how to apply it to non-abelian gauge theories and general relativity, this revived path integral approach
- (1971) t'hooft used path-integral methods to derive the feynman rules for spontaneously broken gauge theories, including weak and electromagnetic interactions, in a gauge that made the high energy behavior of these theories transparent. this was a turning point for path integral
- in this chapter we derive the path integral formalism from canonical formalism, and see what additional sorts of vertices are needed to supplement the simplest version of the feynman path-integral method. 

# the general path integral formula
- weinberg begins with the general formalism for quantum mechanics (9.1.1-12)
- the key insight is that after considering general $<q':t | q,t>$, weinberg considers the transition into a state with infinitesmal increment of time: $< q': \tau + d\tau | q: \tau>$
- this can be written with $d\tau$ taken to be $N$ tiny slices of $d\tau/N$, and we obtain a semi-main equation (9.1.26) in the limit of $N \rightarrow \infty$ this becomes a integral and we obtain a main equation (9.1.34) which is a constrained path integral. Physically this is the integral of all path that take $q(\tau)$ from $q$ at $\tau = t$ to $q'$ at $\tau = t'$. 
- the great advantage of writing matrix elements in this way is that the path integrals are easy to calculate when expanded in powers of the coupling constants in $H$
- the path integral formalism allows us to not only compute transition probability between states, but also matrix elements between states with time-ordered products of general operators in between (9.1.35-38).

# transition to the s-matrix

- if we want to convert the result of (9.1.34) to a notation appropriate to qft, we shall let the index $a$ run over all points $\vec{x}$

> The idea being instead of all paths from point to point, we are integrating over all fields that take on the initial and final conditions
    
in space and over a spin and species index $m$, and replacing $Q_a(t)$ with $Q_a(\vec{x},t)$, same for $P$.

- Then to get the $S$ matrix element we just need to take the $t\rightarrow \pm \infty$ limits in the final and initial states. 
- some derivations later we find an expression for the annihilation operators in the in and out states (9.2.7), together with (9.2.8), we have a differential equation to solve
- going with a gaussian ansatz, and the solution of vacuum expectation value of time ordered products can be expressed as (9.2.17). recall that in 6.4 we learned that the S-mat element is like the vacuum expectation value of t-ordered products, so this marks a intermediate stoppoint.

# lagr version of path integral

- In (9.1.38), if $H$ is of the form (9.3.1), then the exponential part of (9.1.38) can be written as the corresponding lagrangian (9.3.1-10)
- however, there are some additional caveats with (9.3.10), being the determinant of $\mathscr{A}$.
    - recall 
        $$M = \frac{ < VAC | T{...} | VAC> }{< VAC | VAC > }$$
        so if this determinant amounts to some constant, then we have no problem (this would be the case for a set of scalar fields)
    - HMANASS, weinberg gives an example of a 'nonlinear $\sigma$ model' whose lagrangian density amounts to the determinant of $\mathscr{A}$ having exponential dependence on the trace of a term in the lagrangian. we can regard this determinant as providing a correction ($\Delta \mathscr{L}$) to the effective lagrangian density. This means we can still interpert the exponential part as an exponential of a lagrangian, but the lagrangian needs to be modified.
    - HMANASS, weinberg gives another example where we need to add a correction to the lagrangian density in order to keep the $e^{i\int \mathscr{L}}$ interpretation. 
    - [❤️] In order to keep the exponentiated action interpretation, we add a $i\epsilon \times (\text{terms})$ to the lagrangian, giving (9.3.11). 

# path integral derivation of the feynman rules

- using the equation for $M$ (9.4.1), and our newly derived interpretation of $e^{i I[\psi]}$ as the weight function in the path integral (9.3.11), we obtain a formula for $M$: (9.4.2). 
- dividing the lagrangian into a free and interaction part, we get the action in free and interaction parts as well (9.4.4-7)
- by adopting the actio weighting function interpretation, we have assumed that the lagrangian is quadratic in the fields, so we can always write the free action in the \textbf{generalized quadratic form} (9.4.8-9.4.11)
- To deal with interactions, we will expand the exponential in powers of $I_1$ and then $I_1$ in powers of the field (9.4.12)
- The general integral that we encounter both in the numerator and the denominator of (9.4.2) are of the form $\mathscr{J}$ in (9.4.13)
    > the $\psi$s can be taken to be 1 to get the denominator using some formula in the appendix, this can be written as (9.4.14), which amounts to the instructions of drawing feynman diagrams. what's left is to check that the factors of each vertex/line match the feynman rules we derived earlier
- the propagator in the path integral approach can be written as (9.4.15), some derivations later we find that its the same as the propagator we found earlier (9.4.16-18). 
- weinberg then goes on to show that the same equivalence between path integral and feynman rules holds for another unperturbed lagrangian (the previous example was with a scalar field), and that the same holds for a lagrangian with derivative couplings.  
