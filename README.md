# Loader.io Variables

This repository stores **variable data used for load testing** with [Loader.io](https://loader.io). The files are consumed by Loader.io test configurations to vary requests (e.g., different event IDs, zip codes, or join paths) during load tests.

## Why this repo is public

**The repository must be public** so that Loader.io can fetch the variable files over the network. Loader.io does not support private repositories for variable sources; keeping this repo public is required for the service to access it.

## Contents

| File | Description |
|------|-------------|
| **zipcode-and-event-id.json** | Variable sets of `event_id` and `zipcode` used in load tests (larger set). |
| **zipcode-and-event-id-2026.json** | Same structure as above; subset of `event_id` and `zipcode` most up to date for 2026. |
| **loaderio-variables.json** | Variable set of `join_path` values (join URLs with IDs and tokens). |
| **us-city-zips.json** | Variable set of `city_zipcode` (US city zip codes). |
| **genzipcodes.py** | Python script that uses the `zipcodes` package to generate zip code data (zip code, state, lat, long) as JSON. |

## Usage

1. In Loader.io, configure your test to use a **variable file** and point it to the raw URL of the desired JSON file in this repo (e.g. GitHub/GitLab “raw” URL).
2. Ensure this repository is **public** so Loader.io can access that URL.
