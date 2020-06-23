# SOLIDWORKS-Export-to-Mesh

This is a simple SOLIDWORKS macro to export files to the .3MF format and updates the body names within the file.  By default, SOLIDWORKS assigns random names to the bodies saved within these files and it becomes confusing when imported into slicers like Slic3r, PrusaSlicer, or [SuperSlicer](https://github.com/supermerill/SuperSlicer/releases) (highly reccomended) that display body names as opposed to file names.

Additional functionality from my other SW macros has crept into this and there are provisions to to export all configurations in a single click, change the file name, export location, and ability to save preferences from within the GUI.

![Screenshot](/Doc/Export Options Screenshot.png)

# Requirements
The rename functionality requires Python 3.X to be installed

# Project status
This code is believed to be stable and ready for general use, but no guarantees or warranty are provided.  It has been tested only with SOLIDWORKS 2019, PrusaSlicer 2.2.0, and SuperSlicer 2.2.51
