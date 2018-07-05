#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Start with sine design that need to be printed.

def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()

# Simulate creating a 3d print from design.
        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed(completed_models):
    """ Show all the models that were printed."""
    
    print("\nThe following models have been printed: ")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['iphone case', 'robot', 'dodecahedron']
completed_models = []
print_models(unprinted_designs[:], completed_models)

show_completed(completed_models)
