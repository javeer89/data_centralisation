ALTER TABLE orders_table
	ADD --CONSTRAINT		FK_Order_Date
		FOREIGN KEY 	(date_uuid)
			REFERENCES 		dim_date_times (date_uuid),

	ADD --CONSTRAINT		FK_Orders_Users
		FOREIGN KEY		(user_uuid)
			REFERENCES 		dim_users (user_uuid),
/*
	ADD --CONSTRAINT		FK_Orders_Card
		FOREIGN KEY		(card_number)
			REFERENCES 		dim_card_details (card_number),
*/
	ADD --CONSTRAINT		FK_Orders_Store
		FOREIGN KEY		(store_code)
			REFERENCES 		dim_store_details (store_code),
	
	ADD --CONSTRAINT		FK_Orders_Product
		FOREIGN KEY		(product_code)
			REFERENCES 		dim_products (product_code);


	
SELECT *
FROM orders_table;
