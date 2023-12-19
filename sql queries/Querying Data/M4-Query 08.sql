SELECT
		ROUND (CAST (SUM(pd."product_price_(£)" * ot.product_quantity) as numeric), 2)	as total_sales,
		store_type,
		country_code

FROM 	dim_store_details as sd
INNER JOIN
		orders_table as ot
		USING (store_code)
INNER JOIN
		dim_products as pd
		USING (product_code)

WHERE 	country_code LIKE 'DE'

GROUP BY
		store_type, country_code
ORDER BY
		total_sales ASC