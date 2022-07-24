# data-warehouse-dbt-airflow-postgress-redash

[![Contributors][contributors-shield]][contributors-url][![Forks][forks-shield]][forks-url][![Stargazers][stars-shield]][stars-url][![Issues][issues-shield]][issues-url][![MIT License][license-shield]][license-url][![LinkedIn][linkedin-shield]][linkedin-url]

A data-warehouse built for the pNEUMA open dataset of naturalistic trajectories of half a million vehicles collected by a swarm of drones in a congested downtown area of Athens, Greece.

## About the data

The data is initially a video feed of drones tracking different vehicles on the road. Then this was turned into a trajectory describing format. In our data the vehicles are described with 4 columns, and the trajectories are described with 6 repeating columns that change with approximately 4 second time interval.

For each .csv file the following apply:

- each row represents the data of a single vehicle
- the first 10 columns in the 1st row include the columns’ names
(**track_id**; **type**; **traveled_d**; **avg_speed**; **lat**; **lon**; **speed**; **lon_acc**; **lat_acc**; **time**)
- the first 4 columns include information about the trajectory like the unique trackID, the type of vehicle, the distance traveled in meters and the average speed of the vehicle in km/h
- the last 6 columns are then repeated every 6 columns based on the time frequency. For example, column_5 contains the latitude of the vehicle at time column_10, and column­­­_11 contains the latitude of the vehicle at time column_16.
- Speed is in km/h, Longitudinal and Lateral Acceleration in m/sec2 and time in seconds.

## Installation

## Roadmap

- [x] Create the data extraction and loading module
- [x] Containerize the module
- [x] Run Airflow in a container
- [x] Modify the compose file to use multiple database users
- [x] Create an Airflow DAG with a DockerOperator
- [x] Test that the workflow actually populates the containerized database
- [x] Locally install dbt
- [x] Connect dbt to the db and run models
- [x] Install and connect Redash
- [x] Create sample visualization
- [x] Containerized Redash with the rest
- [ ] Run dbt models as Airflow DAGs
- [ ] Generate dbt docs with Airflow
- [ ] Containerized dbt with the rest
- [ ] Create a dev, staging, and production area for the database.

## Acknowledgement

- Data source: pNEUMA – [open-traffic.epfl.ch](https://www.google.com/url?q=http://open-traffic.epfl.ch&sa=D&ust=1598884463327000&usg=AFQjCNF55kUX-00yiJbzlPzZhbgY2R4cfg)

- Airflow-with-docker-setup: [Medium blog](https://towardsdatascience.com/setting-up-apache-airflow-with-docker-compose-in-5-minutes-56a1110f4122) by [Marvin Lanhenke](https://medium.com/@marvinlanhenke)

- Airflow-DockerOperator-with-dockercompose: [Medium blog](https://towardsdatascience.com/using-apache-airflow-dockeroperator-with-docker-compose-57d0217c8219) by [Flávio Clésio](https://flavioclesio.medium.com/)

- [Multiple-users-postgres_docker-image](https://hub.docker.com/r/lmmdock/postgres-multi)

- [proper-mounting-volumes-in-DockerOperators](https://stackoverflow.com/questions/64947706/mounting-directories-using-docker-operator-on-airflow-is-not-working)

- [Redash easy installation instruction][redash-install-blog]
- [Redash basics][redash-basics]

## Contributors

![Contributors list](https://contrib.rocks/image?repo=Hen0k/data-warehouse-dbt-airflow-postgress)
[Henok Tilaye][my-profile]

Made with [contrib.rocks](https://contrib.rocks).

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/Hen0k/data-warehouse-dbt-airflow-postgress.svg?style=for-the-badge
[my-profile]: https://github.com/Hen0k
[contributors-url]: https://github.com/Hen0k/data-warehouse-dbt-airflow-postgress/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Hen0k/data-warehouse-dbt-airflow-postgress.svg?style=for-the-badge
[forks-url]: https://github.com/Hen0k/data-warehouse-dbt-airflow-postgress/network/members
[stars-shield]: https://img.shields.io/github/stars/Hen0k/data-warehouse-dbt-airflow-postgress.svg?style=for-the-badge
[stars-url]: https://github.com/Hen0k/data-warehouse-dbt-airflow-postgress/stargazers
[issues-shield]: https://img.shields.io/github/issues/Hen0k/data-warehouse-dbt-airflow-postgress.svg?style=for-the-badge
[issues-url]: https://github.com/Hen0k/data-warehouse-dbt-airflow-postgress/issues
[license-shield]: https://img.shields.io/github/license/Hen0k/data-warehouse-dbt-airflow-postgress.svg?style=for-the-badge
[license-url]: https://github.com/Hen0k/data-warehouse-dbt-airflow-postgress/blob/master/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/henok-tilaye-b18840151/
[redash-install-blog]: https://www.techrepublic.com/article/how-to-deploy-redash-data-visualization-dashboard-help-docker/
[redash-basics]: https://hevodata.com/learn/redash/
