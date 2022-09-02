# dannys dinner `sqlite` 

## crear y realacionar tablas

```bash
sqlite3 dinner.db
```
```sql
DROP TABLE IF EXISTS members;

CREATE TABLE IF EXISTS members(
    customer_id varchar(1) PRIMARY KEY NOT NULL UNIQUE,
    join_date DATETIME
);

# datos members
INSERT INTO members
  ("customer_id", "join_date")
VALUES
  ('A', '2021-01-07'),
  ('B', '2021-01-09');
```
```sql
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
```
```sql
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
```

# 

### 1. Cuál es la cantidad total que gastó cada cliente?
### consulta
```sql
SELECT
    a.customer_id as Customer,
    count(a.customer_id) as Total_com,
    sum(b.price) as Total_amount
FROM
    sales a
LEFT JOIN
    menu b On (a.product_id = b.product_id)
GROUP BY a.customer_id
ORDER BY Total_amount DESC;
```
### Respuesta:
Customer|Total_com|Total_amount
-- | -- | --
A|6|76
B|6|74
C|3|36

### 2. Cuántos días ha visitado cada cliente el restaurant?
### consulta
```sql
SELECT
    customer_id as Customer,
    COUNT(DISTINCT(order_date)) as Total_visit
FROM
    sales
GROUP BY customer_id
ORDER BY Total_visit DESC;
```
### Respuesta:
Customer|Total_visit
-- | --
B|6
A|4
C|2

### 3. Cuál fue el primer artículo comprado por cada cliente?
### consulta
```sql
WITH f_buy as(
    SELECT
        a.customer_id,
        a.order_date,
        b.product_name,
        dense_rank() over(partition by a.customer_id order by a.order_date)rank
    FROM
        sales a
    LEFT JOIN
        menu b on(a.product_id=b.product_id))
SELECT
    customer_id,
    order_date,
    product_name
FROM
    f_buy
WHERE rank=1
GROUP BY customer_id, product_name
```
### Resuldato:
Customer|Date_pursh|Name_product
-- | -- | --
A|2021-01-01|curry
A|2021-01-01|sushi
B|2021-01-01|curry
C|2021-01-01|ramen

### 4. Cuál es el artículo más comprado y cuantas veces lo compro cada cliente?
### Consulta
```sql
SELECT
    b.product_name as Pname
    count(b.product_name) as More_sale
FROM
    sales a
LEFT JOIN menu b ON(a.product_id=b.product_id)
GROUP BY b.product_name
ORDER BY More_sale DESC
```
### Respuesta:
Pname|More_sale
-- | --
ramen|8
curry|4
sushi|3

### 5. Qué artículo fue más popular por cliente?
### Consulta
```sql
WITH popitems as(
SELECT
	a.customer_id,
	b.product_name,
	count(b.product_name) as or_count,
	dense_rank() over(partition by a.customer_id order by count(b.product_name) DESC) rank
FROM sales a
LEFT JOIN menu b ON(a.product_id=b.product_id)
GROUP BY a.customer_id, b.product_name
)
SELECT
	customer_id,
	product_name,
	or_count
FROM
	popitems
WHERE rank=1
```
### Respuesta:
Customer|Product name|Popular foo
-- | -- | --
A|ramen|3
B|curry|2
B|ramen|2
B|sushi|2
C|ramen|3