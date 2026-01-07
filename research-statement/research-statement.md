---
layout: default
title: Research Statement
permalink: /research-statement/
---
# Research Statement

My research interests lie at the intersection of AI and fundamental physics, viewed from two complementary directions: using AI as a tool for physics discovery, and using physical principles to better understand and design AI systems.

**AI for physics**

In particle physics and cosmology, a central challenge is the identification of subtle physical signals, whether signatures of Standard Model processes or new physics, from data filled with background processes, noise, and detector effects.
Modern machine learning methods, with their ability to uncover the latent statistical structure in large, high-dimensional datasets, provide a promising new approach.
I am particularly interested in methods that balance performance with physical insight, for example, methods that learn or respect symmetries, identify optimal summary statistics, or enable likelihood-free inference while remaining firmly grounded in physical models.

**Physics for AI**

Many foundational ideas in machine learning are rooted in physics, from Hopfield networks to Boltzmann machines and modern energy-based models.
Physicists bring a distinctive perspective to questions of ML interpretability, drawing on symmetry principles, conservation laws, thermodynamic reasoning, and scale analysis to place principled constraints on model behavior, reduce effective complexity, and clarify what and how models have learned.
Concrete directions I hope to explore include defining entropy-like quantities during training, understanding learning dynamics through effective equations of motion or state, and using physical constraints to guide model design and reliability.
<!-- 
---

# Research Statement (1000 words)

My research interests lie at the intersection of AI and fundamental physics, viewed from two complementary directions: using AI as a tool for physics discovery, and using physical principles to better understand and design AI systems.

**AI for physics**

n particle physics and cosmology, a central challenge is to identify subtle physical signals, whether Standard Model processes or signatures of new physics, from data dominated by backgrounds, noise, and detector effects. Classical analyses often reduce events into a small number of handcrafted observables and then perform likelihood-based inference. This approach is principled, but can be limited when the relevant information is distributed across many correlated features, as is typical for collider events, cosmic surveys, or multi-channel astrophysical observations. Modern machine-learning methods, with their ability to uncover latent statistical structure in large, high-dimensional datasets, offer a promising route to more powerful inference.

A direction I am particularly interested in is simulation-based inference, where one leverages forward simulators of the physical model and detector rather than requiring an explicit analytic likelihood. This includes likelihood-free approaches that learn either informative summary statistics, a likelihood ratio, or a posterior approximation directly from simulations. Concretely, I am interested in how to design such pipelines so that they remain anchored to physical models rather than becoming purely discriminative pattern recognizers. Practically, this means (i) making the mapping from theory parameters to data explicit through the simulator, (ii) preserving interpretability by learning low-dimensional representations that can be diagnosed and stress-tested, and (iii) quantifying uncertainty and sensitivity to nuisance parameters in a way that matches the standards of high-energy physics and cosmology.

Within this space, I see several concrete research directions.

1) Learning physically meaningful summaries and test statistics, with rigor

2) Encoding inductive biases through symmetries and equivariances.
Many problems in fundamental physics come with strong known symmetries, such as permutation symmetry of sets of particles, rotational symmetries, or approximate Lorentz structure at the level of reconstructed objects. Leveraging these symmetries can improve sample efficiency and robustness, and can make learned representations easier to interpret. I am interested in architectures and training objectives that respect symmetries by design, and in diagnosing what happens when symmetry assumptions are only approximate due to detector effects or selection biases. In collider contexts, this naturally connects to set-based models for jets and events; in cosmology, it connects to translation and rotation equivariance in maps and fields.

**Physics for AI**

Historically, some of the most influential ideas in AI came from physics: the Hopfield network is governed by the Hamiltonian of the Ising model [1], and the Boltzmann machine, as developed by Hinton, more explicitly draws from the principles of statistical mechanics.

The desire to understand "intelligence," just like the desire to understand the universe at large scale, or the desire to understand the fundamental constituents of matter, is the desire of a physicist. 

