# collection of functions to be used in the MHW_LENS2 project
import numpy as np

def get_ij(longitude, latitude, POPgrd):
    """
    i, j = get_ij(longitude, latitude, grd)

    return the index of the closest point on the grid from the
    point (longitude,latitude) in degree
    """


    lon = POPgrd.TLONG
    lat = POPgrd.TLAT

    lon = lon[:,:] - longitude
    lat = lat[:,:] - latitude

    diff = (lon * lon) + (lat * lat)

    jindex, iindex = np.where(diff==diff.min())

    return iindex[0], jindex[0]
