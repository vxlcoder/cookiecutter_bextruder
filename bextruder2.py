
'''
Copyright (C) 2018 CG Cookie
http://cgcookie.com
hello@cgcookie.com

Created by Jonathan Denning

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import os
import math
import time

import bgl
import bpy
import bmesh
from bpy.types import Panel
from mathutils import Vector
from mathutils.geometry import intersect_line_line
from bmesh.types import BMVert, BMEdge, BMFace

from .addon_common.cookiecutter.cookiecutter import CookieCutter
from .addon_common.common import ui
from .addon_common.common.bmesh_utils import BMeshHideState
from .addon_common.common.maths import Point, Point2D, XForm
from .addon_common.common.decorators import PersistentOptions



class VIEW3D_OT_bextruder2(CookieCutter):
    bl_idname      = 'cgcookie.bextruder2'
    bl_label       = 'BExtruder2'
    bl_description = 'Extrude + Loop Cut'
    bl_space_type  = 'VIEW_3D'
    bl_region_type = 'TOOLS'

    @classmethod
    def can_start(cls, context):
        ''' Start only if editing a mesh '''
        ob = context.active_object
        return (ob and ob.type == 'MESH' and context.mode == 'EDIT_MESH')

    def start(self):
        ''' BExtruder tool is starting '''
        bpy.ops.ed.undo_push()  # push current state to undo
        pass

    @CookieCutter.FSM_State('main')
    def modal_main(self):
        self.done()

