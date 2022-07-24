

with source_data as (

    select * from vehicles where traveled_distance>200

)

select *
from source_data