import bpy

#branche1

        
class MyOwnOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.myown_operator"
    bl_label = "my own  Operator"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):     
        print ("my own test operator !!!!")
        return {'FINISHED'} 
           
# sculpt    
class changeToSculptModeOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.change_to_sculpt_operator"
    bl_label = "to sculpt operator"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context): 
        currentScene =bpy.context.scene
        currentLayer = currentScene.active_layer
        objInCurrentLayer = [ob for ob in bpy.context.scene.objects if ob.layers[currentLayer]]
        for obj in objInCurrentLayer: 
         
            if obj.type == 'MESH':
                print (obj)
                obj.select = True  
                bpy.context.scene.objects.active = obj
                # return to the object context to apply transformations
                bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
                bpy.ops.object.transform_apply(location=True)
                bpy.ops.object.transform_apply(rotation=True)
                bpy.ops.object.transform_apply(scale=True)
                # apply sculpt mode 
                bpy.ops.object.mode_set(mode='SCULPT', toggle=False)
          
        
        print ("to sculpt operator !!!!")
        return {'FINISHED'}          
#edit
class changeToEditModeOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.change_to_edit_operator"
    bl_label = "to edit operator"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):     
        currentScene =bpy.context.scene
        currentLayer = currentScene.active_layer
        objInCurrentLayer = [ob for ob in bpy.context.scene.objects if ob.layers[currentLayer]]
        for obj in objInCurrentLayer: 
         
            if obj.type == 'MESH':
                print (obj)
                obj.select = True  
                bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
                #bpy.context.scene.objects.active = obj
                bpy.ops.object.mode_set(mode='EDIT')
                bpy.ops.mesh.select_mode(type="VERT")
                bpy.ops.mesh.select_all(action='SELECT')
                bpy.ops.mesh.vertices_smooth()
                bpy.ops.mesh.subdivide()
 
        return {'FINISHED'}   
    
#createSquircle   
class createSquircle(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.create_squircle"
    bl_label = "to object operator"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        cursorLocation = context.scene.cursor_location
        bpy.ops.mesh.primitive_cube_add(radius=1, view_align=False, enter_editmode=False, location=cursorLocation, layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
        obj =bpy.context.selected_objects[0]
        bpy.context.scene.objects.active = obj
        
        
        bpy.ops.object.modifier_add(type='SUBSURF')
        #bpy.context.object.modifiers["Subsurf"].subdivision_type = 'SIMPLE'
        bpy.context.object.modifiers["Subsurf"].subdivision_type = 'CATMULL_CLARK'
        bpy.context.object.modifiers["Subsurf"].levels = 2
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Subsurf")
        return {'FINISHED'}       

class applySmoothOne(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.apply_smooth_one"
    bl_label = "to object operator"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        obj =bpy.context.selected_objects[0]
        bpy.context.scene.objects.active = obj
        
        
        bpy.ops.object.modifier_add(type='CORRECTIVE_SMOOTH')
        bpy.context.object.modifiers["CorrectiveSmooth"].use_only_smooth = True
        bpy.context.object.modifiers["CorrectiveSmooth"].factor = 0.55
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="CorrectiveSmooth")

        return {'FINISHED'}

class applyDivideOne(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.apply_divide_one"
    bl_label = "to object operator"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        obj =bpy.context.selected_objects[0]
        bpy.context.scene.objects.active = obj
        
        
        bpy.ops.object.modifier_add(type='SUBSURF')
        #bpy.context.object.modifiers["Subsurf"].subdivision_type = 'SIMPLE'
        bpy.context.object.modifiers["Subsurf"].subdivision_type = 'CATMULL_CLARK'
        bpy.context.object.modifiers["Subsurf"].levels = 1
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Subsurf")


        return {'FINISHED'} 
 
 
 
#modifier
class changeToObjectModeOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.change_to_object_operator"
    bl_label = "to object operator"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        currentScene =bpy.context.scene
        currentLayer = currentScene.active_layer
        objInCurrentLayer = [ob for ob in bpy.context.scene.objects if ob.layers[currentLayer]]
        for obj in objInCurrentLayer: 
         
            if obj.type == 'MESH':
                print (obj)
                obj.select = True  
                bpy.context.scene.objects.active = obj
                bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
        return {'FINISHED'}         
        
        
        
        
        
 #draw principal       
class CreateObject(bpy.types.Panel):
    """Creates the Create Object Panel"""
    bl_label = "Create Object"
    bl_idname = "create_object"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "Shortcuts ... (:"

    def draw(self, context):
        layout = self.layout

        obj = context.object
        col = layout.column(align=True)
        row = col.row()
        row.operator("object.change_to_sculpt_operator", text="all to sculpt mode", icon="SCULPTMODE_HLT")
        row = col.row()
        row.operator("object.change_to_object_operator", text="all to object mode", icon="OBJECT_DATAMODE")
        row =col.row()
        row.operator("object.create_squircle", text="createsqircle", icon="OBJECT_DATAMODE")
        
        col.label(text="Cursor:")

        row = col.row()
        row.operator("view3d.snap_cursor_to_center", text="Center")
        row.operator("view3d.view_center_cursor", text="View")

        col.operator("view3d.snap_cursor_to_selected", text="Cursor to Selected")
        row = col.row()
        row.label(text="operations:")
        row = col.row()
        row.operator("object.apply_smooth_one", text="smooth one", icon="OBJECT_DATAMODE")
        row = col.row()
        row.operator("object.apply_divide_one", text="divide one", icon="OBJECT_DATAMODE")
          
        #row.operator("object.change_to_edit_operator", text="all to edit mode", icon="EDITMODE_HLT")
        

def register():
    bpy.utils.register_class(CreateObject)
    bpy.utils.register_class(MyOwnOperator)
    bpy.utils.register_class(changeToSculptModeOperator)
    bpy.utils.register_class(changeToEditModeOperator)
    bpy.utils.register_class(changeToObjectModeOperator)
    bpy.utils.register_class(createSquircle)
    bpy.utils.register_class(applySmoothOne)
    bpy.utils.register_class(applyDivideOne)
    

def unregister():
    bpy.utils.unregister_class(CreateObject)
    bpy.utils.register_class(MyOwnOperator)
    bpy.utils.register_class(changeToSculptModeOperator)
    bpy.utils.register_class(changeToEditModeOperator)
    bpy.utils.register_class(changeToObjectModeOperator)
    bpy.utils.register_class(createSquircle)
    bpy.utils.register_class(applySmoothOne)
    bpy.utils.register_class(applyDivideOne)

if __name__ == "__main__":
    register()



