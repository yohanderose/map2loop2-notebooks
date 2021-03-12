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
    out_dir='wa-remote',
    overwrite='true',
    # loopFilename='lachie.loop3d',
    bbox_3d=bbox,
    proj_crs={'init': 'EPSG:28350'},
    quiet='all'
)

proj.run()
