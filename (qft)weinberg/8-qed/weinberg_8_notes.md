\subsection{qed}


\begin{itemize}
    \item infer the need for a principle of gauge invariance from the difficulty of formulating quantum theory of massless particles with spin
    \item deduce the features of electrodynamics from gauge invariance
    \item take gauge invariance as a starting point and deduce the existence of a vector potential for massless particles of unit spin
\end{itemize}

\paragraph{gauge invariance}

\begin{itemize}
    \item there is no way to construct a 4-vector as a linear combination of the creation and annihilation operators for helicity $\pm 1$
    \item Instead of banishing $A_\mu$ from the action, we shall require that the part of the action $I_M$ for matter and its interaction with radiation be invariant under a gauge transformation 
    $A_\mu \rightarrow A_\mu +\dmu \epsilon$
    \item we'd find that the lorentz invariance of $I_M$ requires $\dmu \frac{\delta I_M}{\delta A_\mu (x)} = 0$ which implies $\frac{\delta I_M}{\delta A_\mu (x)}$ is a conserved current
    \item How to construct such current? We know that infinitesmal internal symmetries of the action implies conserved currents, in fact consider the transformation
    \[\delta \psi^l(x) = i \epsilon(x) q_l \psi^l (x)\]
    that leaves the matter action invariant for a constant $\epsilon$, when the matter field satisfies the field equations this transformation defines a conserved current $J^\mu$. 
    \item we can construct a lorentz-invariant theory by coupling the vector field $A_\mu$ to the conserved $J^\mu$ in the sense that $\delta I_M/\delta A_\mu(x)$ is taken to be proportional to $J^\mu$ from above:
    \[\frac{\delta I_M}{\delta A_\mu(x)} = J^\mu (x)\]
    \item the requirement above can be restated as a principle of invariance: the matter action is invariant under the adjoint transformations:
    \[\delta A_\mu(x) = \dmu \epsilon(x), \quad
    \delta \psi_l(x) = o \epsilon(x) q_l \psi_l(x)\]
    \begin{itemize}
        \item If $\epsilon$ is a constant, this is a global symmetry, or gauge invariance of the first kind
        \item If $\epsilon(x)$ is arbitrary, then this is a local symmetry, or gauge invariance of the second kind
    \end{itemize}
    \item Taking the radiation action to be that of (8.1.14), and imposing the equation of motion yields $0 = \frac{\delta}{\delta A_\nu} [I_\gamma + I_{M}] = \dmu F^{\mu \nu} + J^\nu$, which is the inhomogeneous maxwell equations. 
\end{itemize}

\paragraph{constraints and gauge conditions}
\begin{itemize}
    \item there are constraints that arise when we try to quantize the theory whose lagrangian we just studied above
    \item the first constraint arises from the fact that the lagrangian density is independent of the time-derivative of $A_0$, meaning $\Pi_0 = 0$. this is a primary constraint. this primary constraint leads immediately to the secondary constraint of 
    \[\partial_i \Pi^i = - J^0\]
    \item because of the partial arbitrariness of $A_\mu$ due to gauge invariance, it is not possible to apply the canonical quantization procedure directly, rather, we need to first choose a gauge.
\end{itemize}

\paragraph{choosing coulomb gauge}

\begin{itemize}
    \item choosing the coulomb gauge, and then applying dirac's method of removing second class constraints, we done.
\end{itemize}