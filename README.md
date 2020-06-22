# SOLIDWORKS-Export-to-Mesh
SOLIDWORKS Macro to rename bodies within .3MF exports

This is a simple SOLIDWORKS macro to export files to the .3MF format that is preferred for use with many new FDM slicers like Slic3r, PrusaSlicer, SuperSlicer, and many others.  By default, SOLIDWORKS assigns random names to the bodies saved within these files and it becomes confusing when imported into some slicers that display body names as opposed to file names.

Additional functionality from my other SW macros has crept into this and there are provisions to change the file name, export location, and ability to export all configurations in a single click, and ability to save preferences from within the GUI.

# Requirements
The rename functionality requires Python 3.X to be installed
