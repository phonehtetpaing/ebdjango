select
os_family as id,
os_family,
count(t.total_number) as os_family_cnt
from
(
select
    id,
    ip_address,
    os_family,
    count(distinct os_family) as total_number
from
    core_summarylogendusers
where
    vendor_id = {vendor_id}
group by
    id, ip_address, os_family
) as t
group by t.os_family