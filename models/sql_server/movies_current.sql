select *
from {{source('sql_server_dbo','movie_scd2')}}
where _fivetran_active = true -- Current Versions of Records Only
