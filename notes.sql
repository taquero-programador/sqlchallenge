# dannys dinner
# sqlite
# crear y realacionar tablas

sqlite3 dinner.db

DROP TABLE IF EXISTS members;

CREATE TABLE IF EXISTS members(
    customer_id varchar(1) PRIMARY KEY NOT NULL UNIQUE,
    join_date DATETIME
);

# datos memebers
INSERT INTO members
  ("customer_id", "join_date")
VALUES
  ('A', '2021-01-07'),
  ('B', '2021-01-09');

# -------------------------------------------------------------------

DROP TABLE IF EXISTS menu 

CREATE TABLE IF EXISTS menu(
    product_id INTEGER PRIMARY KEY NOT NULL UNIQUE,
    product_name varchar(10),
    price INTEGER NOT NULL
);

# valores para menu
INSERT INTO menu
  ("product_id", "product_name", "price")
VALUES
  ('1', 'sushi', '10'),
  ('2', 'curry', '15'),
  ('3', 'ramen', '12');

# -------------------------------------------------------------------

DROP TABLE IF EXISTS sales;

CREATE TABLE IF EXISTS sales(
    customer_id varchar(1) NOT NULL,
    order_date DATE NOT NULL,
    product_id INTEGER NOT NULL,
    FOREIGN KEY(customer_id) REFERENCES members(customer_id),
    FOREIGN KEY(product_id) REFERENCES menu(product_id)
);

# insertar datos en sales

INSERT INTO sales
  ("customer_id", "order_date", "product_id")
VALUES
  ('A', '2021-01-01', '1'),
  ('A', '2021-01-01', '2'),
  ('A', '2021-01-07', '2'),
  ('A', '2021-01-10', '3'),
  ('A', '2021-01-11', '3'),
  ('A', '2021-01-11', '3'),
  ('B', '2021-01-01', '2'),
  ('B', '2021-01-02', '2'),
  ('B', '2021-01-04', '1'),
  ('B', '2021-01-11', '1'),
  ('B', '2021-01-16', '3'),
  ('B', '2021-02-01', '3'),
  ('C', '2021-01-01', '3'),
  ('C', '2021-01-01', '3'),
  ('C', '2021-01-07', '3');

# -------------------------------------------------------------------
# 1. Cuál es la cantidad total que gastó cada cliente?
# consulta
SELECT
    a.customer_id as Customer,
    count(a.customer_id) as Total_com,
    sum(b.price) as Total_amount
FROM
    sales a
LEFT JOIN menu b On (a.product_id = b.product_id)
GROUP BY a.customer_id
ORDER BY Total_amount DESC;
# Resultado:
Customer|Total_com|Total_amount
A|6|76
B|6|74
C|3|36
# -------------------------------------------------------------------
# 2. Cuántos días ha visitado cada cliente el restaurant?
# consulta
