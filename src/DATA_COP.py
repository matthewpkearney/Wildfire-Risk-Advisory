#!/home/mkear/miniconda3/bin/python3
import cdsapi

dataset = "cems-fire-historical-v1"
request = {
    "product_type": "reanalysis",
    "dataset_type": "consolidated_dataset",
    "system_version": ["4_1"],
    
    "area": [38.1, -120.1, 37.9, -119.9], #[38, 120], #38N, 120W
    "year": ["2023", "2024"],
    "month": [
        "01", "02", "03",
        "04", "05", "06",
        "07", "08", "09",
        "10", "11", "12"
    ],
    "day": [
        "01", "02", "03",
        "04", "05", "06",
        "07", "08", "09",
        "10", "11", "12",
        "13", "14", "15",
        "16", "17", "18",
        "19", "20", "21",
        "22", "23", "24",
        "25", "26", "27",
        "28", "29", "30",
        "31"
    ],
    "grid": "0.25/0.25",
    "data_format": "grib",
    "variable": ["ignition_component"]
}

client = cdsapi.Client(url= 'https://ewds.climate.copernicus.eu/api', key ='40ee054f-044e-4fa0-958c-63777a1b7c81')
# client = cdsapi.Client()
client.retrieve(dataset, request).download()