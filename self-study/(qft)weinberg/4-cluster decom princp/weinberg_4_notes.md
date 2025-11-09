

Cluster Decomposition Principle
- We can express the Hamiltonian by giving its matrix elements between states with arbitrary number of particles. We will do so via a bunch of creation and annihilation operator, the benefit of this approach is that if a certain condition on the $\ap \ap^\dag $s in the Hamiltonian are satisfied, the S-matrix will satisfy the **cluster decomposition principle**, which will imply **locality** is obeyed.
> **local**: events separated by spacelike vectors can not influence each other 
    
-  It can be argued that the cluster-decomposition principle plays a role in field theory inevitable, because past attempts to formulate a relativistic quantum theory without using field theory have either failed lorentz invariance or the CDP.

# Structure of this chapter:

- discuss the basis of states containing arbitrary \# of bosons and fermions
- define the creation and annihilation operators
- show how to construct the Hamiltonian that yields the S-matrix that satisfies the CDP

# Bosons and Fermions

- the **bose and fermi statics** state that bosons are symmetric under exchange while fermions are antisymmetric
    $$\Phi_{p_1, p_2} = \pm \Phi_{p_2, p_1}$$
- we will define the bosons to be the ones that take the plus sign, and fermion as the ones that take the minus sign
- claim: all particles are either bosons or fermions
    - Suppose there exists another particle that is not fermion or boson, meaning its eigenvalue under exchange is $\alpha \neq \pm 1$, then consider an arbitrary state under two operations of exchange, find that the original state gets scale by a nontrivial value $\alpha^2$ $\Box$
    - the above argument depends on two operations of exchange get us back to the initial state, but this doesn't have to be the case, the state can take a tour that doesnt end back where it began. This would be a problem in two-dimensional space, but not in 3,4, and will come in section 9.7. This would be a problem if the $\alpha$ depends on more things than the species of the particles, and is assumed away in the cluster decomposition principle
- We now want to mathematically define a bunch of states that contain bosons and fermions, and is symmetric under exchagne of boson-boson, boson-fermions, but asymmetric under exchange of fermion-fermion. Such is accomplished with delta functions on all permutations, shown on page 172 

# Creation and Annihilation Operators

- The creation and annihilation operators in Weinberg specifically operate on the states that obey the exchange statistics of bosons and fermions defined by Weinberg
- The annihilation operators of both bosons and fermions annihilate the vacuum
- These operators obey the following commutation/anti-commutation relation:
    $$a(q')a^\dag(q) \mp a^\dag(q)a(q') = \delta(q' - q)$$
    where the anticommutator is for fermion-fermion, commutator for everything else
    - Claim: Any operator maybe expressed as a sum of products of creation and annihilation operators
        - Begin with $\braket{\Psi_0}{\mathscr{O}\Psi_0} = C_00$, the rest follows pretty intuitively as on page 175
- the lorentz transformation rules for the creation operators are on page 177
- the transformation rules for the creation operators under the discrete transformations are beneath

# Cluster Decomposition and Connected Amplitudes

- The cluster decomposition principle simply states that experiments that are sufficiently separated in space have unrelated results
- Consider a process where $A = \{a_1, a_2, a_n\} \rightarrow B = \{b_1,b_2, ..., b_m\}$, the S-matrix element would be $S_{AB}$
    -Think about all the possible processes that could have led to this happening, we can have $a_1 \rightarrow b_1$, the rest doing the corresponding, or $a_1 \rightarrow b_2$, the rest doing the corresponding, or $a_1, a_2 \rightarrow b_1, b_2$, and the rest doing the corresponding...
    - without a doubt, there is a way to represent such multistate transition with combinatorics, and it will involve using $(-1)^?$ terms because some of the terms in the combinatoric monster will involve fermion-fermion exchange.
    - Indeed, we find that $S_{\beta \alpha}$ corresponds to a sum over all different ways of partitioning the particles in $A$ to clusters that goes to clusters in $B$
- the cluster decomposition principle is a statement that if $\alpha_1 \rightarrow \beta_1 $, $\alpha_2 \rightarrow \beta_2 $, ... $\alpha_n \rightarrow \beta_n $ are studied in $n$ labs that are very far from each other, the amplitude $S_{\beta \beta}$ factorizes as it would for Prob[AB]=Prob[A]Prob[B], in other words, we can treat the processes as independent events
- the recursively defined connected parts of the S-matrix gives us a way to rewrite $S_{\beta \alpha}$, thus another way to state the cluster decomposition principle, the recursiveness comes from the fact that the connected 1-particle component to define the connected 2-particle component, ...
- This gives a restatement of the cluster decomposition principle, into the statement that $S_{\beta \alpha}^C$ vanishes if any particles in the state $\beta$ or $\alpha$ are far from any others

# Structure of the interaction
- How do we formulate a Hamiltonian that respects the Cluster decomposition principle? The answer is if the Hamiltonian satisfies (4.4.1), (4.4.2).
- "the trusting reader may prefer to skip the rest of this chapter, and move on to consider the implications in chapter 5", I trust you! So I ll skip!










