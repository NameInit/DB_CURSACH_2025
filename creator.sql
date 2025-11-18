CREATE TABLE role (
    r_id SERIAL PRIMARY KEY,
    r_role VARCHAR(100) NOT NULL,
    r_db_config JSON NOT NULL
);

CREATE TABLE internal_user (
    id SERIAL PRIMARY KEY,
    login VARCHAR(100) NOT NULL,
    password VARCHAR(255) NOT NULL,
    r_id INTEGER NOT NULL,
    CONSTRAINT fk_internal_user_role 
        FOREIGN KEY (r_id) 
        REFERENCES role(r_id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
);


CREATE TABLE provider (
    p_id SERIAL PRIMARY KEY,
    p_name VARCHAR(255) NOT NULL,
    p_city VARCHAR(100) NOT NULL,
    p_date_open_del DATE NOT NULL,
    p_date_close_del DATE
);

CREATE TABLE medicine (
    m_id SERIAL PRIMARY KEY,
    m_name VARCHAR(255) NOT NULL,
    m_group VARCHAR(100) NOT NULL,
    m_name_manufacturer VARCHAR(255) NOT NULL,
    m_country_manufacturer VARCHAR(100) NOT NULL
);

CREATE TABLE storage (
    s_id SERIAL PRIMARY KEY,
    s_count INTEGER NOT NULL,
    s_cost REAL NOT NULL,
    s_date_in DATE NOT NULL,
    m_id INTEGER NOT NULL,
    CONSTRAINT fk_storage_medicine 
        FOREIGN KEY (m_id) 
        REFERENCES medicine(m_id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
);

CREATE TABLE user_order (
    uo_id SERIAL PRIMARY KEY,
    uo_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    u_id INTEGER NOT NULL,
    CONSTRAINT fk_user_order_internal_user 
        FOREIGN KEY (u_id) 
        REFERENCES internal_user(id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
);

CREATE TABLE order_list (
    o_id SERIAL PRIMARY KEY,
    o_date DATE NOT NULL,
    o_cost DECIMAL(10,2) NOT NULL,
    o_count INTEGER NOT NULL,
    p_id INTEGER NOT NULL,
    CONSTRAINT fk_order_list_provider 
        FOREIGN KEY (p_id) 
        REFERENCES provider(p_id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
);

CREATE TABLE order_line (
    ol_d SERIAL PRIMARY KEY,
    ol_count INTEGER NOT NULL,
    o_id INTEGER NOT NULL,
    m_id INTEGER NOT NULL,
    CONSTRAINT fk_order_line_order_list 
        FOREIGN KEY (o_id) 
        REFERENCES order_list(o_id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,
    CONSTRAINT fk_order_line_medicine 
        FOREIGN KEY (m_id) 
        REFERENCES medicine(m_id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
);

CREATE TABLE user_list_order (
    ulo_id SERIAL PRIMARY KEY,
    ulo_amount INTEGER NOT NULL,
    uo_id INTEGER NOT NULL,
    m_id INTEGER NOT NULL,
    CONSTRAINT fk_user_list_order_user_order
        FOREIGN KEY (uo_id) 
        REFERENCES user_order(uo_id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,
    CONSTRAINT fk_user_list_order_medicine
        FOREIGN KEY (m_id) 
        REFERENCES medicine(m_id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
);

CREATE TABLE product_report (
    report_id SERIAL PRIMARY KEY,
    p_month INT NOT NULL,
    p_year INT NOT NULL,
    p_amount INT NOT NULL,
    p_value INT NOT NULL
);


-- Заполнение таблицы provider
INSERT INTO provider (p_id, p_name, p_city, p_date_open_del, p_date_close_del) VALUES
(1, 'Фармакор', 'Москва', '2020-01-15', NULL),
(2, 'Медпоставка', 'Санкт-Петербург', '2019-03-20', NULL),
(3, 'Аптечный склад', 'Новосибирск', '2021-07-10', '2023-12-31'),
(4, 'Фармацевтические системы', 'Екатеринбург', '2018-11-05', NULL),
(5, 'Медицинские товары', 'Казань', '2022-02-28', NULL),
(6, 'Здоровье плюс', 'Ростов-на-Дону', '2020-09-12', NULL),
(7, 'Аптека 36.6', 'Владивосток', '2019-12-01', '2024-01-15'),
(8, 'Фармация', 'Краснодар', '2021-04-18', NULL);

-- Заполнение таблицы medicine
INSERT INTO medicine (m_id, m_name, m_group, m_name_manufacturer, m_country_manufacturer) VALUES
(1, 'Парацетамол', 'Жаропонижающие', 'Фармстандарт', 'Россия'),
(2, 'Ибупрофен', 'Противовоспалительные', 'Берлин-Хеми', 'Германия'),
(3, 'Амоксициллин', 'Антибиотики', 'Синтез', 'Россия'),
(4, 'Аспирин', 'Анальгетики', 'Байер', 'Германия'),
(5, 'Лоратадин', 'Антигистаминные', 'Гедеон Рихтер', 'Венгрия'),
(6, 'Метформин', 'Противодиабетические', 'Тева', 'Израиль'),
(7, 'Аторвастатин', 'Гиполипидемические', 'Пфайзер', 'США'),
(8, 'Омепразол', 'Ингибиторы протонной помпы', 'АстраЗенека', 'Великобритания');

-- Заполнение таблицы storage
INSERT INTO storage (s_id, s_count, s_cost, s_date_in, m_id) VALUES
(1, 150, 25.50, '2024-01-10', 1),
(2, 80, 45.75, '2024-01-12', 2),
(3, 200, 120.00, '2024-01-15', 3),
(4, 300, 15.25, '2024-01-18', 4),
(5, 120, 85.40, '2024-01-20', 5),
(6, 90, 65.30, '2024-01-22', 6),
(7, 60, 210.75, '2024-01-25', 7),
(8, 180, 95.60, '2024-01-28', 8);

-- Заполнение таблицы order_list
INSERT INTO order_list (o_id, o_date, o_cost, o_count, p_id) VALUES
(1, '2024-02-01', 25500.00, 1000, 1),
(2, '2024-02-03', 18300.00, 400, 2),
(3, '2024-02-05', 48000.00, 200, 3),
(4, '2024-02-07', 15250.00, 1000, 4),
(5, '2024-02-10', 34160.00, 400, 5),
(6, '2024-02-12', 19590.00, 300, 6),
(7, '2024-02-15', 42150.00, 200, 7),
(8, '2024-02-18', 57360.00, 600, 8);

-- Заполнение таблицы order_line
INSERT INTO order_line (ol_d, ol_count, o_id, m_id) VALUES
(1, 500, 1, 1),
(2, 200, 1, 2),
(3, 300, 1, 3),
(4, 400, 2, 4),
(5, 200, 3, 5),
(6, 300, 4, 6),
(7, 200, 5, 7),
(8, 600, 6, 8),
(9, 150, 7, 1),
(10, 250, 8, 2);

SELECT * FROM product_report
WHERE p_year = 2024 AND p_month = 2

SELECT EXTRACT(MONTH FROM o_date) AS p_month, EXTRACT(YEAR FROM o_date) AS p_year, SUM(o_cost) AS p_amount, COUNT(*) AS p_value FROM order_list
GROUP BY o_date

SELECT * FROM order_line

CREATE OR REPLACE PROCEDURE report1(input_year INTEGER, input_month INTEGER)
AS $$
DECLARE
    month_amount DECIMAL(10,2);
    month_value INTEGER;
    report_exists BOOLEAN;
BEGIN
    SELECT EXISTS(
        SELECT 1 FROM product_report 
        WHERE p_year = input_year AND p_month = input_month
    ) INTO report_exists;

    IF report_exists THEN
        RAISE NOTICE 'ERROR: Report is exists';
        RETURN;
    END IF;

    SELECT 
        COALESCE(SUM(o_cost), 0),
        COALESCE(COUNT(*), 0)
    INTO month_amount, month_value
    FROM order_list
    WHERE 
        EXTRACT(YEAR FROM o_date) = input_year AND 
        EXTRACT(MONTH FROM o_date) = input_month;

    INSERT INTO product_report (p_month, p_year, p_amount, p_value)
    VALUES (input_month, input_year, month_amount, month_value);

    RAISE NOTICE 'SUCCESS: Report created';
END;
$$ LANGUAGE plpgsql;