"""
Creates a near-copy of the thorlabs CP33, modified for one side to mate to a 38mm microscope tube
"""
import openpyscad as ops
import os

plate_width = 40.6
bottom_screw_separation = 51
bottom_screw_pitch = 12
plate_thickness = 8.9
hole_pitch = 30
hole_diameter = 3.6
epsilon = 0.01
tail_width = 6.5
wall_thickness = 1.8

hole_edge_spacing = 2.0
adapter_width = plate_width + 2*wall_thickness + 2*tail_width
adapter_height = plate_width + wall_thickness
adapter_depth = bottom_screw_pitch + 5


adapter = ops.Cube([adapter_width, adapter_depth, adapter_height])
tail_cutout = ops.Cube([tail_width + epsilon, adapter_depth + epsilon, adapter_height - wall_thickness + epsilon])
tail_cutout = tail_cutout.translate([-epsilon, -epsilon/2, wall_thickness])

tail_cutout2 = ops.Cube([tail_width + epsilon, adapter_depth + epsilon, adapter_height - wall_thickness + epsilon])
tail_cutout2 = tail_cutout2.translate([epsilon + adapter_width - tail_width, -epsilon/2, wall_thickness])

center_cutout = ops.Cube([plate_width, adapter_depth + epsilon, plate_width - hole_edge_spacing/2 + epsilon])
center_cutout = center_cutout.translate([tail_width + wall_thickness, -epsilon/2, -epsilon])

plate_cutout = ops.Cube([plate_width, plate_thickness, plate_width])
plate_cutout = plate_cutout.translate([tail_width + wall_thickness, (adapter_depth - plate_thickness)/2, 0])

drill_hole1 = ops.Cylinder(d=hole_diameter, h=wall_thickness + epsilon)
drill_hole1 = drill_hole1.translate([(adapter_width - bottom_screw_separation)/2, (adapter_depth -bottom_screw_pitch)/2, -epsilon/2])

drill_hole2 = ops.Cylinder(d=hole_diameter, h=wall_thickness + epsilon)
drill_hole2 = drill_hole2.translate([(adapter_width + bottom_screw_separation)/2, (adapter_depth -bottom_screw_pitch)/2, -epsilon/2])

drill_hole3 = ops.Cylinder(d=hole_diameter, h=wall_thickness + epsilon)
drill_hole3 = drill_hole3.translate([(adapter_width - bottom_screw_separation)/2, (adapter_depth + bottom_screw_pitch)/2, -epsilon/2])

drill_hole4 = ops.Cylinder(d=hole_diameter, h=wall_thickness + epsilon)
drill_hole4 = drill_hole4.translate([(adapter_width + bottom_screw_separation)/2, (adapter_depth + bottom_screw_pitch)/2, -epsilon/2])

adapter = adapter - tail_cutout - tail_cutout2 - center_cutout - plate_cutout - drill_hole1 - drill_hole2 -\
        drill_hole3 - drill_hole4

filename = 'thorlabs_cage_adapter'
adapter.write(filename + '.scad')

with open(filename + '.scad', 'r') as fn:
    content = fn.read()

with open(filename + '.scad', 'w') as fn:
    fn.write('$fa=0.5;\n$fs=0.5;\n')
    fn.write(content)

os.system('/Applications/OpenSCAD.app/Contents/MacOS/OpenSCAD -o ' + filename + '.stl' + ' ' + filename + '.scad')
