physicalproperty - Descriptor class for physical property attributes
********************************************************************

Scope
=====
This module features a `PhysicalProperty` descriptor class which is useful for implementing class attributes which model a physical property. Specifically, `PhysicalProperty` provides class attributes with:

* Units
* Optional upper and/or lower bounds

Units and upper/lower bounds are defined along with the class definition; any attempt to set the attribute with an incompatible unit or a value out-of-bounds will raise an exception.

Constraining class attributes in this way provides assurance that, for example, an absolute temperature cannot accidentally be set to a negative value, a voltage can't accidentally be set to a capacitance, etc.


Documentation
=============
Located on `ReadTheDocs <http://physicalproperty.readthedocs.org>`_.


Installation
============
Dependencies
------------
* `numpy <http://www.numpy.org>`_
* `astropy <http://www.astropy.org>`_

The `physicalproperty` module currently only works with python 2.7.

Since this package depends on `numpy`, I've eschewed the tradiational pip/pypi approach for packaging and distribution and instead opted for `conda <http://conda.pydata.org/docs/index.html>`_/`binstar <https://binstar.org>`_. I recommend using the most recent release of the `Anaconda scientific python distribution <https://store.continuum.io/cshop/anaconda/>`_ by `Continuum Analytics <https://www.continuum.io>`_ to mitigate the difficulty of installing `numpy` on your system. Once you've installed anaconda, you can install the most recent version of `physicalproperty` like so::

    conda install -c jrsmith3 physicalproperty

Building from source
--------------------
First, clone the `git repo <https://github.com/jrsmith3/physicalproperty>`_ or uncompress a tarball of the source. Second, execute the following command::

    conda build path/to/physicalproperty/conda.recipe

Finally, install the built package with::

    conda install physicalproperty --use-local


Examples
========
Lets say you want to implement a class which will return the energy flux of `blackbody emission <https://en.wikipedia.org/wiki/Black-body_radiation>`_. ::

    >>> from astropy import units, constants
    >>> from physicalproperty import PhysicalProperty
    >>> class blackbody(object):
    ...     """
    ...     Model blackbody radiator
    ...     """
    ...     temp = PhysicalProperty(unit="K", lo_bnd=0)
    ...     emissivity = PhysicalProperty(lo_bnd=0, up_bnd=1)
    ...     def __init__(self, temp, emissivity=1):
    ...         self.temp = temp
    ...         self.emissivity = emissivity
    ...     def energy_flux(self):
    ...         """
    ...         Energy flux from blackbody radiator
    ...         """
    ...         flux = constants.sigma_sb * self.emissivity * self.temp**4
    ...         return flux.to("W/m2")
    >>> bb = blackbody(temp=300)
    >>> bb.temp
    <Quantity 300.0 K>
    >>> bb.energy_flux()
    <Quantity 459.30021300000004 W / m2>
    >>> bb.temp = -10.2
    Traceback (most recent call last):
    ValueError: Cannot set less than 0.0 K


License
=======
The code is licensed under the `MIT license <http://opensource.org/licenses/MIT>`_. You can use this code in your project without telling me, but it would be great to hear about who's using the code. You can reach me at joshua.r.smith@gmail.com.


Contributing
============
The repository is hosted on `github <https://github.com/jrsmith3/physicalproperty>`_ . Feel free to fork this project and/or submit a pull request. Please notify me of any issues using the `issue tracker <https://github.com/jrsmith3/physicalproperty/issues>`_ .

In the unlikely event that a community forms around this project, please adhere to the `Python Community code of conduct <https://www.python.org/psf/codeofconduct/>`_.

Version numbers follow the `PEP440 <https://www.python.org/dev/peps/pep-0440/>`_ rubric. Versions will have three components: major.minor.patch. These components can be understood within the `semver <http://semver.org/>`_ rubric.
