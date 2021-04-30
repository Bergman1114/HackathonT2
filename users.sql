CREATE TABLE IF NOT EXISTS useract
(
	user_id VARCHAR(10) PRIMARY KEY NOT NULL,
    user_email TEXT NOT NULL,
    user_name VARCHAR(20) NOT NULL,
    user_password VARCHAR(20) NOT NULL
)

INSERT INTO useract (user_id, user_email, user_name, user_password) VALUES
('1001', 'Shweta@example.com', 'SBaid', 'Pass1'),
('1002', 'Sean@example.com', 'SSmith', 'Pass2'),
('1003', 'Frank@example.com', 'FPalmer', 'Pass3'),
('1004', 'Tex@example.com', 'TLone', 'Pass4')

CREATE TABLE customer
	(
	customer_id TINYINT PRIMARY KEY AUTO_INCREMENT,
	customer_name VARCHAR(20) NOT NULL,
	customer_lname VARCHAR(20) NOT NULL,
	customer_address1 VARCHAR(60) NOT NULL,
	customer_address2 VARCHAR(60) NOT NULL,
	customer_email VARCHAR (20) NOT NULL,
	customer_phone VARCHAR(10) NOT NULL,
	user_id VARCHAR(10) NOT NULL,
	FOREIGN KEY (user_id) REFERENCES useract (user_id) ON UPDATE CASCADE ON DELETE CASCADE
	)
	
SELECT * FROM useract

SELECT * FROM customer