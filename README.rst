Shepp-Logan Phantom Data Generator
===================================

**Forked from https://github.com/mckib2/phantominator**

This NLeSC fork is streamlined for generating synthetic Shepp-Logan phantom datasets for AI training.

Installation
============

.. code-block:: bash

    git clone https://github.com/NLeSC-Knowledge-Development/SLphantom-generator
    cd SLphantom-generator
    pip install -e .

Usage
=====

Open the Jupyter notebook:

.. code-block:: bash

    jupyter notebook phantominator/examples/shepp_logan.ipynb

The notebook contains examples and a data generation workflow to create synthetic brain phantom images with variations for training neural networks.

About
=====

Simplified Python package for generating Shepp-Logan phantom images. This fork focuses on:

- CT-style phantom generation
- Batch data generation with anatomical variations
- LoRA dataset format (images + metadata.jsonl)
- Easy-to-use Jupyter notebook interface

    # CT phantom
    from phantominator import shepp_logan
    ph = shepp_logan(128)

    # MR phantom (returns proton density, T1, and T2 maps)
    M0, T1, T2 = shepp_logan((128, 128, 20), MR=True)

The Shepp-Logan 3D phantom has ellipsoids in [-1, 1] along the z-axis.
The 2D Shepp-Logan exists at z=-0.25, so if we want just a subset
along the z-axis with the first slice being the traditional 2D
phantom, we can use the `zlims` option:


Core Functions
==============

.. code-block:: python

    from phantominator import shepp_logan

    # Generate a simple CT phantom
    ph = shepp_logan(128, modified=True)

    # Generate a 3D phantom
    ph = shepp_logan((128, 128, 20), zlims=(-.5, .5))

    # Get ellipse parameters for customization
    ph, E = shepp_logan(128, modified=True, ret_E=True)

See the notebook for detailed examples of batch generation with anatomical variations.

License
=======

See LICENSE file (original MIT license from mckib2/phantominator).
