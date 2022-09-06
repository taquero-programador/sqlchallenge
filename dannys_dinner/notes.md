# dannys dinner `sqlite` 

## Crear y relacionar tablas

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
***
### 1. Cuál es la cantidad total que gastó cada cliente?
### Consulta
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
***
### 2. Cuántos días ha visitado cada cliente el restaurant?
### Consulta
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
***
### 3. Cuál fue el primer artículo comprado por cada cliente?
### Consulta
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
### Respuesta:
Customer|Date_pursh|Name_product
-- | -- | --
A|2021-01-01|curry
A|2021-01-01|sushi
B|2021-01-01|curry
C|2021-01-01|ramen
***
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
***
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
	customer_id as Customer,
	product_name as "Product name",
	or_count as "Popular foo"
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
***
### 6. Primer artículo comprado por el cliente después de ser miembro?
### Consulta
```sql
WITH after_member as(
SELECT
	a.customer_id,
	b.product_name,
	c.join_date,
	a.order_date,
	dense_rank() over(partition by a.customer_id order by a.order_date) rank
FROM sales a
LEFT JOIN menu b ON(a.product_id=b.product_id)
LEFT JOIN members c ON(a.customer_id=c.customer_id)
WHERE a.order_date > c.join_date
)
SELECT
	customer_id as Customer,
	join_date as "Member from",
	product_name as "Product name",
	order_date as "Date Purchased"
FROM
	after_member
WHERE rank=1
```
### Respuesta:
Customer|Member from|Product name|Date Purchased
-- | -- | -- | --
A|2021-01-07|ramen|2021-01-10
B|2021-01-09|sushi|2021-01-11
***
### 7. Qué artículo compro el cliente antes de ser miembro?
### Consulta
```sql
WITH before_member as(
SELECT
	a.customer_id,
	b.product_name,
	c.join_date,
	a.order_date,
	dense_rank() over(partition by a.customer_id order by a.order_date) rank
FROM sales a
LEFT JOIN menu b ON(a.product_id=b.product_id)
LEFT JOIN members c ON(a.customer_id=c.customer_id)
WHERE a.order_date < c.join_date
)
SELECT
	customer_id as Customer,
	join_date as "Member from",
	product_name as "Product name",
	order_date as "Date Purchased"
FROM
	before_member
WHERE rank=1
```
### Respuesta:
Customer|Member from|Product name|Date Purchased
--| -- | -- | --
A|2021-01-07|sushi|2021-01-01
A|2021-01-07|curry|2021-01-01
B|2021-01-09|curry|2021-01-01
C|2021-01-10|ramen|2021-01-01
C|2021-01-10|ramen|2021-01-01
***
### 8. Total de artículos y cantidad gastada por cliente antes de ser miembro?
### Consulta
```sql
SELECT
	a.customer_id as Customer,
	count(a.product_id) as "Total articles",
	sum(b.price) as "Total amount"
FROM sales a
LEFT JOIN menu b ON(a.product_id=b.product_id)
LEFT JOIN members c ON(a.customer_id=c.customer_id)
WHERE a.order_date < c.join_date
GROUP BY a.customer_id
```
### Respuesta:
Customer|Total articles|Total amount
-- | -- | --
A|2|25
B|3|40
C|3|36
***
### 9. Si cada $1 gastado equivales a 10 puntos y el sushi tiene el doble de puntos. Cuánto tendría cada cliente?
### Consulta
```sql
SELECT
	a.customer_id as Customer,
	sum(b.points) as Points
FROM sales a
LEFT JOIN (
	SELECT *,
		CASE product_id
			WHEN 1 THEN price*20
			ELSE price*10
		END points
	FROM menu
) b on(a.product_id=b.product_id)
GROUP BY a.customer_id
```
### Respuesta:
Customer|Points
-- | --
A|860
B|940
C|360
***
### 10.
***
### Referencia de relaciones con sqlalchemy
### Uno a muchos
La tabla hija tendra una columna con un ForeignKey que hara referencia a la principal.
En la tabla padre se coloca `relationship()` como referencía a una colección de elementos de la tabla hija.
```python
class Parent(Base):
    __tablename__ = "parent"

    id = Column(Integer, primary_key=True)
    children = relationship("Child")


class Child(Base):
    __tablename__ = "child"

    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey("parent.id"))
```
### Bidireccional uno a muchos y muchos a uno.
En ambas tablas se establece `relationship()` con back_populate como argumento adicional, el cual hace referencía a la tabla actual.
Se puede usar `backref`.
```python
class Parent(Base):
    __tablename__ = "parent"

    id = Column(Integer, primary_key=True)
    children = relationship("Child", back_populate="parent")


class Child(Base):
    __tablename__ = "child"

    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey("parent.id"))
    parent = relationship("Parent", back_populate="child")
```
### 
