from lasio import read
import json
from fastapi import APIRouter
filename = './data/WL_0503696_00_01_18_077_07W5_03_Leg_3_Data_Curves.las'
# ['DEPTH', 'ROP', 'GAS', 'GAMMA']
router = APIRouter()


@router.get('/')
def read_file():
    # Read the LAS file and get the LASFile object
    las_file = read(filename)

    # Access the header information
    header = las_file.header
    print('Header', header['Curves'])

    # Access the curve data
    curves = dict()
    # convert numpy array to list
    curves['depth'] = {
        'values': las_file.curves['DEPTH'].data.tolist(),
        'name': 'depth',
        'unit': 'm'
    }
    curves['gamma'] = {'values': las_file.curves['GAMMA'].data.tolist(),
                       'name': 'gamma',
                       'unit': 'API'}
    curves['gas'] = {'values': las_file.curves['GAS'].data.tolist(),
                     'name': 'gas',
                     'unit': 'unit'}
    curves['rop'] = {'values': las_file.curves['ROP'].data.tolist(),
                     'name': 'rop',
                     'unit': 'm/min'}
    # print('length', len(las_file.data))
    json_data = json.dumps(curves)

    return json_data
