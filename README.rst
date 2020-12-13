Thorlabs 30mm cage plate holder (CP33)
========================================

In order to attach an optical cage system to a microscope, I created this.

Features
---------
- Fits one 30mm cage sytem thorlabs cage plate
- Has flaps with two holes on either side to screw into a substrate

Getting Started
--------------------

To generate an STL file for this project, you need to do the following (if you want to modify the STL, otherwise just download it).

Installing Dependencies
~~~~~~~~~~~~~~~~~~~~~~~~

If you have not already, install the [openSCAD](http://www.openscad.org/) and [openpyscad](https://pypi.org/project/openpyscad/)

Issues 
------------------------
1. [FIXED v2] Holes came out too small for screws. I specified 2.6, but the holes came out at ~2.0mm, and the screws appear to be closer to 3mm in diameter. 
2. [FIXED v2] Holes are too close to wall and I cannot screw the things in, becuase the screw caps are butting against the wall. Screw head diameter is 6mm, so I need 1.5mm of clearance from the hole on either side.
3. [FIXED v2] The rods are partially covered on either side, the groove for the cage plate is too deep. It measures ~4mm, it needs to measure no more than 2mm.
4. The whole thing needs to be slightly less wide - it doesn't fit within the tabs on the microscope screw holder. At least 4mm needs to be cut off from the tabs on the side.
5. If the whole thing were just a smidge taller 

Notes
--------
- The screw pitch is almost perfect, and I think should do just fine.