Despite rapid progress in modern ML, the biggest challenge in both its theory and application remains in understanding how it learns and generalizes. 

1) Training dynamics as effective physics.
Stochastic gradient descent can be viewed as a noisy dynamical system. I am interested in “effective theory” descriptions of learning dynamics: what are the relevant degrees of freedom, what can be integrated out, and what macroscopic quantities track progress and generalization? This suggests studying the geometry of the loss landscape (Hessian spectra, flat vs sharp directions), and developing coarse-grained descriptors that are stable across architectures and datasets.

2) Thermodynamic and information-theoretic quantities during learning.
A natural question is whether one can define entropy-like quantities that evolve during training, capturing compression, representation complexity, or uncertainty. The autoencoder framework 

3) Symmetry and conservation principles as design constraints.
Physics gains interpretability by identifying invariants and conserved quantities. I am interested in whether analogous invariants exist in learning dynamics, such as quantities approximately preserved by certain optimizers, normalizations, or architectural symmetries. Even when exact conservation is unrealistic, approximate invariances can be valuable as regularizers and diagnostics. This connects directly to reliable ML: if a model’s behavior is constrained by principled structure, it is less likely to exploit spurious correlations.

4) Scale analysis, scaling laws, and renormalization-style viewpoints.
Modern ML exhibits striking empirical scaling regularities. Physicists naturally ask which parameters matter at which scales, and how behavior changes under coarse-graining. I am interested in whether renormalization-style reasoning can help formalize when increased capacity helps, when it harms, and how to characterize transitions such as double descent or sudden changes in representation. Even partial success here would provide a more predictive theory of model behavior.

5) Reliability, uncertainty, and out-of-distribution behavior as first-class objectives.
Many ML failures in scientific settings come from distribution shift or unmodelled systematics. I am interested in principled reliability criteria that can be linked to physical notions of stability, sensitivity, and control. This includes calibration, uncertainty quantification, and stress-testing procedures that can be justified theoretically and implemented practically. In my view, physics-informed diagnostics should become part of the standard ML pipeline, not an afterthought.

generalize, how training dynamics select solutions, and how to make learned representations reliable under perturbations. I view this as a physics problem: training is a dynamical process in a high-dimensional space, subject to constraints and noise, exhibiting emergent behavior and sometimes sharp transitions.


Despite the rapid developments in AI, the biggest challenge in both its theory and application remains in understanding how it works. I see this as a physics problem: the same tools we use to model physical systems can help guide AI model design and provide a framework for understanding how they learn.

Physicists bring a distinctive perspective to questions of ML interpretability, drawing on symmetry principles, conservation laws, thermodynamic reasoning, and scale analysis to place principled constraints on model behavior, reduce effective complexity, and clarify what and how models have learned.
Concrete directions I hope to explore include defining entropy-like quantities during training, understanding learning dynamics through effective equations of motion or state, and using physical constraints to guide model design and reliability.

- conserved quantities, equations of motion/state
- entropy, thermodynamics

**Outlook**

Taken together, these two directions reflect my broader research vision: to build a productive dialogue between AI and physics, where advances in one inform progress in the other. By using AI to extend the reach of physics inference while applying physical reasoning to clarify the behavior of learning systems, I aim to contribute to a more principled and interpretable integration of machine learning into fundamental science. -->


<!-- ---

I am interested in problems at the intersection of AI and physics, from two perspectives. 
- AI for physics: How can we leverage AI to understand physics and discover new physics?
- Physics for AI: How can a physicist's perspective help us make machine learning (ML) more interpretable and reliable?

## AI for physics

In particle physics and cosmology, the challenge is to identify signatures of specific Standard Model processes, or evidence of new physics, hidden amid noise, detector biases, and background events. Modern machine learning, with their unique ability to identify underlying statistical patterns in large amounts of high-dimensional data, is a new promising approach. Examples of this includes optimizing for summary statistics 

