# Authors: Hongyu Wen

import bpy
import random
import mathutils
import numpy as np
from numpy.random import uniform as U, normal as N, randint as RI
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface
from infinigen.core.util import blender as butil

from infinigen.core.util.math import FixedSeed
from infinigen.core.placement.factory import AssetFactory

class OvenFactory(AssetFactory):
    def __init__(self, factory_seed, coarse=False, dimensions=[1., 1., 1.]):
        super(OvenFactory, self).__init__(factory_seed, coarse=coarse)

        self.dimensions = dimensions
        with FixedSeed(factory_seed):

    @staticmethod
    def sample_parameters(dimensions):
        # depth, width, height = dimensions
        depth = 1 + N(0, 0.1)
        width = 1 + N(0, 0.1)
        height = 1 + N(0, 0.1)
        door_thickness = U(0.05, 0.1) * depth
        door_rotation = 0 # Set to 0 for now

        rack_radius = U(0.01, 0.02) * depth
        rack_h_amount = RI(2, 4)
        rack_d_amount = RI(4, 6)

        panel_height = U(0.2, 0.4) * height
        panel_thickness = U(0.15, 0.25) * depth
        botton_amount = RI(1, 3) * 2
        botton_radius = U(0.05, 0.1) * width
        botton_thickness = U(0.02, 0.04) * depth
        heat_radius_ratio = U(0.1, 0.2)

        params = {
            "Depth": depth,
            "Width": width,
            "Height": height,
            "DoorThickness": door_thickness,
            "DoorRotation": door_rotation,
            "RackRadius": rack_radius,
            "RackHAmount": rack_h_amount,
            "RackDAmount": rack_d_amount,
            "PanelHeight": panel_height,
            "PanelThickness": panel_thickness,
            "BottonAmount": botton_amount,
            "BottonRadius": botton_radius,
            "BottonThickness": botton_thickness,
            "HeaterRadiusRatio": heat_radius_ratio,
            "BrandName": brand_name,
        }
    def create_asset(self, **params):
        obj = butil.spawn_cube()
