

  create  table "pneuma"."public"."longest_traveling_distance_veh_dbt_model copy__dbt_tmp"
  as (
    

with source_data as (

    select * from vehicles where traveled_distance>200

)

select *
from source_data
  );