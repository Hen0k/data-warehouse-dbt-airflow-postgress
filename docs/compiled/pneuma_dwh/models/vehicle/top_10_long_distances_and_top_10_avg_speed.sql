


-- with fast_veh as (

--     select *

--     from vehicles 
    
--     order by 
--         avg_speed DESC
        
    
-- )
with longest_distance as (
    select *

        from "pneuma"."public"."longest_traveling_distance_veh_dbt_model" 
        
        order by 
            traveled_distance DESC
)

SELECT *
FROM 
longest_distance