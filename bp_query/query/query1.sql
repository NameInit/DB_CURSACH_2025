SELECT m.m_id, m.m_name, COUNT(*) AS cnt FROM order_line ol
JOIN medicine m ON ol.m_id=m.m_id 
JOIN order_list o ON ol.o_id=o.o_id
WHERE EXTRACT(YEAR FROM o.o_date)=%s AND EXTRACT(MONTH FROM o.o_date)=%s 
GROUP BY m.m_id
ORDER BY cnt DESC;