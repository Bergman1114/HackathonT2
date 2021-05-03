CREATE TABLE customer
(
	customer_id TINYINT PRIMARY KEY AUTO_INCREMENT,
	customer_fname VARCHAR(20) NOT NULL,
	customer_lname VARCHAR(20) NOT NULL,
	customer_address1 VARCHAR(60) NOT NULL,
	customer_state VARCHAR(60) NOT NULL,
	customer_email VARCHAR (20) NOT NULL,
	customer_phone VARCHAR(10) NOT NULL,
	user_id VARCHAR(10) NOT NULL,
	FOREIGN KEY (user_id) REFERENCES usertype (user_id) ON UPDATE CASCADE ON DELETE CASCADE
)


INSERT INTO customer (customer_fname, customer_lname, customer_address1, customer_state, customer_email, customer_phone,user_id) VALUES
	('Shweta', 'Baid', 'Main St,Chantilly', 'VA', 'awesome@gmail.com', '553987650','sbaid'),
	('Bryan','Berg','Rainbow St,Ashbun','VA','berg001@gmail.com','327988778','bb001'),
	('Mohanad','Khalaf','Down St,Richmond','VA','mk501@gmail.com','443337645','mkhalaf'),
	('Dunieski', 'Otano','1234 SW 4th Ave Miami','FL' ,'example@example.com','234567890','dunieski')

SELECT *  FROM customer

DELETE FROM customer

CREATE TABLE usertype 
 	(
	user_id VARCHAR(10) PRIMARY KEY,
	user_type VARCHAR(10) NOT NULL
 	)
 	
INSERT INTO usertype (user_id,user_type) VALUES
	('sbaid','buyer'),
	('bb001','buyer'),
	('mkhalaf','seller'),
	('dunieski','buyer')
	
SELECT *  FROM usertype
	
		

CREATE TABLE orders
	(
	order_id TINYINT PRIMARY KEY AUTO_INCREMENT,
	customer_id TINYINT NOT NULL,
	product_id SMALLINT NOT NULL,
	order_notes VARCHAR(25) NOT NULL,
	order_discountedprice DECIMAL(9,2) NOT NULL,
	order_taxpercentage DECIMAL(9,2) NOT NULL,
	order_taxamount DECIMAL(9,2) NOT NULL,
	order_totalprice DECIMAL(9,2) NOT NULL,
	FOREIGN KEY (customer_id) REFERENCES customer (customer_id) ON UPDATE CASCADE ON DELETE CASCADE
	)
	
SELECT *  FROM orders

DELETE FROM orders WHERE order_id = 2

CREATE TABLE products
	(	
	product_id SMALLINT PRIMARY KEY AUTO_INCREMENT,
	product_make VARCHAR(10) NOT NULL,
	product_model VARCHAR(10) NOT NULL,
	product_year VARCHAR(10) NOT NULL,
	product_color VARCHAR(10) NOT NULL,
	product_price DECIMAL(9,2) NOT NULL,
	product_status VARCHAR(10) NOT NULL
	)

	
INSERT INTO products (product_make, product_model, product_year, product_color, product_price, product_status ) VALUES
	('BMW', 'X5', '2020', 'black', 42999.00, 'A'),
	('BMW','X5','2019', 'white', 42999.00, 'A'),
 	('Mercedes', 'S-Class', '2019','black', 101001.00, 'A'),
	('Mercedes', 'S-Class', '2018','white', 101001.00, 'A'),
 	('Toyota', 'Highlander', '2021', 'black',38000.00, 'A'),
	('Toyota', 'Highlander', '2020', 'white',38000.00, 'A'),
 	('Honda', 'Accord','2017','black', 29010.00, 'A'),
 	('Honda', 'Accord','2018','white', 29010.00, 'A'),
	('Nissan', 'Murano', '2020', 'black',32000.00, 'A'),	
 	('Nissan', 'Murano', '2017', 'white',32000.00, 'A')
 
 SELECT *  FROM products
 
 SELECT *  FROM products where product_status = 'A'
 
 DELETE FROM products
 
 DELETE FROM products WHERE product_id = 2