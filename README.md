# SOLIDWORKS-Export-to-Mesh

This is a simple SOLIDWORKS macro to export files to the .3MF format and update the body names within the file.  By default, SOLIDWORKS assigns random names to the bodies saved within these files and it becomes confusing when imported into some FDM slicers like Slic3r, PrusaSlicer, or [SuperSlicer](https://github.com/supermerill/SuperSlicer/releases) (highly recommended) that display body names as opposed to file names.  This macro automatically sets body names to the file name and applies sequential numbers for multi-body files.

Additional functionality from my other SOLIDWORKS macros has crept into this and there are provisions to to export all configurations in a single click, change the file name, export location, file format, and ability to save preferences from within the GUI.

![Screenshot](https://github.com/SigmaRelief/SOLIDWORKS-Export-to-Mesh/blob/master/Doc/Export%20Options%20Screenshot.png)

# Installation
* Place all 4 "Export to Mesh.xxx" files in your preferred macro folder.
* In SOLIDWORKS, click Tools/Customize/Commands/Macro, Select "New Macro Button", and place it in the GUI.
* Point the new button to "Export to Mesh.swp"
* The icon should default to "Export to Mesh.bmp", set it manually if it does not.
* Add a tool tip or prompt if desired.

![SOLIDWORKS Macro Setup](https://github.com/SigmaRelief/SOLIDWORKS-Export-to-Mesh/blob/master/Doc/Macro%20Setup.png)

# Usage
If Python 3.X is installed and already added to the Windows PATH variable, use is as easy as clicking the "Export" button.

![Screenshot with all options](https://github.com/SigmaRelief/SOLIDWORKS-Export-to-Mesh/blob/master/Doc/Export%20Options%20All%20Screenshot.png)

If Python is not added to PATH, launch the macro and click "Configure Python", follow the prompt, then click the "Save settings..." box to save your configuration.

Changes to the default export location can also be saved with the "Save Settings..." box.  The export location can optionally be saved as relative to the user's profile folder by including the [UserDir] variable

Tolerance on mesh files can be optionally adjusted at time of export.  If save settings is selected, these values are set as the new SOLIDWORKS defaults.  SOLIDWORKS uses coarse values by default so it is probably useful to significantly reduce this value if part accuracy and finish are important.

The "Export all configurations" option iterates through all configurations and exports them as individual files.  The file name (and thus internal body names) can be configured via a dropdown to place the SOLIDWORKS configuration name at the beginning or end of the file name, or use the configuration name only.  Entries within this list can be adapted with any desired delimiter or order by typing directly in the dropdown box and saved with the "Save settings..." box.

The file format dropdown only includes .3MF, .STL, and .STEP by default (in both cases to suite your preference).  The body re-naming is only executed with .3MF formats, but most valid file formats are supported should you have a need to do something like exporting all configurations to another format (not limited to mesh types).

The underlying body re-name happens entirely within Python and this portion of the code may be applicable to other CAD tools with minor updates to search for their specific body naming convention.

Variables including SOLIDWORKS Custom Properties, Configuration Names, and current date/time in multiple formats can be included in the File Name and File path fields for single use, or saved as part of the defaults by clicking the Use Variables button.

![Screenshot of Variable Inputs](https://github.com/SigmaRelief/SOLIDWORKS-Export-to-Mesh/blob/master/Doc/Variable%20Inputs%20Screenshot.png)

# Requirements
The rename functionality requires Python 3.X to be installed
The [Date ####] variable requires Microsoft Excel to be installed

# Project status
This code is believed to be stable and ready for general use, but no guarantees or warranty are provided.  It has been tested only with SOLIDWORKS 2019, PrusaSlicer 2.2.0, and SuperSlicer 2.2.53

This is a hobby project and should be treated accordingly.
