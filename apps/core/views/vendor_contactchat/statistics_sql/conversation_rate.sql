select
	id,
    end_user_id,
    message_block_id,
--     message_progress,
    SUBSTRING_INDEX(message_progress, '/', 1) as progress_numerator,
    SUBSTRING_INDEX(message_progress, '/', -1) as progress_denominator
from core_summarylogendusers
where id in (
	select
		max(id)
	from core_summarylogendusers
    where
        message_block_id is not null
        and
        vendor_id = {vendor_id}
        and
        message_block_id = {message_block_id}
    group by end_user_id, log_dt
    order by log_dt desc
    )
order by message_block_id


