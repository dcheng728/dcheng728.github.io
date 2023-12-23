# Introduction

The Atiyah TQFT assigns complex vector fields to manifolds of a certain dimensions. So inherently, the theory bears a certain degree of topological-invariance, which is Atiayh's initial goal for establishing this theory. 

At first glance, assigning complex vector fields to manifolds may seem like a weird concept, especially to non-physicists. But this is a very practical design. Because often in physics, the object we want to study has configuration space given by some manifold. 

The complex vector space is necessary to define a quantum theory. Simply because R is not sufficient for solving the differential equations in QM, so use C.



## Manifolds
We define a $d$-dimensional manifold, or a $d$-manifold, to be a topological space that locally resembles $\mathbb{R}^d$ or $\mathbb{R}_{\ge 0} \times \mathbb{R}^{d-1}$. By locally resemble, we mean having a neighborhood homeomorphic to. 

- A topological space $M$ is a $d$-**manifold** if for any $x\in M$, there exists an open neighborhood $U$ of $x$ such that it can be mapped homeomorphically to some open subset of $\mathbb{R}^{d}$, or alternatively, $\mathbb{R}_{\ge 0} \times \mathbb{R}^{d-1}$.

The additional relaxation of allowing $U$ to resemble $\mathbb{R}_{\ge 0} \times \mathbb{R}^{d-1}$ is present because we are working with manifolds with boundary. One can easily see that the former condition of locally resembling $\mathbb{R}^d$ is stronger. 

- For a $d$-manifold $M$, we define the ***interior points*** $\text{int} (M)$ of $M$ to be the set of all points in $M$ that locally resembles $\mathbb{R}^n$.

It would then be natural to define the ***boundary*** of $M$ to be $M \setminus \text{int} (M)$, denoted as $\partial M$. 



### examples
- a line segment is a 1-manifold its boundaries are its two endpoints. 
- A circle is a 1-manifold.
- Disjoint union of a line and a circles, or a line and a line, or a circle and a circle is a 1-manifold. 

### lemma
Finite disjoint union of $k$-manifolds is a $k$-manifold. 

One can easily check that all points on a circle are interior, so a circle, as a 1-manifold has the empty set as its boundary. When this happens, we say the manifold is \textbf{closed}. Colloquially, the boundary of a manifold is be known as the ``sharp edges" of the manifold. In low dimensions, it is very convenient to determine the boundary of a manifold by identifying its sharp edges. 



\begin{example}
    The sphere $S^2$ is a closed 2-manifold.
\end{example}


\begin{example}
    A torus is a closed 2-manifold.
\end{example}

\begin{example}
    A pair of pants is closed a 2-manifold. 
\end{example}

Atiyah's TQFT requires the manifold to be ``oriented." However, the precise definition of orientable manifold is not necessary for the rest of this paper, because we mostly deal with manifolds in low dimension. All that a reader needs to know is the orientation of a manifold is a continuous assignment of a binary direction between clockwise and counter-clockwise along the manifold. Whenever necessary, we will specify the orientation of a manifold.

\begin{example}
    A circle is orientable.
\end{example}

By assumption we let circle $S^1$ be clockwise, and we will denote its mirror image which would be counter-clockwise with $\bar{S}^1$. For any orientable manifold $M$, we will denote its mirror image with opposite orientation with $\bar{M}$.

\subsection{Cobordism}

The concept of cobordism arises when considering a manifold of dimension one higher that can be constructed with some manifold as its boundary. 



\begin{definition}
    Given oriented $d$-manifolds $M_1, M_2$, we say that they are \textbf{cobordant} if there exists $(d+1)$-manifold $Y$ such that $\partial Y = M_1 \cup \bar{M_2}$. When such $Y$ exists, we call it the \textbf{cobordism} between $M_1$ and $M_2$.
\end{definition}

\begin{figure}[H]
    \centering
    \includegraphics[width = 0.5 \textwidth]{illustrations/TQFT/cob.png}
    \caption{An example of cobordism between two circles. Note that the orientations of the circles are opposite.}
