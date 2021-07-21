select
	id,
    DATE_FORMAT(log_dt, '%%w') as log_day,
    log_dt,
    sum(SUBSTRING_INDEX(message_progress, '/', 1)) as progress_numerator,
    sum(SUBSTRING_INDEX(message_progress, '/', -1)) as progress_denominator,
    100 * sum(SUBSTRING_INDEX(message_progress, '/', 1)) / sum(SUBSTRING_INDEX(message_progress, '/', -1)) as conversion_rate
from core_summarylogendusers
where id in (
	select
		max(id)
	from core_summarylogendusers
    where
        message_block_id is not null
    group by end_user_id
    order by log_dt desc
    )
and
	log_dt >= (CURRENT_DATE - interval WEEKDAY(CURRENT_DATE) day) - interval 1 day
    and
    log_dt < (CURRENT_DATE - interval WEEKDAY(CURRENT_DATE) day) + interval 5 day
    and
    vendor_id = {vendor_id}
group by id, log_day
order by message_block_id
