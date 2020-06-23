# SOLIDWORKS-Export-to-Mesh

This is a simple SOLIDWORKS macro to export files to the .3MF format and update the body names within the file.  By default, SOLIDWORKS assigns random names to the bodies saved within these files and it becomes confusing when imported into slicers like Slic3r, PrusaSlicer, or [SuperSlicer](https://github.com/supermerill/SuperSlicer/releases) (highly reccomended) that display body names as opposed to file names.  This macro automatically sets body names to the file name and applies sequential numbers for multi-body files.

Additional functionality from my other SW macros has crept into this and there are provisions to to export all configurations in a single click, change the file name, export location, and ability to save preferences from within the GUI.

![Screenshot](https://github.com/SigmaRelief/SOLIDWORKS-Export-to-Mesh/blob/master/Doc/Export%20Options%20Screenshot.png)

# Installation
Place all files in your preferred macro folder.
In SOLIDWORKS, click Tools/Customize/Commands/Macro and Select "New Macro Button"
Point the new button to "Export to Mesh.swp"
The icon should default to "Export to Mesh.bmp", set it manually if it does not.
Add a tool tip or prompt if desired.

# Useage
If Python 3.X is installed and already added to the Windows PATH varriable, use is as easy as clicking the "Export" button.

![Screenshot](https://github.com/SigmaRelief/SOLIDWORKS-Export-to-Mesh/blob/master/Doc/Export%20Options%20All%20Screenshot.png)

If Python is not added to PATH click "Configure Python" and follow the prompt, then click the "Save settings..." box to save your configuration.

Changes to the default export location can also be saved with the "Save Settings..." box.  The export location can optionally be saved as relative to the user's profile folder to allow easier shared use.  This option is only visible if the export path is already within the actuve users profile folder.

The "Export all configurations" option itterates through all configurations and exports them as individual files.  The file name (and thus internal body names) can be configured via a dropdown to place the Configuration name at the beginning or end of the file name, or use the configuration name only.  Enties within this list can be adapted with any desired delimiter or order and saved with the "Save settings..." box.

The file format dropdown includes only .3MF and .STL by default (in both both cases to suite your preference).  The body re-naming is only executed with .3MF formats, but most valid file formats are supported should you have a need to do something like exporting all configurations to another format (not limited to mesh types).

The underlying body re-name happens entirely within Python and this portion of the code may be applicable to other CAD tools with minor updates to search for their specific body naming convention.

# Requirements
The rename functionality requires Python 3.X to be installed

# Project status
This code is believed to be stable and ready for general use, but no guarantees or warranty are provided.  It has been tested only with SOLIDWORKS 2019, PrusaSlicer 2.2.0, and SuperSlicer 2.2.51

This ia a hobby project and should be treated accordingly.
