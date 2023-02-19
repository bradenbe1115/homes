# homes

This repo serves as the main ingest & load engine for the AirBnB data project. Each extractor is treated as it's own microservice and housed within this repo. If at a later time it makes sense for one or more of the microservices to be treated as their own project, they will be rolled out of this repo. The current plan is for each microservice to run as a lambda function in AWS and push up ingested data to a S3 bucket.

## Directories

## ./foundation

Each subdirectory is related to a specific data source. Within each sub-directory is a common folder to house API wrappers or web scrapers that can be used across source specific lambda functions