\end{figure}

Figure 1 displays a cobordism between $S^1$ and $S^1$. When thinking about cobordisms, the notion of orientation is crucial for making the subject well-defined. Because we will be exploring cobordisms between manifolds and the empty set in the next section, as one can check for themselves, losing the notion of orientation will create contradictions all over the place. 

There are two equivalent formalisms for establishing the corbordism between two manifolds $M_1$ and $M_2$. The first approach begins by drawing $M_1$ on the left with the same orientation, and $M_2$ on the right with the opposite orientation. Then any manifold that one can draw which utilizes $M_1$ and $M_2$ as its boundary would be a cobordism between the two. The alternate approach is to draw both $M_1$ and $M_2$ with the same orientation, but on top of each other. Then one considers the cobordism between $M = M_1 \cup M_2$ and the empty set. The two methods have their own advantages dependent on the nature of the manifold being drawn. As one can see, Figure 1 takes the first approach. 

% There are two equivalent formalisms for establishing the cobordism between manifolds, both of them require defining a direction in advance, which is often taken to be from left to right. This means when we say cobordism between $M_1$ and $M_2$, the manifold $M_1$ would be drawn to be on the left and $M_2$ would be on the right. Then, the manifold $M_1$ would be drawn 

% \begin{enumerate}
%     \item 
% \end{enumerate}

\subsection{Tensor Products}

Now we move on to vector spaces, which is key to defining quantum states in quantum field theory. The reason that Atiyah's theory needs to incorporate complex vector spaces is that, in general, quantum field theory is defined over an uncountably-infinite-dimensional complex vector space called the Hilbert space. Linear operators in the Hilbert space tell us, in principle, various things we can know about a physical state, such as spin, energy, momentum, etc. 

\begin{definition}
    Let $K$ be a field and $K^l$, $K^m$ be $l,m$ dimensional vector fields over $K$. For some $u \in K^l$ and $v \in K^m$, we define the tensor product between $u$ and $v$ denoted $u \otimes v$ to be a vector $w$ in the vector field $K^{l \times m}$ with $w_{(m * i) + j + 1} = u_{i+1} * v_{j+1}$ for $i \in \{0,1,...,l-2\}$, $j \in \{0,1,...,m-1\}$.
\end{definition}


\begin{example}
    $$\begin{bmatrix}
a_1 \\
a_2 
\end{bmatrix} \otimes 
 \begin{bmatrix}
b_1 \\
b_2 
\end{bmatrix} =
\begin{bmatrix}
a_1 * b_1 \\
a_1 * b_2\\
a_2 * b_1 \\
a_2 * b_2
\end{bmatrix}$$
\end{example}

\section{Axiomatization}

We begin with Atiyah's axioms for his TQFT. According to Atiyah, a TQFT of dimension $d$ is a function $Z$ which does the two following jobs:

\begin{itemize}
    \item[\textbf{J1}] Assign a complex vector space $Z(\Sigma)$ to each compact, oriented, smooth $d$-manifold $\Sigma$.
    \item[\textbf{J2}] Assign a vector $Z(Y) \in Z(\Sigma)$ for each compact, oriented $(d+1)$-manifold whose boundary is $\Sigma$.
\end{itemize}

The function $Z$ shall satisfy the following  axioms.

\begin{itemize}
    \item[\textbf{A1}] $Z(\Sigma_1 \cup \Sigma_2) \cong Z(\Sigma_1) \otimes  Z(\Sigma_2)$ for disjoint $\Sigma_1, \Sigma_2$
    \item[\textbf{A2}] If $Y_1$ is a cobordism with boundary $\Sigma_1$ and $\Sigma_2$, then $Z(Y_1)$ is a homomorphism from $Z(\Sigma_1)$ to $Z(\Sigma_2)$. If, in addition, $Y_2$ is a cobordism with bounary $\Sigma_2$ and $\Sigma_3$, then $Z(Y_1 \wedge_{\Sigma_2} Y_2) \cong Z(Y_2) \circ Z(Y_1)$ is a homomorphism from $Z(\Sigma_1)$ to $\Sigma_3$. In other words, $Z$ is associative. 
    \item[\textbf{A3}] $Z(\bar{\Sigma})$ is isomorphic to $Z(\Sigma)^*$, the dual vector space of $Z(\Sigma)$.
