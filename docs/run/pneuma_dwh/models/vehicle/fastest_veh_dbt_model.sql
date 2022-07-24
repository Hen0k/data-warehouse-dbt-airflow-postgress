
  create view "pneuma"."public"."fastest_veh_dbt_model__dbt_tmp" as (
    

with source_data as (

    select * from vehicles where avg_speed>40

)

select *
from source_data
  );