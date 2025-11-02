SELECT p_id,p_name,p_city,p_date_open_del,p_date_close_del FROM (
	SELECT p.p_id, p.p_name, p.p_city, p.p_date_open_del, p.p_date_close_del, COUNT(*) AS cnt FROM provider p
	JOIN order_list o ON p.p_id=o.p_id
	JOIN order_line ol ON ol.o_id=o.o_id
	JOIN medicine m ON m.m_id=ol.m_id
	WHERE EXTRACT(YEAR FROM o.o_date)=%s AND m.m_id=%s
	GROUP BY p.p_id
	ORDER BY cnt DESC, p.p_name
	LIMIT 1
) t