Machine learning 

## Physics for AI

Historically, some of the most influential ideas in AI came from physics: the Hopfield network is governed by the Hamiltonian of the Ising model, and the Boltzmann machine, as developed by Hinton, more explicitly draws from the principles of statistical mechanics.

The desire to understand "intelligence," just like the desire to understand the universe at large scale, or the desire to understand the fundamental constituents of matter, may be the desire of a physicist. Despite the rapid developments in AI, the biggest challenge in both its theory and application remains in understanding how it works. I see this as a physics problem: the same tools we use to model physical systems can help guide AI model design and provide a framework for understanding how they learn.

Physicists have unique perspectives and tools to understand complex systems and their time-evolutions. Symmetry-driven approaches and orders of magnitude thinking allow efficient reduction of the parameter space, while thermodynamic laws, conserved quantities, and equations of motion offer handles on the time-evolution, hence the learning procedures, of the system. Some examples of directions for this line of work: understanding how to define entropy and other thermodynamic quantities at various stages of a neural network training, and how they evolve.

The 


To address this challenge, I would like to treat neural network training as the time-evolution of a statistical system. This viewpoint invites the use of familiar tools from statistical physics, such as order parameters, correlation functions, and entropy-based perspectives, to characterise how learning progresses and how macroscopic behaviour emerges.

An alternative direction that excites me is the neural network field theory correspondence. In the infinite-width limit, ensembles of fully connected networks are known to correspond to Gaussian processes, which are equivalent to free field theories. However, how this correspondence extends to realistic network sizes, architectures, and training dynamics remains unclear.

More broadly, I hope to use ideas from theoretical physics to build a principled framework for understanding modern AI at the scales at which it is used today. -->


<!--
## AI for physics

### Particle Physics
In particle physics and cosmology, the challenge is to identify signatures of a specific Standard Model process, or evidence of new physics, hidden amid noise, detector biases, and background events. Raw detector data, carry little meaning; one wishes to extract the physically meaningful information, using ML.

Machine learning offers a way to bridge this gap by learning representations that are robust to detector effects and other nuisance variations, while respecting the symmetries and constraints that define the underlying physics. I am particularly interested in methods that provide calibrated uncertainties and clear statistical interpretations, so that their outputs can be trusted in physics analyses. I am also drawn to approaches that prioritise interpretability alongside performance, and that incorporate physical structure to help reveal what the network has learned.


### Theoretical Physics
This direction is less clear.


## Physics for AI

Historically, some of the most influential ideas in AI came from physics: the Hopfield network is governed by the Hamiltonian of the Ising model [1], and the Boltzmann machine, as developed by Hinton, more explicitly draws from the principles of statistical mechanics.

The desire to understand "intelligence," just like the desire to understand the universe at large scale, or the desire to understand the fundamental constituents of matter, is the desire of a physicist. Despite the rapid developments in AI, the biggest challenge in both its theory and application remains in understanding how it works. I see this as a physics problem: the same tools we use to model physical systems can help guide AI model design and provide a framework for understanding how they learn.

To address this challenge, I would like to treat neural network training as the time-evolution of a statistical system. This viewpoint invites the use of familiar tools from statistical physics, such as order parameters, correlation functions, and entropy-based perspectives, to characterise how learning progresses and how macroscopic behaviour emerges.

An alternative direction that excites me is the neural network field theory correspondence. In the infinite-width limit, ensembles of fully connected networks are known to correspond to Gaussian processes, which are equivalent to free field theories. However, how this correspondence extends to realistic network sizes, architectures, and training dynamics remains unclear.

More broadly, I hope to use ideas from theoretical physics to build a principled framework for understanding modern AI at the scales at which it is used today.

## References

[1] J. Hopfield, "Neural networks and physical systems with emergent collective computational abilities", [PNAS](https://pmc.ncbi.nlm.nih.gov/articles/PMC346238/).
-->
