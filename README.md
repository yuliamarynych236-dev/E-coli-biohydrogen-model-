# E. coli Biohydrogen Production: Metabolic Model Analysis

## Overview

This repository contains a computational analysis of hydrogen (H₂) production in *Escherichia coli* using the genome-scale metabolic model iML1515.

The study focuses on metabolic pathways involved in hydrogen production and evaluates how different metabolic constraints and interventions affect hydrogen yield.

## Objectives

- Analyze the genome-scale metabolic model of *E. coli*.
- Investigate the role of formate hydrogen lyase (FHL) in hydrogen production.
- Evaluate the influence of glucose uptake and growth rate on hydrogen yield.
- Assess the effects of selected metabolic pathway constraints on hydrogen production.
- Identify metabolic factors that may contribute to improving biohydrogen production.

## Tools and Methods

- Python
- Google Colab
- COBRApy
- Flux Balance Analysis (FBA)
- Genome-scale metabolic modeling

## Methodology

The iML1515 metabolic model was analyzed using COBRApy in Google Colab. Flux Balance Analysis was applied to investigate metabolic fluxes and estimate hydrogen production under different model conditions.

The analysis included:
- Evaluation of the initial metabolic model.
- Investigation of formate hydrogen lyase activity.
- Analysis of anaerobic growth conditions.
- Evaluation of the effects of glucose uptake limitations.
- Assessment of selected metabolic pathway constraints.

## Repository Contents

- `E_coli_biohydrogen_analysis.ipynb` – Jupyter notebook containing the computational analysis and results.
- `iML1515 (2).xml.gz` – genome-scale metabolic model of *E. coli* in SBML format.

## Important Note

All results presented in this repository are computational predictions obtained through metabolic modeling. They do not represent experimentally validated measurements. The analysis is based on an existing genome-scale metabolic model and does not involve experimental validation.

## Author

Yuliia Marynych
Khrystyna Malysheva

Stepan Gzhytskyi National University of Veterinary Medicine and Biotechnologies Lviv
