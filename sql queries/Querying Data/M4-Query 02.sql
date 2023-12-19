SELECT locality,
	COUNT (*)
	FROM dim_store_details
	GROUP BY locality
	ORDER BY count DESC
	LIMIT 7