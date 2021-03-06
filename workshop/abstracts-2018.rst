Abstracts
=========


.. _millman:

Graphs and complex networks across domains
------------------------------------------

| **K. Jarrod Millman**

Graphs arise in many fields.
Progress in understanding graphs and developing new graph algorithms in a
number of diverse fields is hindered by the fact that researchers who use them
typically don’t have the opportunity to communicate with others who work on
similar problems in different domains.
In this talk, I will
(a) briefly define what we mean by a graph or complex network  and
(b) outline the purpose and goals for this workshop.

.. _ponisio:

Understanding the ecology and evolution of communities through networks, part I
-------------------------------------------------------------------------------

| **Lauren Ponisio**

Prior to the use of networks to model community-level interactions between
species, ecology and evolution often focused on pair-wise interactions, which
vastly limited the scope of inference. Network theory has enabled ecologists to
uncover common topologies across different types of interactions and overturn
misconceptions about the ubiquity of specialization in interactions.  In
addition, models of network stability has enabled us to make predictions about
the robustness of communities to species loss and perturbations. The next step
to further our understanding of the dynamics of ecological communities include
methods to 1) compare networks beyond collapsing their topology into
quantitative metrics, 2) combine different types of networks (i.e, pollination,
seed dispersal, predation), 3) incorporate metadata into interaction strength
and node roles.  In addition, ecological data still relies on tedious data
collection by humans---innovations in metabarcoding and image processing will
also propel our understanding of ecological interactions forward.


.. _gaiarsa:

Understanding the ecology and evolution of communities through networks, part II
--------------------------------------------------------------------------------

| **Marília Palumbo Gaiarsa**

Prior to the use of networks to model community-level interactions between
species, ecology and evolution often focused on pair-wise interactions, which
vastly limited the scope of inference. Network theory has enabled ecologists to
uncover common topologies across different types of interactions and overturn
misconceptions about the ubiquity of specialization in interactions.  In
addition, models of network stability has enabled us to make predictions about
the robustness of communities to species loss and perturbations. The next step
to further our understanding of the dynamics of ecological communities include
methods to 1) compare networks beyond collapsing their topology into
quantitative metrics, 2) combine different types of networks (i.e, pollination,
seed dispersal, predation), 3) incorporate metadata into interaction strength
and node roles.  In addition, ecological data still relies on tedious data
collection by humans---innovations in metabarcoding and image processing will
also propel our understanding of ecological interactions forward.


.. _ryder:

A history of spectral graph theory and its applications, part I
---------------------------------------------------------------

| **Nick Ryder**

Spectral graph theory gives an expression of the combinatorial properties of a
graph using the eigenvalues and eigenvectors of matrices associated with the
graph. These ideas were first introduced in the late 80s in order to prove
Cheeger's inequality for finding a sparse cut. The utility of spectral graph
theory eventually stretched to Laplacian systems for solving linear equations.
Implementing graph sparsification gives us the ability to do this quickly. In
this talk we will describe the introduction of the Laplacian matrix and its use
in these areas.

.. _schild:

A history of spectral graph theory and its applications, part II
----------------------------------------------------------------

| **Aaron Schild**

Spectral graph theory started in the 80s, when Cheeger's inequality was used as
a means for constructing sparse and balanced cuts in a graph. In the 2000s, our
field moved on from studying specific eigenvalues to studying the whole
spectrum of the Laplacian matrix with fast Laplacian solvers. To obtain fast
Laplacian solvers, we needed to sparsify graphs, for which we exploited
concentration phenomena of random matrices. In the 2010s, improvements to these
tools led to improvements on a wide variety of problems, like maximum flow,
travelling salesman (both symmetric and asymmetric), and random spanning tree
generation. In this talk, we briefly survey this chain of events and suggest
some future directions.


.. _hagberg:

Exploring network structure, dynamics, and function using NetworkX
------------------------------------------------------------------

| **Aric Hagberg**

NetworkX is a software tool for network science.  I'll tell the previously
untold story of how the software project started at Los Alamos and describe the
original design goals.   The software scope was driven by research applications
such as disease spread, cybersecurity, and measuring scholarly impact.  I'll
describe these applications and the algorithms and analysis that were developed
to support them.


.. _buluc:

Graph abstractions in computational genomics
--------------------------------------------

| **Aydın Buluç**

