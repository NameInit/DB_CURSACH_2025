SELECT iu.id, iu.login, iu.password, r.r_id, r.r_role, r.r_db_config FROM internal_user iu
JOIN role r ON r.r_id=iu.r_id
WHERE iu.login=%s AND iu.password=%s;