\subsection{Quantum Fields and Antiparticles}

In this chapter, quantum fields will be introduced, during its construction, as a result of the union between special relaticity and quantum mechanics, we will encounter

\begin{itemize}
    \item the connection between spin and statistics
    \item the existence of antiparticles
    \item relationships beteween particles and antiparticles, such as CPT
\end{itemize}

\subsubsection{Free fields}

\begin{itemize}
    \item We would like to construct a Hamiltonian out of creation and annihilation operators, from (4.2.12) we know that under Lorentz transformations each of those operators is multiplied by a matrix that depends on the momentum of the operator, and the whole thing may not look as nice, because the Hamiltonian has different operators at different momentum the coefficients would be fked up, we would like to solve this issue.
    \item the solution is to construct the Hamiltonian out of \textbf{creation} and \textbf{annihilation} \textbf{fields}, $\Psi^-, \Psi^+$, respectively, (5.1.4, 5.1.5)
    \item the nice thing about this is under lorentz transformation, each field is multiplied by a position-independent matrix 
    \footnote{See (5.1.6, 5.1.7, the $D_{\bar{l} l}$) on the RHS is the matrix that weinberg is referring to},
    furthermore, we find that these $D$-matrices furnish a representation of the homogeneous lorentz group. 
    
    \item (4.2.12) gives us the transformation rules of the $\ap^\dag$, we take its adjoint and find the transformation rules of both $\ap, \ap^\dag$. Then putting the transformation rules of $\ap, \ap^\dag$ with that of $\Psi^\pm$, we find the transformation rules of coefficients $u,v$ of $\ap, \ap^\dag$ in $\Psi^\pm$ under general Lorentz transformation (5.1.13, 5.1.14), these are the fundamental requirements that will allow us to calculate the $u,v$
    
    \item[\HEART] We then take the rule above, and plug in pure translations, boosts, and rotations, and find
    \begin{itemize}
        \item \textbf{translation}: we get a general rule for arbitrary homogeneous lorentz transformation $\Lambda$ (5.1.19, 5.1.20)
        \item \textbf{boosts}: we get a relation between $u,v$ at $0$ momentum and some nonzero momentum (5.1.21, 5.1.22)
        \item \textbf{rotations}: we get a relation between $u,v$ of different spin $\sigma, \bar{\sigma}$ (5.1.23-5.1.26), notice that the summation on the LHS of these equations is over $\bar{\sigma}$, and that on the right is over $l$, which is an index in the coefficients $u,v$. 
    \end{itemize}
\end{itemize}

\paragraph{Causality}

\begin{itemize}
    \item We check the causality condition of the general free field constructed with coefficients in front of a continuous spectrum of creation and annihilation operators.
    \item The tator 
    \footnote{tator means commutator/anticommutator}  
    $[\psi^+(x),\psi^-(y)]$ in (5.1.30) does not vanish in general. This means \ul{we can not have fields that are created purely with creation operators, or fields that are purely annihilation operators}. So the natural thing is to try linear combinations of the creation and annihilation fields:
    \[\kappa \psi^+ + \lambda \psi^-\]
    We will see later that WLOG $\kappa = \lambda$ so we are only free to choose the scale of the field.
    \item we see that in order for this theory to conserve quantum numbers like electric charge, there must be a doubling of particle species carrying non-zero values of such quantum numbers: if a particular componenet of the annihilation field destrooys a particle of species $n$, then the same component of the creation field must create particles of species $\bar{n}$, \ul{this is the reason for antiparticles}.
\end{itemize}

