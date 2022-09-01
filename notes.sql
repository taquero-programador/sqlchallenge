# dannys dinner
# sqlite
# crear y realacionar tablas

sqlite3 dinner.db

DROP TABLE IF EXISTS members;

CREATE TABLE IF EXISTS members(
    customer_id varchar(i) PRIMARY KEY NOT NULL UNIQUE,
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
