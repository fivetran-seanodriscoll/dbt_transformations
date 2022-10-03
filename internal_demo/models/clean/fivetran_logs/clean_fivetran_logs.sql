
with logs as (
    select * from {{source('fivetran_log', 'log')}}
)

select * from logs
