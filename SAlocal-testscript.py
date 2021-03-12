import os
import hjson
from map2loop.project import Project

bbox_3d = {
    'minx': 250805.1529856466,
    'miny': 6405084.328058686,
    'maxx': 336682.921539395,
    'maxy': 6458336.085975628,
    'base': -3200,
    'top': 1200
}

proj = Project(
    structure_file='SA/data/sth_flinders_28354.shp',
    fault_file='SA/data/2M Linear Structures_28354.shp',
    fold_file='SA/data/2M Linear Structures_28354.shp',
    geology_file='SA/data/2M_Surface_Geology_28354_relage.shp',
    mindep_file="SA/data/null_mindeps.shp",
    metadata='SA/data/meta.hjson',
)

proj.update_config(out_dir='sa-local',
                   overwrite="true",
                   bbox_3d=bbox_3d,
                   proj_crs={'init': 'EPSG:28354'},
                   drift_prefix=['T', 'Q', 'water', 'void'],
                   quiet='no-figures',
                   clut_path='SA/data/GSSA_2M_colours.csv')

proj.run()
