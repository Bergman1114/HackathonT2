CREATE TABLE products
(	
	product_id SMALLINT PRIMARY KEY AUTO_INCREMENT,
	product_make VARCHAR(15) NOT NULL,
	product_model VARCHAR(10) NOT NULL,
	product_year VARCHAR(10) NOT NULL,
	product_color VARCHAR(10) NOT NULL,
	product_price DECIMAL(9,2) NOT NULL
)

Insert INTO products (product_make, product_model, product_year, product_color, product_price) Values
('BMW', 'X5', '2020', 'black', '42999.00'),
('BMW','X5','2020', 'white', '42999.00'),
('Mercedes_Benz', 'S-Class', '2020','black', '101001.00'),
('Mercedes_Benz', 'S-Class', '2020','white', '101001.00'),
('Toyota', 'Highlander', '2021', 'black','38000.00'),
('Toyota', 'Highlander', '2021', 'white','38000.00'),
('Honda', 'Accord','2020','black', '29010.00'),
('Honda', 'Accord','2020','white', '29010.00'),
('Nissan', 'Murano', '2020', 'black','32000.00'),	
('Nissan', 'Murano', '2020', 'white','32000.00')

SELECT * FROM products