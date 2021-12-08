from .base import NCEIBase


class Station(NCEIBase):

    """
    Stations are where the data comes from (for most datasets) and can be considered the smallest 
    granual of location data. If the desired station is known, all of its data can quickly be viewed
    
    Additional Query Parameters
    
        datasetid [Optional] 
            Accepts a valid dataset id or a chain of dataset ids separated by ampersands. Stations 
            returned will be supported by dataset(s) specified
        locationid [Optional]
            Accepts a valid location id or a chain of location ids separated by ampersands. Stations 
            returned will contain data for the location(s) specified
        datacategoryid [Optional] 
            Accepts a valid data category id or an array of data category ids. Stations returned will 
            be associated with the data category(ies) specified
        datatypeid [Optional]
            Accepts a valid data type id or a chain of data type ids separated by ampersands. Stations 
            returned will contain all of the data type(s) specified
        extent [Optional] 
            The desired geographical extent for search. Designed to take a parameter generated by 
            Google Maps API V3 LatLngBounds.toUrlValue. Stations returned must be located within the 
            extent specified.
        startdate [Optional] 
            Accepts valid ISO formated date (yyyy-mm-dd). Stations returned will have data after the 
            specified date. Paramater can be use independently of enddate
        enddate [Optional] 
            Accepts valid ISO formated date (yyyy-mm-dd). Stations returned will have data before the 
            specified date. Paramater can be use independently of startdate
        sortfield [Optional]
            The field to sort results by. Supports id, name, mindate, maxdate, and datacoverage fields
        sortorder [	Optional]
            Which order to sort by, asc or desc. Defaults to asc
        limit [Optional]
            Defaults to 25, limits the number of results in the response. Maximum is 1000
        offset [Optional]
            Defaults to 0, used to offset the resultlist. The example would begin with record 24
    """

    parameters = (
        "datasetid",
        "locationid",
        "datacategoryid",
        "datatypeid",
        "extent",
        "startdate",
        "enddate",
        "sortfield",
        "sortorder",
        "limit",
        "offset"
    )
    
    endpoint = NCEIBase.endpoint + "stations"
    
    __slots__ = [
        'elevation', 
        'mindate', 
        'maxdate', 
        'latitude', 
        'name', 
        'datacoverage', 
        'id', 
        'elevationUnit', 
        'longitude'
    ]
