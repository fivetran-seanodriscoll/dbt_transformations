
with accounts as (
    select * from {{source('salesforce_sandbox', 'account')}}
)

select * from accounts
