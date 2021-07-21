SELECT
  level,
  date_parse(time,'%Y-%m-%d %H:%i:%s') as log_dt,
  json_extract_scalar(user, '$.vendor_user_id') AS vendor_user_id,
  json_extract_scalar(request, '$.device_type') AS device_type,
  json_extract_scalar(request, '$.device_family') AS device_family,
  json_extract_scalar(request, '$.os_family') AS os_family,
  json_extract_scalar(request, '$.os_version') AS os_version,
  json_extract_scalar(request, '$.browser_family') AS browser_family,
  json_extract_scalar(request, '$.browser_version') AS browser_version,
  json_extract_scalar(request, '$.ip_address') AS ip_address,
  json_extract_scalar(request, '$.server_ip_address') AS server_ip_address,
  json_extract_scalar(request, '$.status_code') AS status_code,
  json_extract_scalar(request, '$.content_type') AS content_type,
  json_extract_scalar(request, '$.http_referer') AS http_referer,
  json_extract_scalar(request, '$.action_type') AS action_type,
  json_extract_scalar(request, '$.params') AS params,
  json_extract_scalar(request, '$.endpoint') AS endpoint
FROM {logs_db}.app_log
WHERE json_extract_scalar(user, '$.end_user_id')  is null
