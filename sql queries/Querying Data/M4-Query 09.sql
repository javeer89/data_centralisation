select  event_dates.year, 		  
    concat('"hours": ',EXTRACT(hours FROM  avg(event_dates.time_diff)),' ',
		   '"minutes": ',EXTRACT(minutes FROM  avg(event_dates.time_diff)),' ',		  
		   '"seconds": ',round(EXTRACT(seconds FROM  avg(event_dates.time_diff)),2),' '		  
--		   '"milliseconds": ',round(mod(EXTRACT(seconds FROM  avg(dim_date_times.time_diff))*1000,1000)),' '		  
		  ) as actual_time_taken
		 		  
 from event_dates
group by event_dates.year
order by avg(event_dates.time_diff) desc