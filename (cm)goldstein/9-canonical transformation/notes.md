# canonical trans

Apply cano. tran. defined by p->P, q->Q, H->K. Then Hamilton's principle takes form

$$\delta \int [P_i \dot{Q}_i - K(Q,P,t)]dt = 0$$

$$\delta \int [p_i \dot{q}_i - H(q,p,t)]dt = 0$$

The general solution takes the form

$$\lambda (p_i \dot{q}_i - H) = P_i \dot{Q}_i - K + \frac{d F}{dt}$$

for F function of two of p,q,P,Q, called generating function.

If $\lambda = 1$, the transform is called canonical transformation. If $\lambda \neq$, the transformation is called extended canonical transformation.

- any extended canonical transformation can be made up by a canonical one + scaled transformation. 

Table 9.1 gi es trlations between the canonical trans and generating functions. 

# symplectic relation

## reminder
Let $Q_i = Q_i(q,p)$, then 

$$\dot{Q}_i = \frac{\partial Q_i}{\partial q_j} \dot{q}_j + \frac{\partial Q_i}{\partial p_j} \dot{p}_j$$

when combined with hami eqm, it is

$$\dot{Q}_i = \frac{\partial Q_i}{\partial q_j} \frac{\partial H}{\partial p_j} - \frac{\partial Q_i}{\partial p_j} \frac{\partial H}{\partial q_j}$$

This is written compactly in matrix form:

$$\dot{\vec{\eta}} = \vec{J} \frac{\partial H}{\partial \vec{\eta}}$$

where $\vec{J}$ is the 2nx2n matrix of 

$$\left[\begin{array}{rr}
0 & I \\
-I & 0
\end{array}\right]$$

and $\vec{\eta} = (q_1, q_2, ..., p_1, ..., p_n)$

As an illustration

$$
\left[\begin{array}{rr}
\dot{q}_1 \\
\dot{q}_2 \\
\dot{p}_1 \\
\dot{p}_2
\end{array}\right]

=

\left[\begin{array}{rr}
 0 &  0 & 1 & 0 \\
 0 &  0 & 0 & 1 \\
-1 &  0 & 0 & 0 \\
 0 & -1 & 0 & 0 
\end{array}\right]

\left[\begin{array}{rr}
\partial_{q_1} H \\
\partial_{q_2} H \\
\partial_{p_1} H \\
\partial_{p_2} H
\end{array}\right]
$$

## symplectic structure

Now take restricted transformation $\vec{\zeta} = \vec{\zeta}(\vec{\eta})$. Then $\dot{\vec{eta}} = \vec{M} \dot{\vec{\eta}}$ where $\vec{M}$ is Jacobian. Together with Hami eqm, we have

$$\dot{\vec{\eta}} = \vec{M} \vec{J} \frac{\partial{H}}{{\partial \vec{\eta}}}$$

But $\frac{\partial H}{\partial \vec{\eta}} = \tilde{M} \frac{\partial H}{\partial \vec{\zeta}}$. The Hami eqm for $\zeta$ is

$$\dot{\zeta} = M J \tilde{M} \frac{\partial H}{\partial \zeta}$$

as oppose to $$\dot{\eta} = J \frac{\partial H}{\partial \eta}$$

But we also must have 

$$\dot{\zeta} = J \frac{\partial H}{\partial \zeta}$$

This implies $$MJ\tilde{M} = J$$

note: for extedned canonical trans, it is $MJ\tilde{M} = J$

This is called **symplectic condition**, $M$ is called **symplectic** matrix. 

# Poisson Bracket

define 

$$[u,v]_{q,p} = \frac{\partial u}{\partial q_i} \frac{\partial v}{\partial p_i} - \frac{\partial u}{\partial p_i}\frac{\partial v}{\partial q_i}$$

similarily, the definition can be written as

$$[u,v]_{\eta} = \left( \frac{\partial u}{\partial \vec{\eta}} \right)^T J \left( \frac{\partial v}{\partial \vec{\eta}} \right)$$

- $[q_j, q_k]_{q,p} = 0 = [p_j, p_k]_{q,p}$
- $[q_j, p_k]_{q,p} = \delta_{jk} = - [p_j, q_k]_{q,p}$

The above two relations are written neatly as $[\eta, \eta]_{\eta} = J$

- $[\zeta, \zeta]_\eta = M^T J M$
- This implies if $\eta$ -> $\zeta$ canonical, then $[\zeta, \zeta]_\eta = J$

The relation $[\zeta, \zeta]_\eta = J = [\zeta, \zeta]_\zeta$ is ***called fundamental poisson bracket. It is invariant under cano. trans.*** 

## some poisson bracket algebra

- [u,v] = 0
- [u,v] = - [v,u]
- (linearity) [a + bv, w] = a [u,w] + b[v,w]
- [uv,w] = [u,w]v + u[v,w]
- (nontrivial, Jacobi's identity) [u,[v,w]] + [v,[w,u]] + [w,[u,v]] = 0

## some other cano invariants

- lagrange bracket $\{u,v\}$. It also satisfies $$\{u,u\}[u,u] = - I$$
- the magnitude of volume element in phase space is canonically invariant