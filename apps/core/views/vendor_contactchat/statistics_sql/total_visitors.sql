select
t.id,
count(t.ip_address) as visitor_cnt
from
(
select
	id as id,
    ip_address,
    count(distinct ip_address) as visitor_cnt,
    DATE_FORMAT(log_dt, '%%w') as log_day
from
    core_summarylogendusers
where
	vendor_id = {vendor_id}
group by
	id, ip_address, log_day
) as t

