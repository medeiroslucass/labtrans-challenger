-- View para consulta agrupada dos resultados
CREATE VIEW IF NOT EXISTS resultados_agrupados AS
SELECT r.highway, r.km, r.item,
       COUNT(CASE WHEN r.item = 'Buraco' THEN 1 END) AS buraco,
       COUNT(CASE WHEN r.item = 'Remendo' THEN 1 END) AS remendo,
       COUNT(CASE WHEN r.item = 'Trinca' THEN 1 END) AS trinca,
       COUNT(CASE WHEN r.item = 'Placa' THEN 1 END) AS placa,
       COUNT(CASE WHEN r.item = 'Drenagem' THEN 1 END) AS drenagem
FROM Results r
GROUP BY r.highway, r.km, r.item;