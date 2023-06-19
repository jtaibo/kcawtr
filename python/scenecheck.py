import sys
import maya.standalone
import maya.cmds as cmds


if len(sys.argv) < 3:
    print("KCAWTR scenecheck: invalid arguments")
    exit(-1)

the_project = sys.argv[1]
the_scene = sys.argv[2]

# Set project and open scene

maya.standalone.initialize("Python")
cmds.workspace(the_project, openWorkspace=True)
opened_file = cmds.file(the_scene, o=True)

# Get render settings configuration from defaultRenderGlobals node
# https://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/Nodes/renderGlobals.html

start_frame = int(maya.cmds.getAttr("defaultRenderGlobals.startFrame"))
end_frame = int(maya.cmds.getAttr("defaultRenderGlobals.endFrame"))
frame_padding = maya.cmds.getAttr("defaultRenderGlobals.extensionPadding")
img_format = maya.cmds.getAttr("defaultRenderGlobals.imfkey")

# Get renderable cameras

cameras = maya.cmds.ls(type="camera")
renderable_cameras = []
for c in cameras:
    if maya.cmds.getAttr(c+".renderable"):
        renderable_cameras.append(c)

# Get renderable layers

layers = maya.cmds.ls(type="renderLayer")
renderable_layers = []
for l in layers:
    if maya.cmds.getAttr(l+".renderable"):
        renderable_layers.append(l)

print("--------------------------------------------------------------------------")
print("Start frame: ", start_frame)
print("End frame  : ", end_frame)
print("Padding: ", frame_padding)
print("Cameras: ", renderable_cameras)
print("Layers: ", renderable_layers)
print("Format: ", img_format)

# Generate full paths for expected render files
# https://help.autodesk.com/view/MAYAUL/2023/ENU/?guid=__CommandsPython_renderSettings_html

for c in renderable_cameras:
    for l in renderable_layers:
        for f in range(start_frame, end_frame+1):
            fn = str(f).zfill(frame_padding)
            #fn = ("%0" + str(frame_padding) + "d").format(f)
            render_path = cmds.renderSettings(genericFrameImageName=fn, camera=c, layer=l, fullPath=True)
            print(render_path)

print("--------------------------------------------------------------------------")
