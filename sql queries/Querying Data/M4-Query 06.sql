SELECT
		ROUND (CAST
			   	(sum(product_quantity * dp."product_price_(£)") as numeric),2)
		AS total_sales,
		dt.year,
		dt.month

FROM	orders_table AS ot
INNER JOIN
		dim_date_times AS dt
		ON ot.date_uuid =  dt.date_uuid
INNER JOIN
		dim_products AS dp
		ON ot.product_code = dp.product_code

GROUP BY
		dt.month,dt.year
ORDER BY
		total_sales DESC
LIMIT	10
;

