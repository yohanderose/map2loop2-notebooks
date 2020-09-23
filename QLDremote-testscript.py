from map2loop.project import Project
import time

boundaries = [-33446374, -29211962, 771333707, 773977324, -1200, 12000]
bbox = {"minx": boundaries[0], "maxx": boundaries[1], "miny": boundaries[2],
        "maxy": boundaries[3], "base": boundaries[5], "top": boundaries[4]}

metadata = "https://gist.githubusercontent.com/yohanderose/7ad2ae1b36e4e0b3f27dff17eeae0cc2/raw/82c2120a9a554d470ab28199d9ee9d6bb41f9d0f/QLD_meta.hjson"

start = time.time()
proj = Project(state="QLD",
               remote=True,
               metadata=metadata
               )
postInit = time.time()
print("MAP2LOOP Project init takes " + str(postInit-start) + " seconds")
proj.update_config(
    out_dir="model-test",
    overwrite=True,
    bbox_3d=bbox,
    step_out=0.1,
    proj_crs={'init': "EPSG:28355"},
    quiet=True
)
postConfig = time.time()
print("MAP2LOOP Project config takes " + str(postConfig-postInit) + " seconds")
# proj.plot()
proj.run()
postRun = time.time()
print("MAP2LOOP Project run takes " + str(postRun-postConfig) + " seconds")

print("Total map2loop time is " + str(time.time()-start))
