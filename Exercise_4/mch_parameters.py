#!/usr/bin/env python3
# -*- coding: utf-8 -*-

params = {}
#%% HUMIDITY PARAMETERS

params['uto200s0'] = {}
params['uto200s0']['name'] = 'Absolute humidity'
params['uto200s0']['units'] = 'g/m3'
params['uto200s0']['description'] = 'Absolute air humidity 2 m above ground; current value'
params['uto200s0']['short_name'] = 'abs_hum'

params['pva200s0'] = {}
params['pva200s0']['name'] = 'Vapor pressure'
params['pva200s0']['units'] = 'hPa'
params['pva200s0']['description'] = 'Vapour pressure 2 m above ground; current value'
params['pva200s0']['short_name'] = 'vapor_pres'

params['pvamixs0'] = {}
params['pvamixs0']['name'] = 'Mixing ratio'
params['pvamixs0']['units'] = 'g/kg'
params['pvamixs0']['description'] = 'Mixing ratio'
params['pvamixs0']['short_name'] = 'mix_ratio'

params['ure200s0'] = {}
params['ure200s0']['name'] = 'Relative humidity'
params['ure200s0']['units'] = '%'
params['ure200s0']['description'] = 'Relative air humidity 2 m above ground; current value'
params['ure200s0']['short_name'] = 'rel_hum'

params['pvaices0'] = {}
params['pvaices0']['name'] = 'Ice vapor pressure'
params['pvaices0']['units'] = 'hPa'
params['pvaices0']['description'] = 'Vapour pressure over ice; current value'
params['pvaices0']['short_name'] = 'ice_vap_pres'

params['pvawats0'] = {}
params['pvawats0']['name'] = 'Water vapor pressure'
params['pvawats0']['units'] = 'hPa'
params['pvawats0']['description'] = 'Vapour pressure over water; current value'
params['pvawats0']['short_name'] = 'water_vap_pres'

params['tde200s0'] = {}
params['tde200s0']['name'] = 'Dewpoint temperature'
params['tde200s0']['units'] = 'degree C'
params['tde200s0']['description'] = 'Dewpoint temperature 2 m above ground; current value'
params['tde200s0']['short_name'] = 'dwpt_temp'

#%% PRESSURE PARAMETERS

params['prestas0'] = {}
params['prestas0']['name'] = 'Pressure'
params['prestas0']['units'] = 'hPa'
params['prestas0']['description'] = 'Atmospheric pressure at barometric altitude (QFE); current value'
params['prestas0']['short_name'] = 'pressure'

params['pp0qnhs0']={}
params['pp0qnhs0']['name'] = 'Sea-level pressure'
params['pp0qnhs0']['units'] = 'hPa'
params['pp0qnhs0']['description'] = 'Pressure reduced to sea level according to standard atmosphere (QNH); current value'
params['pp0qnhs0']['short_name'] = 'sl_pressure'

#%% TEMPERATURE PARAMETERS

params['tre200s0'] = {}
params['tre200s0']['name'] = 'Temperature'
params['tre200s0']['units'] = 'deg C'
params['tre200s0']['description'] = 'Air temperature 2 m above ground; current value'
params['tre200s0']['short_name'] = 'temp'

params['tre200hx'] = {}
params['tre200hx']['name'] = 'Temperature hourly max'
params['tre200hx']['units'] = 'deg C'
params['tre200hx']['description'] = 'Air temperature 2 m above ground; hourly maximum'
params['tre200hx']['short_name'] = 'temp_hmax'

params['tre200hn'] = {}
params['tre200hn']['name'] = 'Temperature hourly min'
params['tre200hn']['units'] = 'deg C'
params['tre200hn']['description'] = 'Air temperature 2 m above ground; hourly minimum'
params['tre200hn']['short_name'] = 'temp_hmin'

params['tre200h0'] = {}
params['tre200h0']['name'] = 'Temperature hourly mean'
params['tre200h0']['units'] = 'deg C'
params['tre200h0']['description'] = 'Air temperature 2 m above ground; hourly mean'
params['tre200h0']['short_name'] = 'temp_hmean'

params['tre200hs'] = {}
params['tre200hs']['name'] = 'Temperature hourly'
params['tre200hs']['units'] = 'deg C'
params['tre200hs']['description'] = 'Air temperature 2 m above ground; hourly current value'
params['tre200hs']['short_name'] = 'temp_h'

#%% WIND PARAMETERS

params['fkl010z1'] = {}
params['fkl010z1']['name'] = 'Gust maximum'
params['fkl010z1']['units'] = 'm/s'
params['fkl010z1']['description'] = 'Gust peak (one second); maximum'
params['fkl010z1']['short_name'] = 'gust'

params['fkl010z0'] = {}
params['fkl010z0']['name'] = 'Wind speed'
params['fkl010z0']['units'] = 'm/s'
params['fkl010z0']['description'] = 'Wind speed scalar; ten minutes mean'
params['fkl010z0']['short_name'] = 'wspeed'

params['fve010z0'] = {}
params['fve010z0']['name'] = 'Wind speed vect'
params['fve010z0']['units'] = 'm/s'
params['fve010z0']['description'] = 'Wind speed vectorial; ten minutes mean'
params['fve010z0']['short_name'] = 'wspeed_vect'

params['dkl010z0'] = {}
params['dkl010z0']['name'] = 'Wind direction'
params['dkl010z0']['units'] = 'degree'
params['dkl010z0']['description'] = 'Wind direction; ten minutes mean'
params['dkl010z0']['short_name'] = 'wdir'

#%% PRECIPITATION PARAMETERS

params['hns000s0'] = {}
params['hns000s0']['name'] = 'Fresh snow'
params['hns000s0']['units'] = 'cm'
params['hns000s0']['description'] = 'Fresh snow; current value'
params['hns000s0']['short_name'] = 'fresh_snow'

params['rre150z0'] = {}
params['rre150z0']['name'] = 'Precipitation'
params['rre150z0']['units'] = 'mm'
params['rre150z0']['description'] = 'Precipitation; ten minutes total'
params['rre150z0']['short_name'] = 'precip'

params['rco150z0'] = {}
params['rco150z0']['name'] = 'Precipitation duration'
params['rco150z0']['units'] = 'min'
params['rco150z0']['description'] = 'Precipitation duration; ten minutes total'
params['rco150z0']['short_name'] = 'precip_dur'

params['htoauts0'] = {}
params['htoauts0']['name'] = 'Snow depth auto'
params['htoauts0']['units'] = 'cm'
params['htoauts0']['description'] = 'Snow depth (automatic measurement); current value'
params['htoauts0']['short_name'] = 'snow_depth_auto'

params['hto000s0'] = {}
params['hto000s0']['name'] = 'Snow depth'
params['hto000s0']['units'] = 'cm'
params['hto000s0']['description'] = 'Snow depth; current value'
params['hto000s0']['short_name'] = 'snow_depth'

params['hns000sw'] = {}
params['hns000sw']['name'] = 'Fresh snow SYNOP'
params['hns000sw']['units'] = 'cm'
params['hns000sw']['description'] = 'SYNOP: fresh snow'
params['hns000sw']['short_name'] = 'fresh_snow_synop'

params['hto000sw'] = {}
params['hto000sw']['name'] = 'Snow depth SYNOP'
params['hto000sw']['units'] = 'cm'
params['hto000sw']['description'] =  'SYNOP: Snow depth'
params['hto000sw']['short_name'] = 'snow_depth_synop'
