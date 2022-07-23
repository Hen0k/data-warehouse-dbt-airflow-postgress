# data-warehouse-dbt-airflow-postgress

A data-warehouse built for the pNEUMA open dataset of naturalistic trajectories of half a million vehicles collected by a swarm of drones in a congested downtown area of Athens, Greece.

## About the data

For each .csv file the following apply:
– each row represents the data of a single vehicle
– the first 10 columns in the 1st row include the columns’ names
(**track_id**; **type**; **traveled_d**; **avg_speed**; **lat**; **lon**; **speed**; **lon_acc**; **lat_acc**; **time**)
– the first 4 columns include information about the trajectory like the unique trackID, the type of vehicle, the distance traveled in meters and the average speed of the vehicle in km/h
– the last 6 columns are then repeated every 6 columns based on the time frequency. For example, column_5 contains the latitude of the vehicle at time column_10, and column­­­_11 contains the latitude of the vehicle at time column_16.
– Speed is in km/h, Longitudinal and Lateral Acceleration in m/sec2 and time in seconds.

## Acknowledgement

Data source: pNEUMA – [open-traffic.epfl.ch](https://www.google.com/url?q=http://open-traffic.epfl.ch&sa=D&ust=1598884463327000&usg=AFQjCNF55kUX-00yiJbzlPzZhbgY2R4cfg)

Airflow-with-docker-setup: [Medium blog](https://towardsdatascience.com/setting-up-apache-airflow-with-docker-compose-in-5-minutes-56a1110f4122) by [Marvin Lanhenke](https://medium.com/@marvinlanhenke)