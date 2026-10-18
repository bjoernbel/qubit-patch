#!/usr/bin/env python3
"""OpenMC template for the FRB-BB concept.

This file is intentionally a scaffold. In a real study, it would define the
materials, geometry, source, tally settings, and output handling for OpenMC.
"""

from __future__ import annotations


def build_model() -> dict:
    """Return a minimal configuration object for an OpenMC-style setup."""
    return {
        "title": "FRB-BB-2026-KI-001",
        "materials": ["Be-9", "Li-6", "Void"],
        "geometry": "fractal_tree_approximation",
        "source": "fission_like_neutron_source",
        "tallies": ["TBR", "flux", "reaction_rate"],
    }


def main() -> None:
    model = build_model()
    print("OpenMC configuration ready:")
    for key, value in model.items():
        print(f"- {key}: {value}")


if __name__ == "__main__":
    main()
