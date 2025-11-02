SELECT iu.id, iu.name, iu.password, r.r_id, r.r_role, r.r_db_config FROM internal_user iu
JOIN role r ON r.r_id=iu.r_id
WHERE iu.name=%s AND iu.password=%s;