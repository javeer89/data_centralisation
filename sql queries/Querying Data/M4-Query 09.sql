SELECT	
		sub_table.year,
		concat(	'"  hours": ',					EXTRACT(HOUR 			FROM (AVG(difference))),		', ',
				'"  minutes": ',				EXTRACT(MINUTE 			FROM (AVG(difference))),		', ',		  
				'"  seconds": ',		round(	EXTRACT(SECOND 			FROM (AVG(difference))),2),	', ',
				'"  milliseconds": ',	round(	EXTRACT(MILLISECONDS 	FROM (AVG(difference))),2),	', '
		)
		as actual_time_taken
--		AVG(difference) as diff
FROM	(
		SELECT
			year, month, day,
			timestamp,
			(
				CAST(
					LEAD ((CONCAT(year,'/', month,'/', day, ' ', timestamp)),1)
					OVER ( ORDER BY year ASC, month ASC, day ASC, timestamp) AS timestamp )
			)-(
				CAST(CONCAT(year,'/', month,'/', day, ' ', timestamp) AS timestamp)
			)
			as difference
		FROM dim_date_times
		) sub_table

GROUP BY sub_table.year
ORDER BY actual_time_taken DESC
;
/*
IF YOU WANT TO GET SIMILAR DISPLAY AS ON THE COURSE PROJECT PAGE, YOU CAN TRUNCATE THE RESULTS AND LIMIT THEM.
ALSO, 2022 VALUES ARE DIFFERENT. POSSIBLY DUE TO UPDATED ENTRIES.
*/