@node_utils.to_nodegroup('nodegroup_hollow_cube', singleton=False, type='GeometryNodeTree')
def nodegroup_hollow_cube(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketVectorTranslation', 'Size', (0.1000, 10.0000, 4.0000)),
            ('NodeSocketVector', 'Pos', (0.0000, 0.0000, 0.0000)),
            ('NodeSocketFloat', 'Thickness', 0.0000),
            ('NodeSocketBool', 'Switch1', False),
            ('NodeSocketBool', 'Switch2', False),
            ('NodeSocketBool', 'Switch3', False),
            ('NodeSocketBool', 'Switch4', False),
            ('NodeSocketBool', 'Switch5', False),
            ('NodeSocketBool', 'Switch6', False)])
    separate_xyz = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': group_input.outputs["Size"]})
    multiply = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input.outputs["Thickness"], 1: 2.0000},
        attrs={'operation': 'MULTIPLY'})
    subtract = nw.new_node(Nodes.Math, input_kwargs={0: separate_xyz.outputs["Y"], 1: multiply}, attrs={'operation': 'SUBTRACT'})
    subtract_1 = nw.new_node(Nodes.Math, input_kwargs={0: separate_xyz.outputs["Z"], 1: multiply}, attrs={'operation': 'SUBTRACT'})
    combine_xyz_4 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': group_input.outputs["Thickness"], 'Y': subtract, 'Z': subtract_1})
    cube_2 = nw.new_node(Nodes.MeshCube,
    store_named_attribute_1 = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': cube_2.outputs["Mesh"], 'Name': 'uv_map', 3: cube_2.outputs["UV Map"]},
        attrs={'domain': 'CORNER', 'data_type': 'FLOAT_VECTOR'})
    multiply_1 = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["Thickness"]}, attrs={'operation': 'MULTIPLY'})
    separate_xyz_1 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': group_input.outputs["Pos"]})
    add = nw.new_node(Nodes.Math, input_kwargs={0: multiply_1, 1: separate_xyz_1.outputs["X"]})
    scale = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: group_input.outputs["Size"], 'Scale': 0.5000},
        attrs={'operation': 'SCALE'})
    separate_xyz_2 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': scale.outputs["Vector"]})
    add_1 = nw.new_node(Nodes.Math, input_kwargs={0: separate_xyz_2.outputs["Y"], 1: separate_xyz_1.outputs["Y"]})
    subtract_2 = nw.new_node(Nodes.Math,
        input_kwargs={0: separate_xyz_2.outputs["Z"], 1: separate_xyz_1.outputs["Z"]},
        attrs={'operation': 'SUBTRACT'})
    combine_xyz_5 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': add, 'Y': add_1, 'Z': subtract_2})
    transform_2 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': store_named_attribute_1, 'Translation': combine_xyz_5})
    switch_2 = nw.new_node(Nodes.Switch, input_kwargs={1: group_input.outputs["Switch3"], 14: transform_2})
    subtract_3 = nw.new_node(Nodes.Math, input_kwargs={0: separate_xyz.outputs["Y"], 1: multiply}, attrs={'operation': 'SUBTRACT'})
    combine_xyz_2 = nw.new_node(Nodes.CombineXYZ,
        input_kwargs={'X': separate_xyz.outputs["X"], 'Y': subtract_3, 'Z': group_input.outputs["Thickness"]})
    cube_1 = nw.new_node(Nodes.MeshCube,
    store_named_attribute_4 = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': cube_1.outputs["Mesh"], 'Name': 'uv_map', 3: cube_1.outputs["UV Map"]},
        attrs={'domain': 'CORNER', 'data_type': 'FLOAT_VECTOR'})
    add_2 = nw.new_node(Nodes.Math, input_kwargs={0: separate_xyz_2.outputs["X"], 1: separate_xyz_1.outputs["X"]})
    add_3 = nw.new_node(Nodes.Math, input_kwargs={0: separate_xyz_2.outputs["Y"], 1: separate_xyz_1.outputs["Y"]})
    subtract_4 = nw.new_node(Nodes.Math, input_kwargs={0: separate_xyz.outputs["Z"], 1: multiply_1}, attrs={'operation': 'SUBTRACT'})
    combine_xyz_3 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': add_2, 'Y': add_3, 'Z': subtract_4})
    transform_1 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': store_named_attribute_4, 'Translation': combine_xyz_3})
    switch_1 = nw.new_node(Nodes.Switch, input_kwargs={1: group_input.outputs["Switch2"], 14: transform_1})
    subtract_5 = nw.new_node(Nodes.Math, input_kwargs={0: separate_xyz.outputs["Y"], 1: multiply}, attrs={'operation': 'SUBTRACT'})
    combine_xyz = nw.new_node(Nodes.CombineXYZ,
        input_kwargs={'X': separate_xyz.outputs["X"], 'Y': subtract_5, 'Z': group_input.outputs["Thickness"]})
    cube = nw.new_node(Nodes.MeshCube,
    store_named_attribute = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': cube.outputs["Mesh"], 'Name': 'uv_map', 3: cube.outputs["UV Map"]},
        attrs={'domain': 'CORNER', 'data_type': 'FLOAT_VECTOR'})
    add_4 = nw.new_node(Nodes.Math, input_kwargs={0: separate_xyz_2.outputs["X"], 1: separate_xyz_1.outputs["X"]})
    add_5 = nw.new_node(Nodes.Math, input_kwargs={0: separate_xyz_2.outputs["Y"], 1: separate_xyz_1.outputs["Y"]})
    add_6 = nw.new_node(Nodes.Math, input_kwargs={0: multiply_1, 1: separate_xyz_1.outputs["Z"]})
    combine_xyz_1 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': add_4, 'Y': add_5, 'Z': add_6})
    transform = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': store_named_attribute, 'Translation': combine_xyz_1})
    switch = nw.new_node(Nodes.Switch, input_kwargs={1: group_input.outputs["Switch1"], 14: transform})
    subtract_6 = nw.new_node(Nodes.Math, input_kwargs={0: separate_xyz.outputs["Y"], 1: multiply}, attrs={'operation': 'SUBTRACT'})
    subtract_7 = nw.new_node(Nodes.Math, input_kwargs={0: separate_xyz.outputs["Z"], 1: multiply}, attrs={'operation': 'SUBTRACT'})
    combine_xyz_6 = nw.new_node(Nodes.CombineXYZ,
        input_kwargs={'X': group_input.outputs["Thickness"], 'Y': subtract_6, 'Z': subtract_7})
    cube_3 = nw.new_node(Nodes.MeshCube,
    store_named_attribute_5 = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': cube_3.outputs["Mesh"], 'Name': 'uv_map', 3: cube_3.outputs["UV Map"]},
        attrs={'domain': 'CORNER', 'data_type': 'FLOAT_VECTOR'})
    subtract_8 = nw.new_node(Nodes.Math, input_kwargs={0: separate_xyz.outputs["X"], 1: multiply_1}, attrs={'operation': 'SUBTRACT'})
    add_7 = nw.new_node(Nodes.Math, input_kwargs={0: separate_xyz_2.outputs["Y"], 1: separate_xyz_1.outputs["Y"]})
    subtract_9 = nw.new_node(Nodes.Math,
        input_kwargs={0: separate_xyz_2.outputs["Z"], 1: separate_xyz_1.outputs["Z"]},
        attrs={'operation': 'SUBTRACT'})
    combine_xyz_7 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': subtract_8, 'Y': add_7, 'Z': subtract_9})
    transform_3 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': store_named_attribute_5, 'Translation': combine_xyz_7})
    switch_3 = nw.new_node(Nodes.Switch, input_kwargs={1: group_input.outputs["Switch4"], 14: transform_3})
    combine_xyz_9 = nw.new_node(Nodes.CombineXYZ,
        input_kwargs={'X': separate_xyz.outputs["X"], 'Y': group_input.outputs["Thickness"], 'Z': separate_xyz.outputs["Z"]})
    cube_4 = nw.new_node(Nodes.MeshCube,
    store_named_attribute_2 = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': cube_4.outputs["Mesh"], 'Name': 'uv_map', 3: cube_4.outputs["UV Map"]},
        attrs={'domain': 'CORNER', 'data_type': 'FLOAT_VECTOR'})
    add_8 = nw.new_node(Nodes.Math, input_kwargs={0: separate_xyz_1.outputs["X"], 1: separate_xyz_2.outputs["X"]})
    add_9 = nw.new_node(Nodes.Math, input_kwargs={0: separate_xyz_1.outputs["Y"], 1: multiply_1})
    add_10 = nw.new_node(Nodes.Math, input_kwargs={0: separate_xyz_1.outputs["Z"], 1: separate_xyz_2.outputs["Z"]})
    combine_xyz_8 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': add_8, 'Y': add_9, 'Z': add_10})
    transform_4 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': store_named_attribute_2, 'Translation': combine_xyz_8})
    switch_4 = nw.new_node(Nodes.Switch, input_kwargs={1: group_input.outputs["Switch5"], 14: transform_4})
    combine_xyz_10 = nw.new_node(Nodes.CombineXYZ,
        input_kwargs={'X': separate_xyz.outputs["X"], 'Y': group_input.outputs["Thickness"], 'Z': separate_xyz.outputs["Z"]})
    cube_5 = nw.new_node(Nodes.MeshCube,
    store_named_attribute_3 = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': cube_5.outputs["Mesh"], 'Name': 'uv_map', 3: cube_5.outputs["UV Map"]},
        attrs={'domain': 'CORNER', 'data_type': 'FLOAT_VECTOR'})
    add_11 = nw.new_node(Nodes.Math, input_kwargs={0: separate_xyz_2.outputs["X"], 1: separate_xyz_1.outputs["X"]})
    subtract_10 = nw.new_node(Nodes.Math, input_kwargs={0: separate_xyz.outputs["Y"], 1: multiply_1}, attrs={'operation': 'SUBTRACT'})
    add_12 = nw.new_node(Nodes.Math, input_kwargs={0: separate_xyz_2.outputs["Z"], 1: separate_xyz_1.outputs["Z"]})
    combine_xyz_11 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': add_11, 'Y': subtract_10, 'Z': add_12})
    transform_5 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': store_named_attribute_3, 'Translation': combine_xyz_11})
    switch_5 = nw.new_node(Nodes.Switch, input_kwargs={1: group_input.outputs["Switch6"], 14: transform_5})
    join_geometry = nw.new_node(Nodes.JoinGeometry,
        input_kwargs={'Geometry': [switch_2.outputs[6], switch_1.outputs[6], switch.outputs[6], switch_3.outputs[6], switch_4.outputs[6], switch_5.outputs[6]]})
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': join_geometry}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_o', singleton=False, type='GeometryNodeTree')
def nodegroup_o(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    curve_line = nw.new_node(Nodes.CurveLine, input_kwargs={'End': (0.0000, 0.0000, 0.0020)})
    group_input = nw.new_node(Nodes.GroupInput, expose_input=[('NodeSocketFloatDistance', 'Size', 1.0000)])
    curve_circle_1 = nw.new_node(Nodes.CurveCircle, input_kwargs={'Radius': group_input.outputs["Size"]})
    curve_to_mesh = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': curve_line, 'Profile Curve': curve_circle_1.outputs["Curve"]})
    extrude_mesh = nw.new_node(Nodes.ExtrudeMesh, input_kwargs={'Mesh': curve_to_mesh, 'Offset Scale': 0.0030})
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Mesh': extrude_mesh.outputs["Mesh"]}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_heater', singleton=False, type='GeometryNodeTree')
def nodegroup_heater(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    curve_line_1 = nw.new_node(Nodes.CurveLine, input_kwargs={'End': (0.0000, 0.0000, 0.0010)})
    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketFloat', 'width', 0.5000),
            ('NodeSocketFloat', 'depth', 0.0000),
            ('NodeSocketFloat', 'radius_ratio', 0.2000),
    minimum = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input.outputs["width"], 1: group_input.outputs["depth"]},
        attrs={'operation': 'MINIMUM'})
    multiply = nw.new_node(Nodes.Math,
        input_kwargs={0: minimum, 1: group_input.outputs["radius_ratio"]},
        label='Multiply',
        attrs={'operation': 'MULTIPLY'})
    curve_circle_1 = nw.new_node(Nodes.CurveCircle, input_kwargs={'Radius': multiply})
    curve_to_mesh_1 = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': curve_line_1, 'Profile Curve': curve_circle_1.outputs["Curve"], 'Fill Caps': True})
    set_material = nw.new_node(Nodes.SetMaterial,
    geometry_to_instance = nw.new_node('GeometryNodeGeometryToInstance', input_kwargs={'Geometry': set_material})
    multiply_1 = nw.new_node(Nodes.Math,
        input_kwargs={0: minimum, 1: group_input.outputs["arrangement_ratio"]},
        label='Multiply',
        attrs={'operation': 'MULTIPLY'})
    divide = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["width"], 1: multiply_1}, attrs={'operation': 'DIVIDE'})
    floor = nw.new_node(Nodes.Math, input_kwargs={0: divide}, attrs={'operation': 'FLOOR'})
    divide_1 = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["depth"], 1: multiply_1}, attrs={'operation': 'DIVIDE'})
    floor_1 = nw.new_node(Nodes.Math, input_kwargs={0: divide_1}, attrs={'operation': 'FLOOR'})
    multiply_2 = nw.new_node(Nodes.Math, input_kwargs={0: floor, 1: floor_1}, attrs={'operation': 'MULTIPLY'})
    duplicate_elements = nw.new_node(Nodes.DuplicateElements,
        input_kwargs={'Geometry': geometry_to_instance, 'Amount': multiply_2},
        attrs={'domain': 'INSTANCE'})
    divide_2 = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["depth"], 1: floor_1}, attrs={'operation': 'DIVIDE'})
    divide_3 = nw.new_node(Nodes.Math,
        input_kwargs={0: duplicate_elements.outputs["Duplicate Index"], 1: floor},
        attrs={'operation': 'DIVIDE'})
    floor_2 = nw.new_node(Nodes.Math, input_kwargs={0: divide_3}, attrs={'operation': 'FLOOR'})
    multiply_3 = nw.new_node(Nodes.Math, input_kwargs={0: floor_2, 1: divide_2}, attrs={'operation': 'MULTIPLY'})
    multiply_add = nw.new_node(Nodes.Math, input_kwargs={0: divide_2, 2: multiply_3}, attrs={'operation': 'MULTIPLY_ADD'})
    divide_4 = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["width"], 1: floor}, attrs={'operation': 'DIVIDE'})
    modulo = nw.new_node(Nodes.Math,
        input_kwargs={0: duplicate_elements.outputs["Duplicate Index"], 1: floor},
        attrs={'operation': 'MODULO'})
    multiply_4 = nw.new_node(Nodes.Math, input_kwargs={0: modulo, 1: divide_4}, attrs={'operation': 'MULTIPLY'})
    multiply_add_1 = nw.new_node(Nodes.Math, input_kwargs={0: divide_4, 2: multiply_4}, attrs={'operation': 'MULTIPLY_ADD'})
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': multiply_add, 'Y': multiply_add_1})
    set_position = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': duplicate_elements.outputs["Geometry"], 'Offset': combine_xyz})
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Mesh': set_position}, attrs={'is_active_output': True})


