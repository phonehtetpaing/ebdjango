select
device_type as id,
device_type,
count(t.total_number) as os_family_cnt
from
(
select
    id,
    ip_address,
    device_type,
    count(distinct device_type) as total_number
from
    core_summarylogendusers
where
    vendor_id = {vendor_id}
group by
    id, ip_address, device_type
) as t
group by t.device_type
