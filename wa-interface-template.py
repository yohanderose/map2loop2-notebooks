from map2loop.project import Project
import LoopProjectFile
# from threading import Timer
import time

# Accept loopFilename from python state otherwise default
if ('loopFilename' not in vars() and 'loopFilename' not in globals()):
    loopFilename = "lachie.loop3d"

loopFilename = "lachie.loop3d"
print(loopFilename)

# data_dir = "gibberish"

# # TODO: Add utm/gda zone when that can happen
# # Collect extents from loopFilename
# resp = LoopProjectFile.Get(loopFilename, "extents")
# if resp["errorFlag"]:
#     boundaries = [-334463.74, -292119.62,
#                   7713337.07, 7739773.24, -1200.0, 12000.0]
#     print(resp["errorString"])
# else:
#     boundaries = resp["value"]["utm"][2:] + resp["value"]["depth"]


# def swap(list2):
#     return [min(list2), max(list2)]

# boundaries = swap(boundaries[0:2]) + swap(boundaries[2:4]) + swap(boundaries[4:6])


# bbox = {"minx": boundaries[0], "maxx": boundaries[1], "miny": boundaries[2],
#         "maxy": boundaries[3], "base": boundaries[5], "top": boundaries[4]}
# bbox2 = str(bbox["minx"])+","+str(bbox["miny"])+"," + \
#     str(bbox["maxx"])+","+str(bbox["maxy"])

bbox = {
    "minx": 500000,
    "miny": 7490000,
    "maxx": 545000,
    "maxy": 7520000,
    "base": -3200,
    "top": 1200,
}

proj = Project(
    state="WA",
    remote=True,
    metadata='https://gist.githubusercontent.com/yohanderose/8f843de0dde531f009a3973cbdadcc9f/raw/918f412ae488ce1a6bca188306f7730061ecf551/meta_remote.hjson'
)

proj.update_config(
    out_dir='./lachie',
    overwrite=True,
    bbox_3d=bbox,
    proj_crs={'init': 'EPSG:28350'},
    quiet=False
)


proj.run()
proj.config.update_projectfile(loopFilename)
proj.config.export_png()
