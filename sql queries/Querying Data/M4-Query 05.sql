SELECT 	
		sd.store_type as store_type,
		ROUND 	(CAST
			   		(SUM(product_quantity * pd."product_price_(£)") as numeric), 2)
		as total_sales,
		
		ROUND 	(CAST
					(SUM(100*product_quantity*pd."product_price_(£)")/
					(SUM(SUM(product_quantity*pd."product_price_(£)")) over()) as numeric), 2 )
		as "percentage_total(%)"


FROM 	orders_table as ot
INNER JOIN
		dim_store_details as sd
		USING (store_code)
INNER JOIN
		dim_products as pd
		USING (product_code)
GROUP BY
		sd.store_type
ORDER BY
		total_sales DESC
;