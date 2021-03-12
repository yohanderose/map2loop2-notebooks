from map2loop.project import Project

proj = Project(loopdata_state="QLD")

bbox = {
    'minx': 530362.2738029042,
    'maxx': 631236.933233082,
    'miny': 7437099.547519395,
    'maxy': 7529747.5257176235,
    'base': -12000.0,
    'top': 1200.0
}

proj.update_config(
    out_dir='./qld-test',
    overwrite='true',
    # loopFilename='qld-test.loop3d',
    bbox_3d=bbox,
    # bbox_3d={
    #     "minx": 500000,
    #     "miny": 7490000,
    #     "maxx": 545000,
    #     "maxy": 7520000,
    #     "base": -3200,
    #     "top": 1200,
    # },
    proj_crs={'init': 'EPSG:20355'},
    quiet='no-figures')

proj.run()
