SELECT m.m_id AS id, m.m_name AS name, m.m_group AS group, m_country_manufacturer AS country, s.s_cost AS price FROM storage s
JOIN medicine m ON m.m_id=s.m_id
WHERE m.m_id=%s;