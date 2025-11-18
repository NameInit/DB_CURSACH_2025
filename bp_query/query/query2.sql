SELECT p.p_id, p.p_name, SUM(o.o_cost) AS summa  FROM order_list o
JOIN provider p ON o.p_id=p.p_id
WHERE EXTRACT(YEAR FROM o.o_date)=%s AND EXTRACT(MONTH FROM o.o_date)=%s 
GROUP BY p.p_id
ORDER BY summa DESC;