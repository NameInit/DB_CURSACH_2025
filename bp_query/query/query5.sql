SELECT p.* FROM provider p
LEFT JOIN (SELECT * FROM order_list o WHERE EXTRACT(YEAR FROM o.o_date)=%s AND EXTRACT(MONTH FROM o.o_date)=%s) o ON o.p_id=p.p_id
WHERE o.o_id IS NULL