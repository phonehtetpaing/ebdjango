select
	id,
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
    group by end_user_id, log_dt
    order by log_dt desc
    )
 and
     vendor_id = {vendor_id}
group by id, message_block_id
order by message_block_id
