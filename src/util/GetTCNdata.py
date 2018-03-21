# _*_ coding: utf-8 *_*
#Autor: Darwin Rosero Vaca
#Descripción:

from netCDF4 import Dataset
import pandas as pd
import numpy as np

class GetTCNdata():
    """"""

    def __init__(self):
        """Constructor for GetTCNdata"""
        print("Constructor")

    def getData(self, rutaNC,ncVar):
#### ℃ =K - 273.15
        """Lee el archivo NC de datos diarios generados para la tercera comunicacion nacional
                 con las coordenadas de una estacion"""
        dataset = Dataset(rutaNC)
        # print("leyendo el netcdf\n imprimiendo el metadato")
        print(dataset.file_format)
        print(dataset.dimensions['time'])
        print(dataset.variables.keys())
        # print(dataset.variables['precipitation'])
        # print(dataset.variables)
        """longitud = X, latitud = Y Precipitacion = precipitation"""
        # dataset.
        #lat = dataset.variables['lat'][:]
        #lon = dataset.variables['lon'][:]
        print("Latitud ..........................................\n", dataset.variables['lat'],
              "Longitud .........................................\n", dataset.variables['lon'],
              "Longitud .........................................\n")
        var = dataset.variables[ncVar][:]
        #entendiendo los arrays multidemencionales
        print("###################################")
        print("###################################")
        print("var size",var.size,"var ndim",var.ndim,"Var shape ",var.shape)
        print("###################################")
        #var[tiempo,latitud,longitud]
        print("len T ",var[364,0,0],"len [0] ",len(var[0]),"len [365] ",len(var[2]))
        varm = var.mean(axis=0)
        print("longitud :::::::::",varm.size, " : ", len(varm) ,"var por año ::::::::::: \n",varm)
        var_units = dataset.variables[ncVar].units
        #print("latitud ::::::::",dataset.variables['lat'],"longitud :::::::: ",dataset.variables['lon'],"Variable ::::::",dataset.variables[ncVar])

        print("units" ,var_units)
        print("rr length ",len(var))
        return var

    def unirData(self, añoI, añoF,rutaGen,var):

        for a in range(añoI,añoF):
            rutanc=rutaGen+"/tas_day_Ecuador_Ensamble_rcp45_"+str(a)+".nc"
            varnc=nc.getData(rutanc,var)
            print("Archivo ==> ",rutanc)

        print("")


    def getCoord(self, rutaNC):
        """Retorna las coordenadas de las salidasd del modelo WRF"""
        dataset = Dataset(rutaNC)
        # print("leyendo el netcdf\n imprimiendo el metadato")
        print(dataset.file_format)
        print(dataset.dimensions.keys())
        # print(dataset.dimensions['T'])
        # print(dataset.variables.keys())
        # print(dataset.variables['precipitation'])
        # print(dataset.variables)
        """longitud = X, latitud = Y Precipitacion = precipitation"""
        # dataset.
        lat = dataset.variables['XLAT'][1]
        #latdf=pd.DataFrame(lat)
        #latdf.to_csv("/home/drosero/Escritorio/latitud.csv")
        print("latitudes #########################################################33")
        print(dataset.variables['XLAT'])
        print("longitudes #########################################################33")
        print(dataset.variables['XLONG'])
        lon = dataset.variables['XLONG'][0,0]
        print("longitudes[2] #########################################################33")
        #lon = dataset.variables['XLONG'][2]
        print("lat: ",len(lat)," - lon: ",len(lon),"\n",lat,"\n",lon)
        print("############################################3fin getCoor")
        return  lat


    def findCoor(self, latnc, lonnc, latp, lonp):
        """Retorna un serie de tiempo desde el netcdf dada un latitud y longitug"""

        # print(latp," metodo findCoor ", lonp)
        ncmx = np.where(latnc >= latp)
        mx = len(ncmx[0])
        latncb = [latnc[mx - 1], latnc[mx]]
        # print("latitudes ", latncb)
        a = abs(latncb[0]) - abs(latp)
        b = abs(latp) - abs(latncb[1])
        corfin = []
        pos = []
        if a > b:
            corfin.append(latncb[1])
            pos.append(mx)
        else:
            corfin.append(latncb[0])
            pos.append(mx - 1)
        # print("********************************")
        # print(lonnc)
        ncmx = np.where(lonnc <= lonp)
        # print(lonnc[ncmx])
        mx = len(ncmx[0])
        lonncb = [lonnc[mx - 1], lonnc[mx]]
        a = abs(lonncb[0]) - abs(lonp)
        b = abs(lonp) - abs(lonncb[1])
        if a > b:
            corfin.append(lonncb[1])
            pos.append(mx)
        else:
            corfin.append(lonncb[0])
            pos.append(mx - 1)
        # print("longitudes ",lonncb)
        # print("############################################")
        return {"coor": corfin, "pos": pos}

##/media/drosero/Datos/Hydrobid/Dinamico/Mensuales/TMed/RCP45/tas_day_Ecuador_Ensamble_rcp45_2011.nc
##"/media/drosero/Datos/Hydrobid/Dinamico/Mensuales/TMed/RCP45/tas_day_Ecuador_CSIRO-Mk3-6-0_rcp45_2011.nc"

rutagen="/media/darwin/Darwin/Diarios/TMed/RCP45"
#rutagen="/media/drosero/Datos/Hydrobid/Dinamico/Diarios/TMed/RCP45"
#rutagen="/media/drosero/Datos/Hydrobid/Dinamico/Diarios/TMed/RCP45/tas_day_Ecuador_Ensamble_rcp45_"
nc=GetTCNdata()
nc.unirData(2011,2012,rutagen,"temp")
#nc.getData(ruta,"temp")