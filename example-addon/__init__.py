# if reloading a blender add-on while in blender the bpy package is already imported.
# So we only want to reload our add-on packages if that's the case.
if "bpy" in locals():
    # example of reloading .py files
    # import importlib
    # from . import your_package
    # importlib.reload(your_package)
    pass
else:
    import bpy
    # from . import your_package
    pass

bl_info = {
    "name": "Example Add-on",
    "author": "Your name.",
    "version": (0, 0, 1),
    "blender": (3, 3, 1),
    "category": "Generic",
    "location": "View3D",
}

# Because of potential unit tests we need to wrap this under try/catch
# Otherwise it crashes on the bpy.utils.register_classes_factory part.
try:
    def register():
        # bpy.utils.register_class(your_package.your_class)
        pass


    def unregister():
        # bpy.utils.unregister_class(your_package.your_class)
        pass

    # This allows you to run the script directly from Blender's Text editor
    # to test the add-on without having to install it.
    if __name__ == "__main__":
        register()
except TypeError:
    pass
