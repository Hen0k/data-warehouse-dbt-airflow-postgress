
  create view "pneuma"."public"."longest_traveling_distance_veh_dbt_model__dbt_tmp" as (
    

with source_data as (

    select * from vehicles where traveled_distance>400

)

select *
from source_data
  );