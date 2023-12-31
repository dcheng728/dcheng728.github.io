The Feynman Rules


- There is obvious advantage in using a perturbation technique which keeps lorentz invariance and causality (cluster decomposition principle) manifest at all stages of the expansion.
- The old-fashion perturbation theory was not one of those advantageous techniques. The Feynman-Schwinger-Tomonaga is one of those advantageous technique above.
- This chapter outlines the diagrammatic calculational techniques first described by Feynman at Poconos Conference in 1948.

Feynman was led to these diagrammatic rules through his development of the path-integral approach, which will be the subject of section 9.

# Derivation of the Rules via Dyson series

\begin{itemize}
- The Dyson's series expresses the matrix element as (6.1.1)

> Recall the expression of $S$ in terms of Dyson series (3.5.10), using our newest creation and annihilation operator formalism, we put the free fields on both sides of (3.5.10), and putting the corresponding creation and annihilation operators between the free fields and $S$ yields (6.1.1)

- The field of a specific particle that transforms under a particular representation of the homogeneous lorentz group, is given by (6.1.3)

> This can be understood as the 'wave equation' of the particle, which contains everything we can possibly know about such particle. The integral over those coefficients imply that this is a localized particle, or 'wave packet'.

- weinberg here convenes a distinction between particles and antiparticle:
    - field operators that destroy particles and create antiparticles are '\textbf{fields}'
    - field operators that destroy antiparticles and create particles are '\textbf{field adjoints}'
- We now move the $\ap$s on the left of (6.1.1) to the right, using the commutator relations (6.1.4, 5, 6).
- In this way, the contributions to (6.1.1) are those arising from the delta function terms on the right-hand side of (6.1.4). The contribution to (6.1.1) of a given order in each of the terms $\Ham_i$ in the polynomial $\Ham(\psi(x),\psi^\dag(x))$ is given by a sum, over all the ways of pairing creation and annihilation operators, of the integrals of products of factors, in the 6 ways in (5.1.9-14)\footnote{These pairings are derived very trivially from 6.1.4 and 6.1.3}
- The S-matrix is obtained by multiplying these factors together, along with additional numerical factors to be discussed below, then integrating over $x_1,x_2,...,x_N$, then summing over all pairings, and then over the numbers of interactions of each type.
- It is probably worth nothing that Feynman diagrams are simply a diagrammatic mnemonics for keeping tracks of the terms that we encounter in moving the annihilation from left to right in (6.1.1) according to the rules between (6.1.9) and (6.1.14), which tells you how to handle $\ap$ with $\psi$, $\ap$ with $\ap^\dag$, and $\ap$ with time-ordering, respectively. Keep in mind that the lines represent a pairing that you can have. Figure 6.1 tells you more specifically what the pairings corresponds to. 

# The rules
The rules for calculating the S-matrix are conveniently summarized in temrs of Feynman diagrams. Each vertex in the diagrams represent one of the $\Ham_i$, and each of the lines represent a pairing described above.

- arrows always point \textbf{in} the direction that a \textbf{particle} is moving, and \textbf{opposite} to the direction an \textbf{antiparticle} is moving.
- To compute the contribution to the S-matrix for a given process, of a given order $N_i$ in each of the interaction terms $H_i$ in (6.1.2), we carry over the following steps:
    - draw all feynman diagrams consisting of $N_i$ vertices of each type $i$, and containing a line coming into the diagram from below for each particle/antiparticle in the initial state, and a line going upwards out of the diagram for eevery orticle in the final state, together with any number of internal lines running from one vertex to another, as required to give each vertex the proper number of attached lines. Each vertex is labeled with an interaction type $i$ and spacetime coordinate $x^\mu$. Each internal or external line is labeled at the field $\psi_l(x)$ or $\psi_l^\dag(x)$ that creates or destroys the orticle at that vertex, and each external line where it enters or leaves the diagram is labeled with the quantum numbers $\pp, \sigma, n$ or $\pp' \sigma', n'$ of the initial or final orticle.
    - For each vertex of type $i$, include a factor $-i$, obviously from $(-i)^N$, and a factor $g_i$, the coupling constant. For every final orticle, include a factor of (6.1.9,10), For every initial orticle, include a factor of (6.1.11,12). For internal lines include factors of (6.1.13,14)
    - Integrate the product of all these factors over the coordinates $x_1, x_2, ...$ of each vertex
    - Add up the results obtained in this way from each Feynman Diagram. The complete perturbation series for the S-matrix is obtained by adding up the contribution of each order in each interaction type, up to whatever order our strength permits.
- Some special rules apply for specific scenarios:
    - Suppose that an interaction $\Ham_i(x)$ contains $M$ factors of the same field. Then we get an additional factor of $M!$ in front of each diagram. The traditional method to combat this is to adjust the coupling factor to $\frac{g}{M!}$ in the $M$-th order expansion.
    - Remember how the permutations of the vertices cancel with the factor of $\frac{1}{N!}$, this is not always the casae because some permutations of the vertices do not necessarily produce a new diagram. This occurs when we have loop diagrams. In loop diagrams, we need to add an additional factor of $\frac{1}{N}$.
    - Whenever permutation puts the annihilation part $\psi^+(x)$ of a field in $\Ham$ just to the left of the creation part $\psi^{+\dag}(y)$ of a field adjoint in $\Ham(y)$, the permutation that puts the annihilation part $\psi^{-\dag}(y)$ of the field adjoint just to the left of the creation part $\psi^-(x)$ of the field involves one extra interchange of fermion operators, yielding the minus sign in the second term of (6.1.14) for fermions.
- The overall sign of the S-mat does not matter, but the relative signs do.
- general Feynman diagrams form either chains of lines that pass through the diagram with arbitrary number of interactions (traditional >--< diagrams), or else fermionic loops (loop ---->O< diagrams)

