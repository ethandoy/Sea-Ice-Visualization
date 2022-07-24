"""
Read from CSV file and represent data in Blender

This file is meant to be run in the blender console

Created By: Ethan Doyle
03/07/22
"""

import bpy
import csv

def read_file(file):
    """
    reads in a csv file, and appends it to a nested list data structure
    """
    data = []
    with open (file) as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)
    return data

def assign_texture(value):
    """
    assigns proper texture to geometry,
    takes value as an input to determine proper z scale of normal map
    """
    #appends texture
    bpy.context.object.data.materials.append(bpy.data.materials["SnowIce"]) 
    #properly scales normal map on z-axis
    bpy.data.materials["SnowIce"].node_tree.nodes["Mapping.002"].inputs[3].default_value[2] = value

def generate_geo(data_list):
    """
    takes a 2D input list and generates cubes in the correct (x,y,z) position
    and correct z-axis scale
    """
    for i in data_list:
        #needed variables
        x = int(i[1])
        y = int(i[2])
        val = float(i[3])
        z = val/2
        #generates cube geometry in proper place
        bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD', location=(x, y, z), scale=(1, 1, val))
        
        assign_texture(val)

def main():
    filename = "2021Data.csv" 
    data_list = read_file(filename)
    generate_geo(data_list)
    
    
if __name__ == "__main__":
    main()