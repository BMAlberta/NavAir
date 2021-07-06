# NavAir

The goal of NavAir is to provide aviation enthusiasts with a variety of information around airspaces and airports. 

While many applications exist today, I wanted to provide a way to source the data (freely) and build a cohesive Mobile experience.

This repo serves as the start of the API layer for the project. The UI, is forthcoming.

# Data Elements
The following data elements are aggregated and provided in a simple "Airport" object:
- Airport list
    - List of runways for a given airport
- Weather information
- METARs
    - Raw and Decoded
- TAFs
    - Raw and Decoded
- NOTAMs
    - Most recent
    - Historical

## Airports
A sample airport object:
```

  "airports": {
    {
      "icao": "KCMH",
      "name": "John Glenn International Airport",
      "type": "large_airport",
      "lat": "39.998001",
      "lon": "-82.891899",
      "elevation": 815,
      "continent": "NA",
      "country": "US",
      "municipality": "Columbus",
      "region": "US-OH",
      "runways": {
        {
          "id": "10R",
          "elevation": "816",
          "length": "10000"
        },
        {
          "id": "10L",
          "elevation": "823",
          "length": "12500"
        }
      }
    },
    {
      "icao": "KOSU",
      "name": "The Ohio State University Airport",
      "type": "large_airport",
      "lat": "39.998001",
      "lon": "-82.891899",
      "elevation": 815,
      "continent": "NA",
      "country": "US",
      "municipality": "Columbus",
      "region": "US-OH",
      "runways": {
        {
          "id": "10R",
          "elevation": "816",
          "length": "10000"
        },
        {
          "id": "10L",
          "elevation": "823",
          "length": "12500"
        }
      }
    }
  }
}
```

# System Architecture
This system consists of primarily 2 parts; a web API and a persistence layer.

## API
Python was selected for the API layer, primarily the Flask micro web framework for it's versatitily and ease of use.

## Persistence Layer
A relational database is being used for this layer. While this data would work well in a no-SQL product, MariaDB is the product of choice.