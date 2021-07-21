select
t.id,
t.log_day,
count(t.end_user_id) as weekly_visitor_cnt
from
(
select
	id as id,
    end_user_id,
    count(distinct end_user_id) as weekly_visitor_cnt,
    DATE_FORMAT(log_dt, '%%w') as log_day
from
    core_summarylogendusers
where
	log_dt >= (CURRENT_DATE - interval WEEKDAY(CURRENT_DATE) day) - interval 1 day
    and
    log_dt < (CURRENT_DATE - interval WEEKDAY(CURRENT_DATE) day) + interval 5 day
    and
    vendor_id = {vendor_id}
group by
	id, end_user_id, log_day
) as t
group by id, t.log_day
order by t.log_day