from map2loop.project import Project

proj = Project(
    state="WA",
    remote=True,
    metadata='https://gist.githubusercontent.com/yohanderose/8f843de0dde531f009a3973cbdadcc9f/raw/918f412ae488ce1a6bca188306f7730061ecf551/meta_remote.hjson'
)

proj.update_config(
    out_dir='./model-test',
    overwrite=True,
    bbox_3d={
        "minx": 500000,
        "miny": 7490000,
        "maxx": 545000,
        "maxy": 7520000,
        "base": -3200,
        "top": 1200,
    },
    proj_crs={'init': 'EPSG:28350'},
    quiet=True
)


proj.run()
