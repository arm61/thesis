# Corrections responses

1. Clarify relation between the form factor P(q) and the intensity I(q) (maybe not needed when missing page will be included in the all document page 24-26

This is clarified in the missing pages (see Pages 26-28)

2. Clarify the difference between model-dependent and model independent methods page 24

The following sentences have been added to page 24:

 ```
All types of scattering patterns can be analysed by two analysis methods; model independent and model-dependent.
Model-independent analysis is where there is no \emph{a priori} information used in the analysis, when there are no assumptions made about the underlaying structure of the sample. 
However, model-dependent analysis is when reasonable assumptions are made about the structure before the analysis is considered. 
```

3. Define Ackley function page 33.

Moved the introduction of the ackley function to the end of the paragraph and added the following:

```
The Ackley function is a common function used for assessing the utility of global optimisation functions, which has the following form in the two-dimensional case, 
%
\begin{equation}
f(x,y) = -a \exp{\big[-b\sqrt{0.5(x^2 + y^2)}\big]} - \exp{\big[0.5(\cos{cx} + \cos{cy})\big]} + e + a,
\end{equation}
where, $a$, $b$, and $c$ are constants defined by the user, and $e$ is the base of the natural logarithm. 
```

4. Page 37. Clarify what is meant by "dynamically relevant structure"

Changed `dynamically` to `thermodynamically`

5. Equation 3.1 page 44, clarify the fitting variables and how the various structural parameters reported in table 3.1 are then obtained (reference to the relevant equation in the reflectometry chapter.)

The following has added following Equation 3.1 

```
The scattering length for the head or tail of the phospholipid can be found based on the different atom types present in each. 
Therefore, the volume and solvation fraction are variables that may be fitted to give value for the SLD that may be used in Equation~\ref{equ:knsld}.
```

Additionally the following has be added to paragraph 4 of page 48 (in the old version)

```
Therefore, the $\text{SLD}_i$ in Equation~\ref{equ:sld} may be found and used in Equation~\ref{equ:knsld}, while the layer thickness may be used in Equation~\ref{equ:nowthick} to calculate the reflected intensity from a given layer. 
```

6. Page 44 – define what you mean by "Chemically consistent modelling"

The following sentences have been added to the chemically-consistent modelling section 

```
Chemically-consistent modelling, in reflectometry analysis, is the reparameterisation of the layer-model into rational chemical terms, such as molecular volume and the elemental scattering lengths. 
This reparameterisation allows for chemically-realistic constraints to be applied to the model.  
```

7. P59 Figure 3.6 label a-d.

The labels on these figures were small (in the top left corner), the size has been increased.

8. Page 78 write the Tanford equation

The following has been added to the tanford equation side note 

```
which has the form $t_t = (1.5 + 1.265)n_c$ \AA, where $t_t$ is the length and $n_c$ is the number of carbon atoms
```

9. Page 94 Figure 5.7 caption: info on sample (concentration, solvent)

Figure caption changed to 

```
The experimental SANS data, from a solution of hydrogenated \ce{C_{10}TANO_3} in \ce{D2O} at a concentration of \SI{\sim0.15}{\mol\deci\meter^{-3}}, to which the real \texttt{fitoog} run was attempting to fit.
```