@node_utils.to_nodegroup('nodegroup_oven_rack', singleton=False, type='GeometryNodeTree')
def nodegroup_oven_rack(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketFloatDistance', 'Width', 2.0000),
            ('NodeSocketFloatDistance', 'Height', 2.0000),
            ('NodeSocketFloatDistance', 'Radius', 0.0200),
            ('NodeSocketInt', 'Amount', 5)])
    quadrilateral = nw.new_node('GeometryNodeCurvePrimitiveQuadrilateral',
        input_kwargs={'Width': group_input.outputs["Width"], 'Height': group_input.outputs["Height"]})
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["Height"], 1: -0.5000}, attrs={'operation': 'MULTIPLY'})
    combine_xyz_3 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Y': multiply})
    multiply_1 = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["Height"]}, attrs={'operation': 'MULTIPLY'})
    combine_xyz_4 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Y': multiply_1})
    curve_line = nw.new_node(Nodes.CurveLine, input_kwargs={'Start': combine_xyz_3, 'End': combine_xyz_4})
    geometry_to_instance = nw.new_node('GeometryNodeGeometryToInstance', input_kwargs={'Geometry': curve_line})
    duplicate_elements = nw.new_node(Nodes.DuplicateElements,
        input_kwargs={'Geometry': geometry_to_instance, 'Amount': group_input.outputs["Amount"]},
        attrs={'domain': 'INSTANCE'})
    multiply_2 = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["Width"]}, attrs={'operation': 'MULTIPLY'})
    divide = nw.new_node(Nodes.Math,
        input_kwargs={0: multiply_2, 1: group_input.outputs["Amount"]},
        attrs={'operation': 'DIVIDE'})
    multiply_3 = nw.new_node(Nodes.Math,
        input_kwargs={0: duplicate_elements.outputs["Duplicate Index"], 1: divide},
        attrs={'operation': 'MULTIPLY'})
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': multiply_3})
    set_position = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': duplicate_elements.outputs["Geometry"], 'Offset': combine_xyz})
    duplicate_elements_1 = nw.new_node(Nodes.DuplicateElements,
        input_kwargs={'Geometry': geometry_to_instance, 'Amount': group_input.outputs["Amount"]},
        attrs={'domain': 'INSTANCE'})
    multiply_4 = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["Width"], 1: -0.5000}, attrs={'operation': 'MULTIPLY'})
    divide_1 = nw.new_node(Nodes.Math,
        input_kwargs={0: multiply_4, 1: group_input.outputs["Amount"]},
        attrs={'operation': 'DIVIDE'})
    multiply_5 = nw.new_node(Nodes.Math,
        input_kwargs={0: duplicate_elements_1.outputs["Duplicate Index"], 1: divide_1},
        attrs={'operation': 'MULTIPLY'})
    combine_xyz_1 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': multiply_5})
    set_position_1 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': duplicate_elements_1.outputs["Geometry"], 'Offset': combine_xyz_1})
    join_geometry = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [quadrilateral, set_position, set_position_1]})
    curve_circle = nw.new_node(Nodes.CurveCircle, input_kwargs={'Radius': group_input.outputs["Radius"]})
    curve_to_mesh = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': join_geometry, 'Profile Curve': curve_circle.outputs["Curve"], 'Fill Caps': True})
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Mesh': curve_to_mesh}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_text', singleton=False, type='GeometryNodeTree')
def nodegroup_text(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketVectorTranslation', 'Translation', (1.5000, 0.0000, 0.0000)),
            ('NodeSocketString', 'String', 'BrandName'),
            ('NodeSocketFloatDistance', 'Size', 0.0500),
            ('NodeSocketFloat', 'Offset Scale', 0.0020)])
    string_to_curves = nw.new_node('GeometryNodeStringToCurves',
        input_kwargs={'String': group_input.outputs["String"], 'Size': group_input.outputs["Size"]},
        attrs={'align_y': 'BOTTOM_BASELINE', 'align_x': 'CENTER'})
    fill_curve = nw.new_node(Nodes.FillCurve, input_kwargs={'Curve': string_to_curves.outputs["Curve Instances"]})
    extrude_mesh = nw.new_node(Nodes.ExtrudeMesh,
        input_kwargs={'Mesh': fill_curve, 'Offset Scale': group_input.outputs["Offset Scale"]})
    transform_1 = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': extrude_mesh.outputs["Mesh"], 'Translation': group_input.outputs["Translation"], 'Rotation': (1.5708, 0.0000, 1.5708)})
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': transform_1}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_handle', singleton=False, type='GeometryNodeTree')
def nodegroup_handle(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketFloat', 'width', 0.0000),
            ('NodeSocketFloat', 'length', 0.0000),
            ('NodeSocketFloat', 'thickness', 0.0200)])
    cube = nw.new_node(Nodes.MeshCube, input_kwargs={'Size': group_input.outputs["width"]})
    store_named_attribute = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': cube.outputs["Mesh"], 'Name': 'uv_map', 3: cube.outputs["UV Map"]},
        attrs={'domain': 'CORNER', 'data_type': 'FLOAT_VECTOR'})
    cube_1 = nw.new_node(Nodes.MeshCube, input_kwargs={'Size': group_input.outputs["width"]})
    store_named_attribute_1 = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': cube_1.outputs["Mesh"], 'Name': 'uv_map', 3: cube_1.outputs["UV Map"]},
        attrs={'domain': 'CORNER', 'data_type': 'FLOAT_VECTOR'})
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Y': group_input.outputs["length"]})
    transform = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': store_named_attribute_1, 'Translation': combine_xyz})
    join_geometry_1 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [store_named_attribute, transform]})
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["width"]}, attrs={'operation': 'MULTIPLY'})
    combine_xyz_3 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': multiply})
    transform_2 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': join_geometry_1, 'Translation': combine_xyz_3})
    add = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["length"], 1: group_input.outputs["width"]})
    combine_xyz_1 = nw.new_node(Nodes.CombineXYZ,
        input_kwargs={'X': group_input.outputs["width"], 'Y': add, 'Z': group_input.outputs["thickness"]})
    cube_2 = nw.new_node(Nodes.MeshCube, input_kwargs={'Size': combine_xyz_1})
    store_named_attribute_2 = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': cube_2.outputs["Mesh"], 'Name': 'uv_map', 3: cube_2.outputs["UV Map"]},
        attrs={'domain': 'CORNER', 'data_type': 'FLOAT_VECTOR'})
    multiply_1 = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["length"]}, attrs={'operation': 'MULTIPLY'})
    multiply_2 = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["thickness"]}, attrs={'operation': 'MULTIPLY'})
    add_1 = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["width"], 1: multiply_2})
    combine_xyz_2 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Y': multiply_1, 'Z': add_1})
    transform_1 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': store_named_attribute_2, 'Translation': combine_xyz_2})
    join_geometry = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [transform_2, transform_1]})
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': join_geometry}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_center', singleton=False, type='GeometryNodeTree')
def nodegroup_center(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketVector', 'Vector', (0.0000, 0.0000, 0.0000)),
            ('NodeSocketFloat', 'MarginX', 0.5000),
            ('NodeSocketFloat', 'MarginY', 0.0000),
            ('NodeSocketFloat', 'MarginZ', 0.0000)])
    bounding_box = nw.new_node(Nodes.BoundingBox, input_kwargs={'Geometry': group_input.outputs["Geometry"]})
    subtract = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: group_input.outputs["Vector"], 1: bounding_box.outputs["Min"]},
        attrs={'operation': 'SUBTRACT'})
    separate_xyz = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': subtract.outputs["Vector"]})
    greater_than = nw.new_node(Nodes.Math,
        input_kwargs={0: separate_xyz.outputs["X"], 1: group_input.outputs["MarginX"]},
        attrs={'operation': 'GREATER_THAN', 'use_clamp': True})
    subtract_1 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: bounding_box.outputs["Max"], 1: group_input.outputs["Vector"]},
        attrs={'operation': 'SUBTRACT'})
    separate_xyz_1 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': subtract_1.outputs["Vector"]})
    greater_than_1 = nw.new_node(Nodes.Math,
        input_kwargs={0: separate_xyz_1.outputs["X"], 1: group_input.outputs["MarginX"]},
        attrs={'operation': 'GREATER_THAN', 'use_clamp': True})
    op_and = nw.new_node(Nodes.BooleanMath, input_kwargs={0: greater_than, 1: greater_than_1})
    greater_than_2 = nw.new_node(Nodes.Math,
        input_kwargs={0: separate_xyz.outputs["Y"], 1: group_input.outputs["MarginY"]},
        attrs={'operation': 'GREATER_THAN'})
    greater_than_3 = nw.new_node(Nodes.Math,
        input_kwargs={0: separate_xyz_1.outputs["Y"], 1: group_input.outputs["MarginY"]},
        attrs={'operation': 'GREATER_THAN', 'use_clamp': True})
    op_and_1 = nw.new_node(Nodes.BooleanMath, input_kwargs={0: greater_than_2, 1: greater_than_3})
    op_and_2 = nw.new_node(Nodes.BooleanMath, input_kwargs={0: op_and, 1: op_and_1})
    greater_than_4 = nw.new_node(Nodes.Math,
        input_kwargs={0: separate_xyz.outputs["Z"], 1: group_input.outputs["MarginZ"]},
        attrs={'operation': 'GREATER_THAN', 'use_clamp': True})
    greater_than_5 = nw.new_node(Nodes.Math,
        input_kwargs={0: separate_xyz_1.outputs["Z"], 1: group_input.outputs["MarginZ"]},
        attrs={'operation': 'GREATER_THAN', 'use_clamp': True})
    op_and_3 = nw.new_node(Nodes.BooleanMath, input_kwargs={0: greater_than_4, 1: greater_than_5})
    op_and_4 = nw.new_node(Nodes.BooleanMath, input_kwargs={0: op_and_2, 1: op_and_3})
    op_not = nw.new_node(Nodes.BooleanMath, input_kwargs={0: op_and_4}, attrs={'operation': 'NOT'})
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'In': op_and_4, 'Out': op_not}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_cube', singleton=False, type='GeometryNodeTree')
def nodegroup_cube(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketVectorTranslation', 'Size', (0.1000, 10.0000, 4.0000)),
            ('NodeSocketVector', 'Pos', (0.0000, 0.0000, 0.0000)),
    cube = nw.new_node(Nodes.MeshCube,
        input_kwargs={'Size': group_input.outputs["Size"], 'Vertices X': group_input.outputs["Resolution"], 'Vertices Y': group_input.outputs["Resolution"], 'Vertices Z': group_input.outputs["Resolution"]})
    store_named_attribute_1 = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': cube.outputs["Mesh"], 'Name': 'uv_map', 3: cube.outputs["UV Map"]},
        attrs={'domain': 'CORNER', 'data_type': 'FLOAT_VECTOR'})
    store_named_attribute = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': store_named_attribute_1, 'Name': 'uv_map'},
        attrs={'domain': 'CORNER', 'data_type': 'FLOAT_VECTOR'})
    multiply_add = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: group_input.outputs["Size"], 1: (0.5000, 0.5000, 0.5000), 2: group_input.outputs["Pos"]},
        attrs={'operation': 'MULTIPLY_ADD'})
    transform = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': store_named_attribute, 'Translation': multiply_add.outputs["Vector"]})
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': transform}, attrs={'is_active_output': True})


    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketFloat', 'Depth', 1.0000),
            ('NodeSocketFloat', 'Width', 1.0000),
            ('NodeSocketFloat', 'Height', 1.0000),
            ('NodeSocketFloat', 'DoorThickness', 0.0700),
            ('NodeSocketFloat', 'DoorRotation', 0.0000),
            ('NodeSocketFloatDistance', 'RackRadius', 0.0100),
            ('NodeSocketInt', 'RackHAmount', 2),
            ('NodeSocketInt', 'RackDAmount', 5),
            ('NodeSocketFloat', 'PanelHeight', 0.3000),
            ('NodeSocketFloat', 'PanelThickness', 0.2000),
            ('NodeSocketInt', 'BottonAmount', 4),
            ('NodeSocketFloatDistance', 'BottonRadius', 0.0500),
            ('NodeSocketFloat', 'BottonThickness', 0.0300),
            ('NodeSocketFloat', 'HeaterRadiusRatio', 0.1500),
    combine_xyz_1 = nw.new_node(Nodes.CombineXYZ,
        input_kwargs={'X': group_input.outputs["DoorThickness"], 'Y': group_input.outputs["Width"], 'Z': group_input.outputs["Height"]})
    combine_xyz_2 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': group_input.outputs["Depth"]})
    cube = nw.new_node(nodegroup_cube().name, input_kwargs={'Size': combine_xyz_1, 'Pos': combine_xyz_2})
    position = nw.new_node(Nodes.InputPosition)
    center = nw.new_node(nodegroup_center().name,
        input_kwargs={'Geometry': cube, 'Vector': position, 'MarginX': -1.0000, 'MarginY': 0.1000, 'MarginZ': 0.1500})
    set_material_2 = nw.new_node(Nodes.SetMaterial,
    set_material_3 = nw.new_node(Nodes.SetMaterial,
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["Width"], 1: 0.0500}, attrs={'operation': 'MULTIPLY'})
    multiply_1 = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["Width"], 1: 0.8000}, attrs={'operation': 'MULTIPLY'})
    multiply_2 = nw.new_node(Nodes.Math, input_kwargs={0: multiply}, attrs={'operation': 'MULTIPLY'})
    handle = nw.new_node(nodegroup_handle().name,
        input_kwargs={'width': multiply, 'length': multiply_1, 'thickness': multiply_2})
    add = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["Depth"], 1: group_input.outputs["DoorThickness"]})
    multiply_3 = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["Width"]}, attrs={'operation': 'MULTIPLY'})
    multiply_4 = nw.new_node(Nodes.Math, input_kwargs={0: multiply_1, 1: -0.5000}, attrs={'operation': 'MULTIPLY'})
    add_1 = nw.new_node(Nodes.Math, input_kwargs={0: multiply_3, 1: multiply_4})
    multiply_5 = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["Height"], 1: 0.9200}, attrs={'operation': 'MULTIPLY'})
    combine_xyz_13 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': add, 'Y': add_1, 'Z': multiply_5})
    transform_1 = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': handle, 'Translation': combine_xyz_13, 'Rotation': (0.0000, 1.5708, 0.0000)})
    set_material_8 = nw.new_node(Nodes.SetMaterial,
    add_2 = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["Depth"], 1: group_input.outputs["DoorThickness"]})
    multiply_6 = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["Width"]}, attrs={'operation': 'MULTIPLY'})
    combine_xyz_12 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': add_2, 'Y': multiply_6, 'Z': 0.0300})
    multiply_7 = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["Height"], 1: 0.0500}, attrs={'operation': 'MULTIPLY'})
    text = nw.new_node(nodegroup_text().name,
        input_kwargs={'Translation': combine_xyz_12, 'String': group_input.outputs["BrandName"], 'Size': multiply_7})
    set_material_9 = nw.new_node(Nodes.SetMaterial,
    geometry_to_instance = nw.new_node('GeometryNodeGeometryToInstance', input_kwargs={'Geometry': join_geometry_3})
    combine_xyz_4 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': group_input.outputs["Depth"]})
    rotate_instances = nw.new_node(Nodes.RotateInstances,
        input_kwargs={'Instances': geometry_to_instance, 'Rotation': combine_xyz_3, 'Pivot Point': combine_xyz_4})
    door = nw.new_node(Nodes.Reroute, input_kwargs={'Input': rotate_instances}, label='door')
    multiply_8 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input.outputs["DoorThickness"], 1: 2.1000},
        attrs={'operation': 'MULTIPLY'})
    subtract = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input.outputs["Depth"], 1: multiply_8},
        attrs={'operation': 'SUBTRACT'})
    multiply_9 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input.outputs["DoorThickness"], 1: 2.1000},
        attrs={'operation': 'MULTIPLY'})
    subtract_1 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input.outputs["Width"], 1: multiply_9},
        attrs={'operation': 'SUBTRACT'})
    ovenrack = nw.new_node(nodegroup_oven_rack().name,
        input_kwargs={'Width': subtract, 'Height': subtract_1, 'Radius': group_input.outputs["RackRadius"], 'Amount': group_input.outputs["RackDAmount"]})
    geometry_to_instance_1 = nw.new_node('GeometryNodeGeometryToInstance', input_kwargs={'Geometry': ovenrack})
    duplicate_elements = nw.new_node(Nodes.DuplicateElements,
        input_kwargs={'Geometry': geometry_to_instance_1, 'Amount': group_input.outputs["RackHAmount"]},
        attrs={'domain': 'INSTANCE'})
    multiply_10 = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["Depth"]}, attrs={'operation': 'MULTIPLY'})
    multiply_11 = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["Width"]}, attrs={'operation': 'MULTIPLY'})
    add_3 = nw.new_node(Nodes.Math, input_kwargs={0: duplicate_elements.outputs["Duplicate Index"], 1: 1.0000})
    multiply_12 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input.outputs["DoorThickness"], 1: 2.0000},
        attrs={'operation': 'MULTIPLY'})
    subtract_2 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input.outputs["Height"], 1: multiply_12},
        attrs={'operation': 'SUBTRACT'})
    add_4 = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["RackHAmount"], 1: 1.0000})
    divide = nw.new_node(Nodes.Math, input_kwargs={0: subtract_2, 1: add_4}, attrs={'operation': 'DIVIDE'})
    multiply_13 = nw.new_node(Nodes.Math, input_kwargs={0: add_3, 1: divide}, attrs={'operation': 'MULTIPLY'})
    combine_xyz_5 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': multiply_10, 'Y': multiply_11, 'Z': multiply_13})
    set_position = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': duplicate_elements.outputs["Geometry"], 'Offset': combine_xyz_5})
    set_material = nw.new_node(Nodes.SetMaterial,
    racks = nw.new_node(Nodes.Reroute, input_kwargs={'Input': set_material}, label='racks')
    add_5 = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["Depth"], 1: group_input.outputs["DoorThickness"]})
    reroute_10 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': add_5})
    reroute_11 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Width"]})
    reroute_8 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["DoorThickness"]})
    combine_xyz_6 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': reroute_10, 'Y': reroute_11, 'Z': reroute_8})
    reroute_9 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Height"]})
    combine_xyz_7 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': reroute_9})
    cube_1 = nw.new_node(nodegroup_cube().name, input_kwargs={'Size': combine_xyz_6, 'Pos': combine_xyz_7})
    set_material_5 = nw.new_node(Nodes.SetMaterial,
    subtract_3 = nw.new_node(Nodes.Math,
        input_kwargs={0: reroute_10, 1: group_input.outputs["PanelThickness"]},
        attrs={'operation': 'SUBTRACT'})
    multiply_add = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input.outputs["HeaterRadiusRatio"], 1: 2.0000, 2: 0.1000},
        attrs={'operation': 'MULTIPLY_ADD'})
    heater = nw.new_node(nodegroup_heater().name,
        input_kwargs={'width': reroute_11, 'depth': subtract_3, 'radius_ratio': group_input.outputs["HeaterRadiusRatio"], 'arrangement_ratio': multiply_add})
    add_6 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_8, 1: reroute_9})
    combine_xyz_15 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': group_input.outputs["PanelThickness"], 'Z': add_6})
    transform_2 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': heater, 'Translation': combine_xyz_15})
    heater_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': join_geometry_2}, label='heater')
    reroute_14 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Width"]})
    combine_xyz_9 = nw.new_node(Nodes.CombineXYZ,
        input_kwargs={'X': group_input.outputs["PanelThickness"], 'Y': reroute_14, 'Z': group_input.outputs["PanelHeight"]})
    add_7 = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["Height"], 1: group_input.outputs["DoorThickness"]})
    combine_xyz_8 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': add_7})
    cube_2 = nw.new_node(nodegroup_cube().name, input_kwargs={'Size': combine_xyz_9, 'Pos': combine_xyz_8})
    position_1 = nw.new_node(Nodes.InputPosition)
    center_1 = nw.new_node(nodegroup_center().name,
        input_kwargs={'Geometry': cube_2, 'Vector': position_1, 'MarginX': -1.0000, 'MarginY': 0.0500, 'MarginZ': 0.0500})
    set_material_4 = nw.new_node(Nodes.SetMaterial,
    set_material_7 = nw.new_node(Nodes.SetMaterial,
    reroute_13 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["PanelThickness"]})
    multiply_14 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_14}, attrs={'operation': 'MULTIPLY'})
    bounding_box = nw.new_node(Nodes.BoundingBox, input_kwargs={'Geometry': cube_2})
    add_8 = nw.new_node(Nodes.VectorMath, input_kwargs={0: bounding_box.outputs["Min"], 1: bounding_box.outputs["Max"]})
    scale = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: add_8.outputs["Vector"], 'Scale': 0.5000},
        attrs={'operation': 'SCALE'})
    separate_xyz = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': scale.outputs["Vector"]})
    combine_xyz_16 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': reroute_13, 'Y': multiply_14, 'Z': separate_xyz.outputs["Z"]})
    multiply_15 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input.outputs["PanelHeight"], 1: 0.2000},
        attrs={'operation': 'MULTIPLY'})
    text_1 = nw.new_node(nodegroup_text().name,
        input_kwargs={'Translation': combine_xyz_16, 'String': '12:01', 'Size': multiply_15})
    combine_xyz_21 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': group_input.outputs["BottonThickness"]})
    curve_line = nw.new_node(Nodes.CurveLine, input_kwargs={'End': combine_xyz_21})
    reroute_12 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["BottonRadius"]})
    curve_circle = nw.new_node(Nodes.CurveCircle, input_kwargs={'Radius': reroute_12})
    curve_to_mesh = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': curve_line, 'Profile Curve': curve_circle.outputs["Curve"], 'Fill Caps': True})
    add_9 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_12, 1: 0.0050})
    o = nw.new_node(nodegroup_o().name, input_kwargs={'Size': add_9})
    join_geometry_4 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [curve_to_mesh, o]})
    combine_xyz_10 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': reroute_13, 'Z': separate_xyz.outputs["Z"]})
    transform = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': join_geometry_4, 'Translation': combine_xyz_10, 'Rotation': (0.0000, 1.5708, 0.0000)})
    reroute_16 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': separate_xyz.outputs["Z"]})
    reroute_15 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["BottonRadius"]})
    multiply_16 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input.outputs["PanelHeight"], 1: 0.0500},
        attrs={'operation': 'MULTIPLY'})
    multiply_add_1 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_15, 1: 1.0000, 2: multiply_16}, attrs={'operation': 'MULTIPLY_ADD'})
    add_10 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_16, 1: multiply_add_1})
    combine_xyz_17 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': reroute_13, 'Z': add_10})
    multiply_17 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input.outputs["BottonRadius"], 1: 0.2500},
        attrs={'operation': 'MULTIPLY'})
    text_2 = nw.new_node(nodegroup_text().name,
        input_kwargs={'Translation': combine_xyz_17, 'String': 'Off', 'Size': multiply_17})
    multiply_add_2 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_15, 1: 0.7000, 2: multiply_16}, attrs={'operation': 'MULTIPLY_ADD'})
    add_11 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_16, 1: multiply_add_2})
    combine_xyz_18 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': reroute_13, 'Y': multiply_add_2, 'Z': add_11})
    text_3 = nw.new_node(nodegroup_text().name,
        input_kwargs={'Translation': combine_xyz_18, 'String': 'High', 'Size': multiply_17})
    multiply_18 = nw.new_node(Nodes.Math, input_kwargs={0: multiply_16, 1: -1.0000}, attrs={'operation': 'MULTIPLY'})
    multiply_add_3 = nw.new_node(Nodes.Math,
        input_kwargs={0: reroute_15, 1: -0.7000, 2: multiply_18},
        attrs={'operation': 'MULTIPLY_ADD'})
    combine_xyz_19 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': reroute_13, 'Y': multiply_add_3, 'Z': add_11})
    text_4 = nw.new_node(nodegroup_text().name,
        input_kwargs={'Translation': combine_xyz_19, 'String': 'Low', 'Size': multiply_17})
    add_12 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_13, 1: group_input.outputs["BottonThickness"]})
    combine_xyz_20 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': add_12, 'Z': separate_xyz.outputs["Z"]})
    multiply_19 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input.outputs["BottonThickness"], 1: 0.1000},
        attrs={'operation': 'MULTIPLY'})
    text_5 = nw.new_node(nodegroup_text().name,
        input_kwargs={'Translation': combine_xyz_20, 'String': '1', 'Size': group_input.outputs["BottonRadius"], 'Offset Scale': multiply_19})
    join_geometry_6 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [transform, text_2, text_3, text_4, text_5]})
    geometry_to_instance_2 = nw.new_node('GeometryNodeGeometryToInstance', input_kwargs={'Geometry': join_geometry_6})
    add_13 = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["BottonAmount"], 1: 2.0000})
    reroute_6 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': add_13})
    duplicate_elements_1 = nw.new_node(Nodes.DuplicateElements,
        input_kwargs={'Geometry': geometry_to_instance_2, 'Amount': reroute_6},
        attrs={'domain': 'INSTANCE'})
    add_14 = nw.new_node(Nodes.Math, input_kwargs={0: duplicate_elements_1.outputs["Duplicate Index"], 1: 1.0000})
    add_15 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_6, 1: 1.0000})
    divide_1 = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["Width"], 1: add_15}, attrs={'operation': 'DIVIDE'})
    multiply_20 = nw.new_node(Nodes.Math, input_kwargs={0: add_14, 1: divide_1}, attrs={'operation': 'MULTIPLY'})
    combine_xyz_11 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Y': multiply_20})
    set_position_1 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': duplicate_elements_1.outputs["Geometry"], 'Offset': combine_xyz_11})
    multiply_21 = nw.new_node(Nodes.Math, input_kwargs={0: add_13}, attrs={'operation': 'MULTIPLY'})
    add_16 = nw.new_node(Nodes.Math, input_kwargs={0: multiply_21, 1: -1.0100})
    greater_than = nw.new_node(Nodes.Math,
        input_kwargs={0: duplicate_elements_1.outputs["Duplicate Index"], 1: add_16},
        attrs={'operation': 'GREATER_THAN'})
    add_17 = nw.new_node(Nodes.Math, input_kwargs={0: multiply_21, 1: 0.9900})
    less_than = nw.new_node(Nodes.Math,
        input_kwargs={0: duplicate_elements_1.outputs["Duplicate Index"], 1: add_17},
        attrs={'operation': 'LESS_THAN'})
    minimum = nw.new_node(Nodes.Math, input_kwargs={0: greater_than, 1: less_than}, attrs={'operation': 'MINIMUM'})
    delete_geometry = nw.new_node(Nodes.DeleteGeometry,
        input_kwargs={'Geometry': set_position_1, 'Selection': minimum},
        attrs={'domain': 'INSTANCE'})
    set_material_6 = nw.new_node(Nodes.SetMaterial,
    botton = nw.new_node(Nodes.Reroute, input_kwargs={'Input': set_material_6}, label='botton')
    join_geometry_1 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [join_geometry_5, botton]})
    geometry_to_instance_3 = nw.new_node('GeometryNodeGeometryToInstance', input_kwargs={'Geometry': join_geometry_1})
    combine_xyz_14 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': group_input.outputs["Height"]})
    rotate_instances_1 = nw.new_node(Nodes.RotateInstances,
    panel = nw.new_node(Nodes.Reroute, input_kwargs={'Input': rotate_instances_1}, label='panel')
    combine_xyz = nw.new_node(Nodes.CombineXYZ,
        input_kwargs={'X': group_input.outputs["Depth"], 'Y': group_input.outputs["Width"], 'Z': group_input.outputs["Height"]})
    hollowcube = nw.new_node(nodegroup_hollow_cube().name,
        input_kwargs={'Size': combine_xyz, 'Thickness': group_input.outputs["DoorThickness"], 'Switch2': True, 'Switch4': True})
    set_material_1 = nw.new_node(Nodes.SetMaterial,
    join_geometry = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [door, racks, heater_1, panel, body]})
    group_output = nw.new_node(Nodes.GroupOutput,
