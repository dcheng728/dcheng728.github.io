the canonical formalism

- all of the most familiar qft furnish canonical systems, and these can easily be put in a Lagrangian formalism
- The benefit of using Lagrangian formalism, a classical theory with a lorentz-invariant lagrangian density will when canonically quantized lead to a lorentz-invariant quantum theory.
- it would be hopeless to try to guess at a form of the Hamiltonian in non-abelian gauge theories without starting with a lorentz-invariant and gauge-invariant lagrangian density

# canonical variables

### Weinberg formalism to Lagr to Hamiltonian

- this section shows that various quantum theories that we have constructed so far satisfy the commutation rules and equations of motions of the Hamiltonian version of the canonical formalism, this means identifying the operators $q,p$ in theories we have considered so far (scalar, vector, tensor, etc) that satisfy the canonical commutator or anticommutation relations
    $$[q(\vec{x},t),p(\vec{y},t)]_{\mp} = i\delta^3(\vec{x}-\vec{y})$$
    $$[q(\vec{x},t),q(\vec{y},t)]_{\mp} = 0$$
    $$[p(\vec{x},t),p(\vec{y},t)]_{\mp} = 0$$
- Then weinberg uses the commutator relations between fields to find the right $p,q$ for each theory, specifically the ***real scalar field***, ***complex scalar field***, ***real vector field***, ***dirac field of non-majoranna spin 1/2 particle*** (7.1.4-16). 
- Then weinberg defines the quantum mechanical functional derivative (7.1.17,18) for a functional that takes in a system of operators that satisfy the canonical tator relations. 
- Then he transitions to the Hamiltonian formalism by identifying that the functional derivative corresponds to the time-dependence of the operators $p,q$, and observing that the free Hamiltonian $H_0$ derived in weinberg formalism is equal to that of Hamiltonian formalism up to a constant.  

### what Lagr gives free Hami

- This question may be answered by Legendre transformation from Hamiltonian to Lagrangian (7.1.26)
- Lagr: lorentz-invariant, Hami: can be used to get S-mat elements, constraint, the Lagr must correspond to the right free field hami.


### Can an interacting theory be formulated via canonical variable? 

- weinberg introduces the canonical variables in heisenberg picture. He uses capital letters for those canonical variables.
- These canonical variables are quantized in the same way as the non-interacting ones
- weinberg notes that the relation between the canonical conjugates in interacting fields $P$ and the field variables $Q$, and the field variables $\dot{Q}$ is in general not the same as for the free theory operators. 

## the lagr formalism

### How do we choose the hami?

- the easiest way to enforce lorentz invariance is via choosing a suitable lagr then derive the hami. 
- The lagrangian is a functional of $\psi^l$ and $\dot{\psi}^l$ while the conjugate fields $\pi_l$ are defined to be the $\cdot{\psi}^l$ dependence of the lagr.
- pretty standard stuff, gets Euler lagrange in (7.2.9)
- The hamiltonian is obtained via legendre transformation, it would be a functional of the lagr, $\pi_l$ and $\cdot{\psi}$.
- after obtaining the equations of motion from the lagr and hami formalism, it would be tempting to identify the field variables $\psi$ and $\pi$ with canonical variables $q,p$. This works for the simple example of real scalar field, but \textbf{does not work in general}, because there are field variables, such as the time component of a vector field or the hermitian conjugate of a dirac field, that are not canonical variables, and do not have canonical conjugates, yet lorentz invariance requires them to be in the lagr.

### getting the 'non-canonical' terms in the lagrangian

- the terms that do not behave like canonical variables are denoted $C^r$, so now we have 
    $$P_n(\vec{x},t) = \frac{\delta L[Q(t),\dot{Q}(t),C(t)]}{\delta \dot{Q}^n(\vec{x},t)}, \quad
    0 = \frac{\delta L[Q(t),\dot{Q}(t),C(t)]}{\delta C^r(\vec{x},t)}$$
- in a simple case, these equations can be solved to give $C$ in terms of $Q,P$. 

## global symmetries

the real point of lagr is that it provides a natural framework for the qm implementation of symmetry principles


## constraints and dirac brackets

- the chief obstacle to deriving the hami from lagr is the constraints, there are two types
    - \textbf{primary} constraints are either imposed on the system, or arise from the structure of the lagr
    - \textbf{secondary} constraints arise from the requirement that the primary constraint be consistent with the equations of motion. 
- weinberg says the the distinction between primary, secondary constraints is not important and he will treat them equally, but then why bother mentioning it?
- the constraints we have found for the massive vector field are of a type known as second class, which has a standard prescription for the tator relations.

### the standard prescription for some constraints

- defines poisson bracket, notice that poisson brackets satisfy the algebraic properties of commutators and jacobi identity as well.
    - a constraint is known to be \textbf{first} class if its poisson bracket with all other constraints vanishes when we impose the constraints.
    - after the first class constraints are eliminated by a choice of gauge, the remaining constraint equaitons are such that no linear combination of the poission brackets of these constraints with each other vanishes, it follows that the matrix of the poisson brackets of the remaining constraints is non-singular, these are called **second** class constraints 
    > there must be an even number of second class constraints
- Dirac suggests that when all constraints are second class, the commutator relations will be given by the dirac bracket (7.6.19-20), which satisfies the commutator relations and jacobi identity as well (7.6.21-23)
- Maskawa and Nakajima: for any set of canonical variables, governed by second class constraints, it is always possible by a canonical transformation to construct two sets of variables $Q^n, \mathscr{Q}^r$ and their respective conjugates $P_n, \mathscr{P}_r$ such that the constraints read $\mathscr{Q}^r = \mathscr{P}_r = 0$.
- we then find that the dirac bracket is equal to the poisson bracket calculated in terms of the reduced set of unconstrained canonical variables. 