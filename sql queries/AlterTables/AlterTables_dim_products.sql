ALTER TABLE dim_products
	ALTER COLUMN "product_price_(£)" 	TYPE FLOAT			USING "product_price_(£)"::double precision,		
	ALTER COLUMN "weight_(kg)"			TYPE FLOAT,		
	ALTER COLUMN "product_code"			TYPE varchar (13),
	ALTER COLUMN "EAN"					TYPE varchar (13),
	ALTER COLUMN "date_added" 			TYPE date,
	ALTER COLUMN "product-uuid"			TYPE uuid			USING "product-uuid"::uuid,
--	ALTER COLUMN still_available 		TYPE bool			USING still_available::boolean,
	ALTER COlUMN "weight_class"			TYPE varchar (14),
	
	ALTER COLUMN "still_available" 	set data type boolean
							using case
									when "still_available" = 'Still_available' 	then true
									when "still_available" = 'Removed' 			then false
							end;
	;

SELECT *
FROM dim_products;
