select
browser_family as id,
browser_family,
count(t.total_number) as browser_family_cnt
from
(
select
    id,
    ip_address,
    browser_family,
    count(distinct browser_family) as total_number
from
    core_summarylogendusers
where
    vendor_id = {vendor_id}
group by
    id, ip_address, browser_family
) as t
group by t.browser_family