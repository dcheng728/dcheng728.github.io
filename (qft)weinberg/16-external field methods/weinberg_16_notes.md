\subsection{external field methods}

\paragraph{effective action from external field}

\begin{itemize}
    \item $Z[J]$ is the vac-vac amplitude under external current $J$ coupled to $\phi$, it is given by
    \[Z[J] = \sum_{N=0}^{\infty}\frac{(iW[J])^N}{N!} = \exp{(iW[J])}\]
    where $iW[J]$ is the sum of all connected vacvac amp, counting permutations as different diagrams. This means finding Z is finding W.
    \item define $\phi_J$ to be the vac expect value of the operator $\Phi(x)$ in the presence of the current $J$, 
    or equivalently
    \[\phi_J = \frac{\delta}{\delta J(x)}W[J]\]
    \item the quantum effective action is defined as
    \[\Gamma[\phi] \cong - \int d^4x \phi^r(x) J_{\phi r}(x) + W[J]\]
    one finds $\frac{\delta \Gamma[\phi]}{\delta \phi^s(y)} = -J_{\phi s}(y)$
    it is shown that $\Gamma[\phi]$ is the sum of all connected one-particle irreducible graphs in presence of $J_\phi$
    \item $W_\Gamma [J,g]$ is for $W[J]$ when $I[\phi] \rightarrow g^{-1}\Gamma[\phi]$
    \item[\HEART] we find W via the effective action: 
    \[iW[J] = \int_{\text{conn. tree}}\left[ \prod_{r,x}d\phi^r(x) \right] \exp{ \left[ i\Gamma[\phi] + i \int \phi^r(x)J_r(x) d^4x \right] }\]
\end{itemize}

\paragraph{application on scalar theory}
\begin{itemize}
    \item take scalar action and add position-independent external field $\phi_0(x) = \phi_x$ assumed to be some functional over all space so we get a $\mathscr{V}_4 = \int d^4x$, and $\Gamma[\phi_0] = - \mathscr{V}_4 V(\phi_0)$
    \item where $V(\phi_0)$ is known as the effective potential, if we wish to calculate it to one-loop order, we obtain (16.2.13,14)
    \item the divergence of the effective potential can be absorbed into appropriate constants (16.2.15)
\end{itemize}


\paragraph{energy interpretation}
\begin{itemize}
    \item 
\end{itemize}

