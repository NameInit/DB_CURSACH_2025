SELECT m.m_id, m.m_name, COUNT(*) AS cnt FROM order_line ol
JOIN medicine m ON ol.m_id=m.m_id 
JOIN order_list o ON ol.o_id=o.o_id
WHERE EXTRACT(YEAR FROM o.o_date)=2024 AND EXTRACT(MONTH FROM o.o_date)=1 
GROUP BY m.m_id
ORDER BY cnt DESC;

SELECT p.* FROM storage s
JOIN medicine m ON m.m_id=s.m_id
JOIN order_line ol ON ol.m_id=m.m_id
JOIN order_list o ON o.o_id=ol.o_id
JOIN provider p ON p.p_id=o.p_id
WHERE EXTRACT(YEAR FROM o.o_date)=%s AND EXTRACT(MONTH FROM o.o_date)=%s AND m.m_id=%s
ORDER BY s.s_cost DESC
LIMIT 1;