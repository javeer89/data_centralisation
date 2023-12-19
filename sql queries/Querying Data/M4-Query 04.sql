SELECT 
		COUNT (product_quantity) AS numbers_of_sales,
		SUM (product_quantity) AS product_quantity_count,
		CASE
			WHEN sd.store_type LIKE '%Web Portal%' THEN 'Web'
			ELSE 'Offline'
		END as locations
	
FROM	orders_table as ot
INNER JOIN
		dim_store_details as sd
		ON ot.store_code =  sd.store_code

GROUP BY
		locations
ORDER By
		numbers_of_sales ASC

;