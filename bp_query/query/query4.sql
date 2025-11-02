SELECT p.* FROM provider p
LEFT JOIN order_list o ON o.p_id=p.p_id
WHERE o.o_id IS NULL