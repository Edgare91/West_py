import io
import json

"""
	Student: Gabriel Solomon
	Module: gladysSatellite
	Description: This module does …
"""


def readSat(sat, pathToJSONDataFiles):
    """
            reads satellite data from a json file
            Students do NOT need to change the readSat function.
    """

    # data file path
    fileName = sat + "-satellite.json"

    # print("filePath = ", filePath)
    filePath = pathToJSONDataFiles + "/" + fileName

    # open the file
    try:
        fileHandle = open(filePath)
    except IOError:
        print("ERROR: Unable to open the file " + filePath)
        raise IOError

    # read the file
    data = json.load(fileHandle)

    return data


def gpsValue(x, y, sat):
    """
            document your function definition here. what does it do?
    """

    """

	"""
    pathToJSONDataFiles = "C:/Users/jerom/GitHub/evc-cit134a-python/gladys-west-map/data"

    # read the satellite data
    data = readSat(sat, pathToJSONDataFiles)

    """
		delete the remaining code *in this function* and replace it with
		your own code. add more code to do what the assignment asks of you.

		tip: here is where students need to look through the data variable
		read from the satellites and find a matching x,y to return the value.
		to understand better, open and look at the json satellite data in
		vs code.
	"""
    value = 1234

    return value