\end{itemize}


\begin{example}
    For a $d$-manifold $\Sigma$, $Z(\Sigma \times I)$ is the identity homomorphism $Z(\Sigma)$. 
\end{example}

\begin{proof}
    The product $\Sigma \times I$ is a $(d+1)$-manifold that is a cobordism with disjoint boundaries $\Sigma$ and $\Sigma$ at 0 and 1 in its $(d+1)$st dimension, so by \textbf{A2}, $Z(\Sigma \times I)$ is a homomorphism from $Z(\Sigma)$ to $Z(\Sigma)$.
\end{proof}

\begin{remark}
    The $(d+1)$-manifold $\Sigma \times I$ is just a cylinder with $\Sigma$ on each side.
\end{remark}

\begin{proposition}
    In any dimension, $Z(\emptyset)  = \mathbb{C}$ by convention.
\end{proposition}

\newcommand{\AO}{\textbf{A1}}

% The above example states that $Z$ maps the empty set to simply a complex number. Since no matter how you transform the empty set, it is still the empty set, $Z(\emptyset)$ have to be a complex constant in each dimension! This is a very simple corollary of Atiyah's axioms but has important implications, because the boundary of any closed manifold of any dimension is the empty set. This is the first topological invariance of Atiyah's TQFT. 

\section{\texorpdfstring{d = 1}{}}

In the case of $d = 1$, the $(d+1)$-manifold $Y$ is a 2-manifold (i.e. surface) with $1$-manifold $\Sigma$ as its boundary. The simplest 1-manifold object are the circles, denoted $S^1$. By \textbf{J1}, we know that $Z(S^1)$ gives some complex vector space which we will denote as $A$:

$$Z(S^1) = A.$$

Then the disjoint union of $n$ circles will produce a tensor product of $A$:

$$Z(\bigcup_{i=1}^n S^1_i) =A \otimes A \otimes ... A = \bigotimes_{i=1}^n A = A^{\otimes n}.$$

\paragraph{Tube} A Tube $Y$ is simply a cobordism between two circles, so 

\begin{align*}
    Z(Y) \cong m &: Z(S^1) \rightarrow Z(S^1)\\
    &: A \rightarrow A
\end{align*}

is a homomorphism. But alternatively, using the second convention for cobordism, we can regard a tube as a cobordism between two circles of same orientation, and the empty set, we then obtain

\begin{align*}
    Z(Y) \cong m'&: Z(S^1 \cup S^1) \rightarrow Z(\emptyset)\\
    &: A \otimes A \rightarrow \mathbb{C}
\end{align*}

This implies that there exists an isomorphism between $m: A \rightarrow A$ and $m': A \otimes A \rightarrow \mathbb{C}$, which we will denote as some $g: m \rightarrow m'$.

\paragraph{Pants}
 Suppose we have a cobordism $B$ whose boundaries are 2 circles on the left, and 1 circle on the right, i.e. $B$ is a pair of pants. We will denote its left boundary with $\Sigma_1 = S^1 \cup S^1$ and its right boundary with $\Sigma_2 = S^1$. Then the boundary of $B$ is the disjoint union 

$$\partial B = \Sigma = \Sigma_1 \cup \Sigma_2.$$ 

\newcommand{\AT}{\textbf{A2}}

By \AT, $Z(B) \in Z(\Sigma)$ is a homomorphism between $Z(\Sigma_1)$ and $Z(\Sigma_2)$:

