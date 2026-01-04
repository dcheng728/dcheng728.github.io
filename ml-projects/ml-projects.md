---
layout: default
title: AI/ML Projects
permalink: /ml-projects/
---
# AI/ML Projects

## Point Cloud Representation Learning (2023)

Point clouds arise in settings such as LiDAR for self-driving cars, yet raw coordinates carry little meaning: they shift under translation and are easily distorted by noise and sensor biases.
Our goal was to develop a representation that reflects the underlying geometry rather than the coordinates themselves.

![Example point clouds of 3D objects](../media/point%20cloud%20example.png)

*Example point clouds of 3D objects.*

We trained a graph neural network to map each point cloud to a feature vector, while an adversarial network applied perturbations to the input aimed at mimicking various symmetries and noise that the main network should be insensitive to.
The adversarial network sought to maximize deviations in the learned features, while the main network attempted to remain invariant.
Training the two networks jointly led to stable and promising geometric representations.

![Example of how the Adversarial Neural Network applies perturbations](../media/point%20cloud%20perturbation.png)

*Example of how the Adversarial Neural Network applies perturbations.*

[Github Repo](https://github.com/dcheng728/ML-HKS)

---

## Machine Learning in Auction Design (2022)

In summer 2022, I participated in an REU program at the University of Maryland.
We were interested in building sealed-bid online auctions that people could actually trust, even when the auctioneer might have reasons to bend the rules.
We realized that you can’t get truthfulness, high revenue, and credibility all at once in a single-round auction, so we looked at how repeated auctions could give bidders a way to check whether the auctioneer was behaving honestly.
We used machine learning to learn good auction rules.
To keep the auctioneer honest, we added an audit step.
Putting everything together, we ended up with a system that performs well and stays trustworthy without adding much overhead.

![REU group picture](../media/group%20picture.png)

*REU Group Picture.*

![Photo of those of us with Math/CS shirts](../media/reu%20picture.png)

*Photo of those of us with Math/CS shirts.*

---

## Machine Learning in Video Game (2020)

I once played a video game called League of Legnds.
The game has a minimap, which contains key information, e.g. where the players' allies and enemies are located.
But it is very easy to overlook the minimap.
I wanted to create an AI that would summarize the key information on the minimap.

![In-game interface of League of Legends](../media/lol%20example.jpg)

*In-game interface of League of Legends.*

The program extracted champion icons directly from minimap frames using image-processing techniques, then a neural network is applied to classify each icon.

![The pipeline for avatar recognition](../media/classification%20pipeline.png)

*The pipeline for avatar recognition.*

![Demo of the pipeline running live](../media/leagueX%20demo.gif)

*Demo of the pipeline running live.*

I received an award for this project at graduation, and my high school began offering computer science classes in the following year.

[Github Repo](https://github.com/dcheng728/League-X);
Blog Posts (in Chinese):
[part I](https://blog.csdn.net/weixin_42488182/article/details/95088716?spm=1001.2014.3001.5501),
[part II](https://blog.csdn.net/weixin_42488182/article/details/105161123?spm=1001.2014.3001.5501).

---

## Rubik's Cube Scanner + Solver (2018)

I used OpenCV, various computer vision algorithms and filters to create a program that could recognize the faces of a Rubik's Cube.

![Demo of my rubik's cube scanner and solver](../media/rubik%20demo.gif)

*Demo of my rubik's cube scanner + solver.*

My program is actively scanning for rubik's cubes in the webcam image, and when it recognizes one, it will read the colors and automatically enter them into the solver.
The solver then finds the solution and displays an animation of how to solve the cube.

[Github Repo](https://github.com/dcheng728/Rubik-s-Cube-Scanner-Solver),
[Blog Post (in Chinese)](https://blog.csdn.net/weixin_42488182/article/details/103451877?spm=1001.2014.3001.5501)

