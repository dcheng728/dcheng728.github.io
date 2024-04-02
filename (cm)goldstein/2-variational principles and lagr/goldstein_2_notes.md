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

# lagr multiplier

A systematic approach for solving (sort of) semiholonomic constraints

- write the constraints in form $f_\alpha(q_i, ..., \dot{q}_i, ...) = 0$
- Then define lagrange multipliers, which are functions of $q_i,\dot{q}_i, t$: 
$$\lambda_\alpha = \lambda_\alpha(q_i, \dot{q}_i, t)$$
- It must be true that $\lambda_\alpha f_\alpha = 0$, summation implied. From our earlier derivation we found that hamilton's principle gives 
$$\delta \int_{t_0}^{t_1} L(q_i,\dot{q}_i,t) dt = 0$$

which implies

$$\delta \int_{t_0}^{t_1} \left[ L(q_i,\dot{q}_i,t) + \lambda_\alpha f_\alpha \right] dt = 0$$

Then apply the lagr eqm 

$$\frac{d}{dt} \frac{\partial [ L+ \lambda_\alpha f_\alpha ] }{\partial \dot{q}_i} 
- \frac{\partial [ L + \lambda_\alpha f_\alpha ]}{\partial q_i} = 0$$

to obtain the desired eqm. **KEEP IN MIND THE TOTAL TIME DERIVATIVE, PRODUCT RULE NEED TO BE USED**, because $\lambda$ is time dependent. 