\paragraph{Conserved Quantum Number}
\begin{itemize}
    \item Lets say each particle carries some quantum number, and there is some sort of conservation law for that quantum number. Then creation of a particle would add such number and annihilation takes away such number. 
    \item Formulating this in terms of mathematics: Suppose the Hermitian operator $Q$ corresponds to the observable of quantum number $q$ that the particle carries. Then we necessarily have
    \[[Q,\ap] = Q\ap - \ap Q = -q \ap\]
    \[[Q, \ap^\dag] = Q\ap^\dag - \ap^\dag Q = q \ap^\dag\]
    \footnote{because $\ap Q$ first makes a measurement, then takes the particle away, and $Q \ap$ makes the measurement after the particle is taken away, so the former measurement seems to observe an additional $q$. Similar idea for the latter tator relation.}
    \item Recall the form of our Hamiltonian $\Ham$ in terms of the creation and annihilation fields (5.1.9)
    \footnote{
    It would be fair to say $\Ham$ is a polynomial in $\psi^+$, $\psi^-$
    }:
    \begin{align*}
        \Ham = &\sum_{NM} \sum_{l'_1 ... l'_N} \sum_{l_1 ... l_M} g_{l'_1...l'_N,l_1...l_M}\\
        & \psi^-_{l'_1}...\psi^-_{l'_N} \psi^+_{l_1}...\psi^+_{l_M}
    \end{align*}
    Weinberg claims that in order for the Hamiltonian to commute with $Q$, it is necessary that the Hamiltonian be formed out of fields that have simple commutation relations with $Q$, meaning $[Q, \psi_l] = -q_l \psi_l$\footnote{I don't understand why this HAS to be the case right now, I see why it would be nice, but I ll take his words.}.
    \item But this is clearly not the case for $\psi = \ap + \ap^\dag$, unless $Q=0$. 
    \footnote{for $[Q,\psi] = [Q, \ap + \ap^\dag] = -q(\ap- ap^\dag)$.}
    \item A possible solution would be to introduce another particle that carries the opposite charge. This is the idea behind \textbf{antiparticles}.
\end{itemize}


\textbf{causal}: fields commute at spacelike separations.

\subsubsection{Causal Scalar Fields}

\paragraph{what 'scalar' means}
\begin{itemize}
    \item scalar representation means the field only takes on a scalar value at each point in spacetime, for that value to be Lorentz invariant \ul{it must be a Lorentz scalar}. 
    \item[\RA] Recall the definition of the annihilation field in terms of its operator and coefficient
        \[\Psi^+_{\boxed{l}}(x) = \sum_{\sigma n} \int d^3 u_{\boxed{l}} (x;\pp, \sigma, n) a(\pp, \sigma, n) \]
        having scalar field means \ul{we can remove this $l$ index}, 
        again, keep in mind that the field only takes on a scalar value at each point in spacetime!
    \item[\RA] the field being just a scalar means the \textbf{matrix} $D_{\bar{l} l}(\Lambda)$ that we were talking about is \ul{simply a \textbf{scalar}: $D(\Lambda)$}!
        \item[\RA] In his book weinberg considers the simplest representation where $D(\Lambda)=1$
\end{itemize}


\paragraph{spin 0 is necessary}
\begin{itemize}
    \item Recall that the $D^{(j)}$ representation of the rotation group is dim $2j + 1$, so for this representation to be a scalar representation we necessarily have spin = 0. A scalar field necessarily describes particle with 0 spin.
    \item[\RA] we can drop the $\bar{\sigma},\sigma$ labels because they only take on the value of 0, assuming we are working with one species of particles, we can drop the $n$ as well, so we write
    \[u = u(p), v = v(p)\]
    \item it is conventional to normalize the annihilation and creation fields so that
    $u(0) = v(0) = \sqrt{\frac{1}{2m}}$, so we have
    \[u(\pp) = \sqrt{\frac{1}{2p^0}}, 
    \quad
    v(\pp) = \sqrt{\frac{1}{2p^0}}\]
\end{itemize}

\paragraph{implications of causality}
\begin{itemize}
    \item That's for the invariance under lorentz transformation, for causality, we need the fields to commute at spacelike separations. We find that while $[\phi^\pm , \phi^\pm]_{\mp} =0$, $[\phi^\pm , \phi^\mp]_{\mp}$ is not necessarily 0 for spacelike separations. 
    \item To address this problem, we find that (5.2.6-5.2.9) the constants for both fields \ul{$\kappa, \lambda$ must be equal in magnitude}, and \ul{we must be considering the boson}, in other words, the \textbf{commutator} instead of \textbf{anticommutator}. This solution works by exploiting the evenness of $\Delta_+$. 
    \item we can redefine the relative phase of the creation and annihilation operators so that $\kappa$ and $\lambda$ are equal exactly (5.2.10)
\end{itemize}

\paragraph{scalar fields need anti-particles for conserved charge}
\begin{itemize}
    \item The issue here is that $[Q, \phi^+] = -q\phi^+$, $[Q, \phi^{+\dag}] = q\phi^+$, we will have 
    \[[Q, \phi^+ + \phi^{+\dag}] = q (\phi^{+\dag} - \phi^+)\]
    this is not a commutation relation that allows for charge conservation.
    \item Indeed, if the particles that are destroyed and created by $\phi$ carry some conserved quantum number like electric charge, then $\Ham$ will conserve the quantum number if and only if each term in $\Ham$ contains equal number of $\ap$ and $\ap^\dag$, but this would be impossible if $\Ham$ is a polynomial in $\ap + \ap^\dag$. 
    \item[\HEART] In order for the scalar field to have conserved charge, we must imagine there is another field of the particle with opposite charge， let these two fields be $\phi^+, \phi^{+c}$, then we form the field by
    \begin{align*}
        \phi &= \phi^+ + \phi^{+c\dag} \\
        & = \int \frac{d^3 p}{(2\pi)^{3/2} (2 p^0)^{1/2}} 
        \left[ a_{\pp}e^{ip\cdot x} + a_{\pp}^{c\dag}e^{-ip \cdot x}\right]
    \end{align*}
\end{itemize}

\paragraph{MISC}
\begin{itemize}
    \item The commutator of the complex scalar field with its adjoint is
    \[[\phi(x), \phi^\dag(y)] = \Delta(x-y) = \Delta_+(x-y) - \Delta_+(y-x)\]
    \begin{itemize}
        \item Parity: The intrinsic parity of a state containing a spinless particle and its antiparticle is even.
        \item Charge Conju: The intrinsic charge conjugation parity of a state consisting of a spinless particle and antiparticle is even. If the particle is its own antiparticle, the charge conjugation must be real, $\pm 1$
        \item Merlin: even, real if its own antiparticle. 
    \end{itemize}
\end{itemize}

\subsubsection{Causal Vector Fields}

We first follow the same procedure as we did for the scalar field (5.3.1-5.3.5), we encounter a difference when it comes to spin of the particle: vector field can have nontrivial spin (5.3.6, 5.3.7).
Thus we need to examine spin by looking at the rotation transforamtion properties of the vector field, by looking at the rotation generators $\mathscr{J}^\mu_\nu$


\paragraph{Rotation Generator}

\begin{itemize}
    \item The rotation generators are
    \[\left(\begin{array}{rrr}
     0 & 0 & 0 \\
     0 & 0 & -i \\
     0 & i & 0
     \end{array}\right),
     \left(\begin{array}{rrr}
     0 & 0 & i \\
     0 & 0 & 0 \\
     -i & 0 & 0
     \end{array}\right),
     \left(\begin{array}{rrr}
     0 & -i & 0 \\
     i & 0 & 0 \\
     0 & 0 & 0
     \end{array}\right)\]
     squaring them, and adding them up yields $2\delta^i_j$.
    \item We know that in the four vector representation of the rotation group, the time component is zero, pluggint this into (5.3.6, 5.3.7) we obtain (5.3.12, 5.3.14). Plugging in our our last result of $2\delta$ into (5.3.6, 5.3.7), we find (5.3.13, 5.3.15).
    \footnote{Recall that $(J^{(s)})^2 = s(s+1)$, so it may seem like for the $2\delta$ to be true, we must have $s =1$, but that would be the case if the rotation generators are the entire story of this representation. Which isnt the case because there is also another component of time. If the spatial components is nonzero and nontrivial, then we necessarily have $s=1$. However, there is another solution of setting the spatial components trivially to be 0, which would allow us to set $s=0$. }
    \begin{itemize}
        \item \textbf{Possibility 1:} at $\pp=0$, only $u^0, v^0$ are nonzero and $s$ (or $j$) equals 0.
        \item \textbf{Possibility 2:} at $\pp =0$, only $u^i, v^i$ are nonzero and $s = 1$.
    \end{itemize}
\end{itemize}

\paragraph{Spin 0}
\begin{itemize}
    \item The conventional values for $u^0, v^0$ are
    \[u^0, v^0 = \pm i \sqrt{\frac{1}{2m}}\]
    \item as before, we drop the $\sigma$ label for they only take on a single value of $0$
    \item[\HEART] We find that for general momenta, the coefficients are (5.3.16, 5.3.17), and we observe that the annihilation and creation fields are simply the \textbf{4-gradient of the scalar field}. Then weinberg be like thats enough i dont feel like exploring this option no more. 
\end{itemize}

\paragraph{Spin 1}
\begin{itemize}
    \item For spin 1 the label $\sigma$ can take on between $-1, 0, 1$.
    \item By the analogy of the past normalization conventions, we find the 0-momenta, 0-spin coefficients (5.3.20)
    \item Using the raising and lowering operators $J_1^{(1)}\pm iJ_2^{(1)}$, we find the spin 1, -1 coefficients at $\pp = 0$ (5.3.21, 5.3.22)
    \item[\HEART] the above two procedures give us the coefficients for $\sigma = -1, 0, 1$, now we can apply a boost to find the coefficients for any general momenta, and any of those three spins!
    \footnote{The $e^\mu(\pp, \sigma)$ vectors are a simpler way to state the the coefficients for arbitary momenta in terms of the three basis vectors $e(0,-1), e(0,0), e(0,1)$} 
    and we find the fields $\phi^{+\mu}, \phi^{- \mu}$. 
\end{itemize}

\paragraph{Spin 1 causality}
\begin{itemize}
    \item In computing the tators relations for spin 1 particle at spacelike separations, we find this $\Pi^{\mu \nu}$, which by some algebra is reduced to the familiar $\Delta_+$, which we know is even.
    \item[\RA] we apply the same procedure for causality as we did for the scalar field, and we find that for causality it is necessary and sufficient that the spin 1 particle is \textbf{boson} and $|\kappa| = |\lambda|$. So we do the same procedure as scalar to adjust the pahse of the creation and annihilation operators to get them to be exactly equal. 
    \item In addition, we find that this field is self-conjugate, so it is real which prohibits conservation of quantum number like electric charge. 
    \item What if we want to conserve a charge? We do the same thing where we imageine there is another boson with exactly the same mass, spin, but opposite charge. This will give us a complex field. 
    \item again, we can let the particle be neutral, and the boson would be its own antiparticle, and we simply conserve charge = 0.
\end{itemize}
\paragraph{spin 1 MISC}
\begin{itemize}
    \item A quick check indicates that the spin 1 field satisfies the KG equation. 
    \item we can not get electrodynamics by simply taking the $m\rightarrow0$ limit of the massive spin 1 theory, because the spacelike commutator contains a $m^2$ at the bottom (5.3.30) which blows up.
    \item weinberg then discusses something related to photon vs spin1 massive boson, then talk about discrete symmetries.
\end{itemize}

\subsubsection{Dirac Formalism}

\begin{itemize}
    \item The Dirac formalism is just one representation of the homogeneous lorentz group, but it has some \ul{special importance}
    \footnote{
    What is this special importance?
    \begin{itemize}
        \item A
        \item B
    \end{itemize}
    }. This formalism was introduced by Dirac, but weinberg wants to introduce it mathematically rather than historically
    \item from the point of view we are following here, the structure and properties of any quantum field are dictated by the \ul{representation of the homogeneous lorentz group} under which it transforms. 
    
\end{itemize}

\paragraph{Clifford Algebra}
\begin{itemize}
    \item By a representation of the homogeneous Lorentz group, we mean a set of matrices $D(\Lambda)$ satisfying
    \[D(\Lambda_1)D(\Lambda_2) = D(\Lambda_1 \Lambda_2)\]
    \item by looking at the infinitesmal transformations, we get the lie algebra of the lorentz group (5.4.4).
    \footnote{Any set of matrices satisfying the commutation relations in 5.4.4 acts as a set of generators for the some representation of the lorentz group.}
    \item the key here is that we find a set of matrices satisfying 5.4.4 via the \textbf{clifford algebra} (5.4.5 - 5.4.7).
    \item The properties of clifford algebra is explored by weinberg, the essential take away is that the clifford algebra allows us to obtain 
    \begin{itemize}
        \item lorentz scalars (5.4.9), 
        \item lorentz vectors (5.4.8), 
        \item lorentz rank-2 tensors (5.4.10), 
        \item lorentz rank-3 tensors (5.4.11),
        \item lorentz rank-4 tensors (5.4.12). 
    \end{itemize}
    All these $\uparrow$ are representations of the Lorentz group, so we can form representations of the Lorentz group using clifford algebra!
    \item the clifford algebra automatically defines a parity operator (5.4.13-16)
\end{itemize}

\paragraph{Return to 4D spacetime dimensions}
\begin{itemize}
    \item In the 4D spacetime dimensions, weinberg considers an example set of $\gamma$ (5.4.17), the Pauli spinors.
    \item recall that the pauli spinor matrices give the projection of the electron's spin along a direction. 
    \item using the relation between $\mathscr{J}$ and $\gamma$ given in (5.4.6), we find the lorentz group generators (5.4.19,20), and we find that these generators are block-diagonal, meaning we have found a reduciable representation that is simply a direct sum of two irreducible ones.
\end{itemize}

\paragraph{Convenient way to write the clifford rank4tensor}
\begin{itemize}
    \item Weinberg considers how to write the rank4 tensor $\mathscr{P}^{\rho \sigma \tau \eta}$ in a more compact way>
    \item The answer relates to the $\gamma^5$ matrix defined by $\gamma^5 = -i\gamma^0 \gamma^1 \gamma^2 \gamma^3 $, with dis definition, we then find
    \[\mathscr{P}^{\rho \sigma \tau \eta} = 4!i\epsilon^{\rho \sigma \tau \eta} \gamma^5\]
    \item This matrix $\gamma^5$ is a pseudoscalar in the following sense
    \[[\mathscr{J}^{\rho \sigma}, \gamma_5] = 0, \quad 
    \beta \gamma_5 \beta^{-1} = - \gamma_5.\]
    \item Moreover, we find $\mathscr{A}^{\rho \sigma \tau} = 3! i \epsilon^{\rho \sigma \tau \eta} \gamma_5 \gamma_\eta$.
    \item The 16 independent 4x4 matrices can therefore be taken as the components of the scalar 1 (D1), the vector $\gamma^{\rho}$ (D4), the antisymmetric tensor $\mathscr{J}^{\rho \sigma}$ (D 6), the axial vector $\gamma_5 \gamma_\eta$ (D4), and the pseudoscalar $\gamma_5$ (D1). 
    \item recall from earlier that weinberg made a statement about how the clifford scalar, vector, tensors furnish representations of the lorentz group, in addition, they are all linearly independent, and we overall got 16 linearly independent componenet? What he has done here is writing the two tensors with $\gamma_5$ matrix, simplifying this representation. 
    \item Weinberg then shows that the $\gamma_5$ matrix has unit square and anticommutes with the other four cliford matrices. This is particularly convenient, because this anticommutation relation gives us a D5 clifford algebra. 
\end{itemize}


\subsubsection{Causal Dirac Field}

\begin{itemize}
    \item Naturally, we now apply the Dirac representation
    \footnote{This simply means plugging the $\mathscr{J}$ that we obtained in the last section using $\gamma$ into the formula
    \[\sum_{\bar{\sigma}}u_{\bar{l}}(0, \bar{\sigma}) \JJ^{(j)}_{\bar{\sigma} \sigma} = \sum_{l} \mathscr{J}_{\bar{l}l} u_l(0, \sigma)\]}
    we find the two equations above (5.5.3). 
    \item By a theorem from group theory, we find that the spin of the representation must be $\frac{1}{2}$, and we further find the basis vectors (equations above 5.5.6 )
\end{itemize}

\paragraph{The following are read at an extremely cursory pace}

\begin{itemize}
    \item Weinberg notes that the coefficients $\pm c, \pm b$ are determined by the parity operator. he illustrates this point to (5.5.17, 5.5.18). 
    \item Then weinberg does what he did with all the other field: examining its causality. He finds that \textbf{the dirac formalism has to describe fermions}!
    \item then he explores the discrete transformation properties of the dirac field.
\end{itemize}

\subsubsection{General irreducible representations of the Homogeneous Lorentz Group}

\subsubsection{General Causal FIelds}

\subsubsection{The CPT theorem}
The CPT theorem states

\textit{For an appropriate choice of inversion phases, the product CPT of all the inverisons is conserved.}

\subsubsection{Massless Particle fields}

\begin{itemize}
    \item We begin by assuming that the massless particle field is also made out of the a field with creation and annihilation operators. Using the transformation relations (2.5.42), we arrive at (5.9.2, 3, 4)
    \item We find that the coefficients $u,v$ must satisfy (5.9.6,7), we simplify these equations by considering momentum-related transformations as not going from $p_1 \rightarrow p_2$, but $k \rightarrow p_2$. So we can express the general momentum coefficient $u(\pp),v(\pp)$ in terms of the standard momentum $u(\kk),v(\kk)$: (5.9.8,9).
    \item Now we zoom into the $\kk$ case, this transforms by the little group: (5.9.10,11).
    \item we find that \ul{no 4vector field can be constructed from the annihilation and creation operators for a particle of mass zero and helicity $\pm 1$. }
    \item way out: use gauge invariance, and \textbf{tensor} field!
    \item we further find that causality implies the particle be its own charge conjugate, which would be the case for a photon. 
\end{itemize}
