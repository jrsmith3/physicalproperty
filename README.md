physicalproperty - Descriptor class for physical property attributes
********************************************************************

Scope
=====
This module features a `PhysicalProperty` descriptor class which is useful for implementing class attributes which model a physical property. Specifically, `PhysicalProperty` provides class attributes with:

* Units
* Optional upper and/or lower bounds

Units and upper/lower bounds are defined along with the class definition; any attempt to set the attribute with an incompatible unit or a value out-of-bounds will raise an exception.

Constraining class attributes in this way provides assurance that, for example, an absolute temperature cannot accidentally be set to a negative value, a voltage can't accidentally be set to a capacitance, etc.


Installation
============
pip
---
`physicalproperty` is [hosted on pypi](), so installation is simple:

```
pip install physicalproperty
```

non-pip
-------
If you are writing python code using descriptor classes, you probably already know how to download the tarball and execute:

```
python setup.py install
```


Examples
========
Lets say you want to implement a class which will return the energy flux of [blackbody emission]().

```python
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

```

License
=======
The code is licensed under the `MIT license <http://opensource.org/licenses/MIT>`_. You can use this code in your project without telling me, but it would be great to hear about who's using the code. You can reach me at joshua.r.smith@gmail.com.


Contributing
============
The repository is hosted on `github <https://github.com/jrsmith3/ibei>`_ . Feel free to fork this project and/or submit a pull request. Please notify me of any issues using the `issue tracker <https://github.com/jrsmith3/ibei/issues>`_ .

In the unlikely event that a community forms around this project, please adhere to the `Python Community code of conduct <https://www.python.org/psf/codeofconduct/>`_.

Version numbers follow the `semver <http://semver.org>`_ rubric.


API Reference
=============
