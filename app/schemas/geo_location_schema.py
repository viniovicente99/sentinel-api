from pydantic import BaseModel, Field

class GeoLocationSchema(BaseModel):
    country: str
    country_code: str = Field(alias="countryCode")
    region: str = Field(alias="regionName")
    city: str
    latitude: float = Field(alias="lat")
    longitude: float = Field(alias="lon")
    isp: str