Relationships among entities in genomics, such as proteins, DNA sequences, or
genetics markers, are often represented as graphs. Graph abstraction helped
solve many important computational genomics problems from building linkage maps
to genome assembly. In this talk, I will give a short overview on the
characteristics of the graphs that arise in key computational genomics tasks as
well as the fundamental algorithmic questions that are addressed using those
graphs.


.. _arnemann:

Challenges for graph theory in human neuroscience
-------------------------------------------------

| **Katelyn Arnemann**

Graph theory has been applied widely to studies of the human brain, advancing
understanding of cognition and neurological diseases. However, the application
of graph theory to human neuroscience faces many challenges. We will briefly
overview examples of the motivation for and insights enabled by modeling the
brain as a graph. We will then explore challenges for graph theory in human
neuroscience, including challenges with defining the elements of the graphs,
comparing graphs, and calculating and computing informative graph properties.
Examples will be drawn from my work applying graph theory to neuroimaging (MRI
and PET) to study human aging and Alzheimer's disease.


.. _fountoulakis:

Variational Perspective on Local Graph Clustering
-------------------------------------------------

| **Kimon Fountoulakis**

Local spectral methods such as the Approximate Personalized PageRank (APPR)
algorithm have proven to be a powerful tool for the analysis of large data
graphs.  They are defined operationally, and while they come with strong
theory, there is no a priori notion of objective function/optimality condition
that characterizes the steps taken by them.  Here, we derive a novel
variational formulation which makes explicit the actual optimization problem
solved by the APPR algorithm.  In doing so, we draw connections between APPR
and a popular iterative shrinkage-thresholding algorithm (ISTA).  This
viewpoint between APPR and ISTA builds a bridge across two seemingly disjoint
fields of graph processing and numerical optimization, and it allows one to
leverage well-studied, numerically robust, and efficient optimization
algorithms for processing today's large graphs.


.. _scott:

Sequence Assembly Graphs and their Construction
-----------------------------------------------

| **Camille Scott**

The advent of shotgun sequencing of DNA and RNA created the need for more
efficient methods of simplifying massive and redundant string data. Assembly
graphs have become a core abstraction for detecting overlaps between sequenced
fragments, interrogating complete sequencing experiments from one or many
individuals or even species, and succinctly encoding this information in a
principled way. In this talk, I will cover some of the current approaches for
constructing and using assembly graphs, and discuss efforts to move assembly
graph construction into a streaming paradigm.


.. _kyng:

How to Solve Problems on Graphs Using Linear Equations, and How to Solve Linear Equations Using Graphs
------------------------------------------------------------------------------------------------------

| **Rasmus Kyng**

Graphs give us a simple model of a network. Based on this model, we can ask
many interesting questions. For example, we can analyze social networks using
clustering and regression. In transportation networks, we want to understand
and plan flows of traffic, goods, or data. Answering our questions often boils
down to solving an optimization problem on a graph.  Second order methods are a
powerful tool in optimization, but they require solving linear equations, which
can be prohibitively expensive. But when the optimization problem comes from a
graph, this adds structure to the linear equations. We can leverage this
structure to solve the equations quickly, making second order methods
tractable. This insight has been one of the drivers of a major line of research
in graph algorithms, known as the Laplacian Paradigm.  In this talk, we will
see how graph-structured optimization problems give rise to nice linear
equations. We will also see how thinking about these linear equations in terms
of graphs will let us develop very efficient algorithms for solving them.
Finally, we will explore ideas that have recently played a role in making
solvers for these linear equations more practical. 


.. _schmidt:

Linear Regression with Graph Constraints
----------------------------------------

| **Ludwig Schmidt**

Linear regression is one of the core tools in data analysis. Over the past
decade, we have seen significant progress by incorporating prior knowledge such
as sparsity, low rank, or group structures that allow us to achieve higher
accuracy and more interpretable solutions. However, the resulting estimators
also become more challenging algorithmic problems which can be an obstacle to
adoption in practice. In this talk, I will give an overview of linear
regression with graph constraints that arise in settings such as biological
network analysis. On the statistical side, we will see that graph constraints
can offer significantly smaller sample complexity. On the computational side, I
will present an algorithm that incorporates graph structure into linear
regression with little overhead. The algorithm runs in nearly-linear time,
i.e., fast enough so that it is applicable to large graphs.
