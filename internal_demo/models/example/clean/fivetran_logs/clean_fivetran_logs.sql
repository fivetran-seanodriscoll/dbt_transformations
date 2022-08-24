
with logs as (
    select * from {{source('fivetran_logs', 'log')}}
)

select * from logs
