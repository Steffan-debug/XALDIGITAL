SELECT a.nombre_aeropuerto, COUNT(*) AS total_movimientos
FROM data_steffan.VUELOS v
JOIN data_steffan.AEROPUERTOS a ON v.id_aeropuerto = a.id_aeropuerto
GROUP BY a.nombre_aeropuerto
ORDER BY total_movimientos DESC;

SELECT a.nombre_aerolinea, COUNT(*) AS total_vuelos
FROM data_steffan.VUELOS v
JOIN data_steffan.AEROLINEAS a ON v.id_aerolinea = a.id_aerolinea
GROUP BY a.nombre_aerolinea
ORDER BY total_vuelos DESC;

SELECT dia, COUNT(*) AS total_vuelos
FROM data_steffan.VUELOS
GROUP BY dia
ORDER BY total_vuelos DESC;


SELECT a.NOMBRE_AEROLINEA as Aerolinea, v.DIA, COUNT(*) as Vuelos
FROM data_steffan.VUELOS v
JOIN data_steffan.AEROLINEAS a ON v.ID_AEROLINEA = a.ID_AEROLINEA
GROUP BY a.NOMBRE_AEROLINEA, v.DIA
HAVING COUNT(*) > 2;