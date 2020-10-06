from map2loop.project import Project

proj = Project(
    loopdata_state="WA"
)

bbox = {
    "minx": 500102,
    "miny": 7457565,
    "maxx": 603064,
    "maxy": 7567970,
    "base": -1200,
    "top": 12000,
}
proj.update_config(
    out_dir='./model-test',
    overwrite='true',
    bbox_3d=bbox,
    # bbox_3d={
    #     "minx": 500000,
    #     "miny": 7490000,
    #     "maxx": 545000,
    #     "maxy": 7520000,
    #     "base": -3200,
    #     "top": 1200,
    # },
    proj_crs={'init': 'EPSG:28350'},
    quiet=True
)


proj.run()
