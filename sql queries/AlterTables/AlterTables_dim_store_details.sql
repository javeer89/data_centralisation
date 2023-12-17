ALTER TABLE dim_store_details 
	ALTER COLUMN longitude			TYPE FLOAT    		USING longitude::double precision,	
	ALTER COLUMN locality 			TYPE varchar (255),
	ALTER COLUMN store_code 		TYPE varchar (12),
	ALTER COLUMN opening_date		TYPE date			USING opening_date::date,
	ALTER COLUMN staff_numbers 		TYPE smallint 		USING staff_numbers::smallint,
	ALTER COLUMN store_type		 	TYPE varchar (255),
	ALTER COLUMN latitude			TYPE FLOAT    		USING latitude::double precision,
	ALTER COLUMN country_code 		TYPE varchar (2),
	ALTER COLUMN continent	 		TYPE varchar (255);

SELECT *
FROM dim_store_details;
