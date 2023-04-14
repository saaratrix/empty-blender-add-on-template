# Blender 3.4.1 add-on template
An empty boilerplate template for creating a Blender Add-on project.

A dedicated folder for the add-on source files in case you need more files than just the add-on code.
For example for unit tests.

## Set-up
Rename the folder `example-addon` and update `setup.py`'s name and description.
Your Blender add-on code goes into the `example-addon` folder. 

Run `pip install -e .` which installs the [fake-bpy-module](https://github.com/nutti/fake-bpy-module) package. \
Alternatively `pip install fake-bpy-module-3.4`.

From fake-bpy-module for PyCharm users:
> Note: For PyCharm users, change the value idea.max.intellisense.filesize in idea.properties file to more than 2600 because some modules have the issue of being too big for intelliSense to work.

Help -> Edit Custom Properties -> Add `idea.max.intellisense.filesize=SIZE` where SIZE is 2600 or larger.

### Linking add-on folder to Blender
We want to symlink the `example-addon` folder to Blender's `scripts/addons` folder to automatically copy all the files to Blender.

On Windows 10 the syntax is:
`mklink /D "Target" "Source"`

Example:
`mklink /D "C:\Program Files\Blender Foundation\Blender\3.4\scripts\addons\example-addon" "C:\Users\User\empty-blender-add-on-template\example-addon"`

## Activating add-on in blender
Your add-on should now be inside the addons folder inside Blender you navigate to the add-ons preference.

Edit -> Preferences -> Add-ons -> Find or Search for your add-on and activate it.

## Ready to code!
That's it, you're all set up to start developing your Blender add-on. 

### More information:
Blender's official documentation: https://docs.blender.org/manual/en/latest/advanced/scripting/introduction.html


To my own blog:
* [Reloading Blender Add-on without restarting Blender](https://saaratrix.blogspot.com/2020/01/easily-reloading-blender-addon.html)
* [Debugging a Blender Add-on in PyCharm](https://saaratrix.blogspot.com/2020/03/debugging-blender-add-on-in-pycharm.html)
* [Create Blender add-on project in PyCharm](https://saaratrix.blogspot.com/2020/02/create-blender-add-on-project-with.html)