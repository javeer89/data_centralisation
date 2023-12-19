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

SELECT 
		year,
			(
				CAST(
					LEAD ((CONCAT(year,'/', month,'/', day, ' ', timestamp)),1)
					OVER ( ORDER BY year ASC, month ASC, day ASC, timestamp) AS timestamp )
			)-(
				CAST(CONCAT(year,'/', month,'/', day, ' ', timestamp) AS timestamp)
			)
			as difference

FROM dim_date_times

ORDER BY year ASC, month ASC, day ASC, timestamp

*/


 -- figure out differences in timestamp between these orders(transactions) and then group them by year

/*


CAST(CONCAT(year,'/', month,'/', day, ' ', timestamp) AS timestamp)
			as transaction,
		
		CAST(
			LEAD ((CONCAT(year,'/', month,'/', day, ' ', timestamp)),1)
			OVER ( ORDER BY year ASC, month ASC, day ASC, timestamp) AS timestamp )
			as next_transaction

SELECT
		year,
		AVG(
			CAST(
				concat(	'"  hours": ',					EXTRACT(HOUR 			FROM (timestamp)),		', ',
						'"  minutes": ',				EXTRACT(MINUTE 			FROM (timestamp)),		', ',		  
						'"  seconds": ',		round(	EXTRACT(SECOND 			FROM (timestamp)),2),	', ',
						'"  milliseconds": ',	round(	EXTRACT(MILLISECONDS 	FROM (timestamp)),2),	', '
				)
			)
		)
		as actual_time_taken

FROM dim_date_times
GROUP BY
		year

ORDER BY
		year ASC

ALTER TABLE dim_date_times
	ADD COLUMN difference VARCHAR NOT NULL;

UPDATE dim_date_times SET difference = (
				CAST(
					LEAD ((CONCAT(year,'/', month,'/', day, ' ', timestamp)),1)
					OVER ( ORDER BY year ASC, month ASC, day ASC, timestamp) AS timestamp )
			)-(
				CAST(CONCAT(year,'/', month,'/', day, ' ', timestamp) AS timestamp)
			);
 ALTER TABLE dim_date_times
 ALTER COLUMN difference SET NOT NULL;


*/