\begin{align*}
    Z(B) &: Z(\Sigma_1) \rightarrow Z(\Sigma_2) \\
    &:Z(S^1 \cup S^1) \rightarrow Z(S^1) \\
    &: A \otimes A \rightarrow A
\end{align*}

is a homomorphism. 

\paragraph{Disc}

We define a disc $D$ to be a surface whose boundary is a circle. This means that a Disc is also a 2-manifold. 

Observe that $D$ has the boundary specified by $S^1$ which is also equal to $S^1 \cup \bar{\emptyset}$, so $D$ is a cobordism between $S^1$ and $\emptyset$, thus

$$Z(D): A \rightarrow \mathbb{C}$$ is a homomorphism. 


\paragraph{Pants + Disc =  Tube}
We can regard a tube as a pair of pants wedged with a disc. Imagine a pair of pants with two boundaries on the left and one on the right. We can take a disc, match the boundary of the disc with the boundary of the pair of pants on the right. Because the interior of a disc is filled, this will allow us to patch up our pair of pants and now we only have two holes on the left. If we then straighten the patched up manifold we obtain a tube. 

Applying \AT, we know for the tube $Y$, pants $B$, and disc $D$, we have

$$Z(Y) \cong Z(B) \circ Z(D).$$

Since $Z(B)$ and $Z(D)$ are homomorphisms from $A \otimes A$ to $A$ and $A$ to $\mathbb{C}$, respectively. This tells us $Z(Y)$ is a homomorphism from $A \otimes A$ to $\mathbb{C}$. Applying the isomorphism $g^{-1}$ that we found in the Tube section, we obtain a homomorphism between $A$ and $A$, which is what we expect for a tube. 

\paragraph{\texorpdfstring{$\overline{\textbf{Disc}}$}{} + Disc = Sphere} A sphere shall be regarded as a two discs with opposite orientations wedged together. Again, by applying \AT, we obtain

\begin{align*}
    Z(S^2) \cong Z(\bar{D}) \circ Z(D)
\end{align*}

We know that $Z(\bar{D})$ is a homomorphism from $\mathbb{C}$ to $A$ and $Z(D)$ is a homomorphism from $A$ to $\mathbb{C}$. Thus $Z(S^2)$ must define a homomorphism between $\mathbb{C}$ and $\mathbb{C}$. 


But equivalently, we could have also defined $\Sigma_1$ to be $S^1$ and $\Sigma_2$ to be $S^1 \cup S^1$, we could have flipped the pair of pants. In that case we would have obtained

$$Z(B) = m : A \rightarrow A \otimes A.$$

Suppose $A$ is a vector space with dimension $a$, then $A \otimes A$ would have dimension $a^2$. The only choice to give $A$ and $A \otimes A$ the same dimension is making $A$ one-dimensional, i.e. $A \cong \mathbb{C}$. 

\paragraph{Disc} Now consider the $(d+1)$-manifold to be a disc $D$, which is simply a circle with its interior filled. Its boundary $\Sigma$ is a circle $S^1$. Topologically, the disc is a cobordism between the empty set and the circle. So by \AT, $Z(D)$ is a homomorphism between $Z(\emptyset)$ and $Z(S^1)$, which we know are $c \in \mathbb{C}$ and $A$, respectively:

$$Z(D): A \rightarrow \mathbb{C}$$

Similarily, changing the orientation of $D$ will give us the homomorphism

$$Z(\bar{D}): \mathbb{C} \rightarrow A.$$


\paragraph{Sphere} The 2 sphere $S^2$ is a a closed manifold, which means we expect $Z(S^2) $


\section{References}

(in order of relevance)

\begin{itemize}
    \item ``\textit{Geometry and Physics of Knots}," book by Michael Atiyah published by Cambridge University Press, 1993.
    \item ``\textit{The Classification of Extended Topological Field Theories}," talk by Jacob Lurie at the Institute for Advanced Studies, 2022.
    \item ``\textit{Oriented Cobordism: Calculation and Application}," lecture notes by Alexander Kupers, 2017.
\end{itemize}