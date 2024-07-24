select *
from {{source('sql_server_dbo','movie_scd2')}}
where _fivetran_active = false -- Historical Versions of Records Only
