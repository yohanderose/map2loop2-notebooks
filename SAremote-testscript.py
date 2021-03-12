from map2loop.project import Project

bbox_3d = {
    'minx': 250805.1529856466,
    'miny': 6405084.328058686,
    'maxx': 336682.921539395,
    'maxy': 6458336.085975628,
    'base': -3200,
    'top': 1200
}

proj = Project(loopdata_state="SA")

proj.update_config(out_dir='sa-remote',
                   overwrite="true",
                   bbox_3d=bbox_3d,
                   proj_crs={'init': 'EPSG:28354'},
                #    drift_prefix=['T', 'Q', 'water', 'void'],
                #    quiet='no-figures',
                   )
proj.run()
