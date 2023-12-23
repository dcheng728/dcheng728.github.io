# minimum action principle
- **hamilton's principle**: 
$$I = \int_{t_1}^{t_2}Ldt = \int_{t_1}^{t_2}[T-V]dt$$
has vanishing 1st order differential with respect to all nearby paths for $L$ defined as a path
- holonomic constraint implies **equivalence of hamilton's principle and lagrange's equation**. This gives an alternative derivation of Lagr beside from d'alembert's principle of vanishing work from virtual displacements
- minimum action principle can be applied to solve
	- shortest path between 2 pts in space
	- minimum surface of revolution
	- brachistochrone
# for nonholonomic constraints
- In deriving lagr, the constraints as holonomic ones were only used in the last step to move to generalized coordinates, this then gives independent equations of motion. Nonholonomic constraints clearly ruins this.
- **semiholonomic**: $f(q_1,..., q_n, \dot{q}_1, ..., \dot{q}_n) = 0$
- l**agrange multipliers** can treat nonholonomic constraints


- in almost every field of physics, the variational principle can be used to express equations of motion (EM, thermo)
- impulse: $\int{\Delta t} F dt$. If impulse is finite then the force is called impulsive. 
- semi-holonomic constraints are typically given in the form of $$\sum_i a_{ik} dq_k + a_{it}dt = 0$$
- variational principle provides a clean explanation to the arbitrariness of lagr within an addition of a total time derivative: the action is integrated over time!
- 