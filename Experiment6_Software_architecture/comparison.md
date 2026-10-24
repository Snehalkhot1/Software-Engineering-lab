
# Experiment 6: Software Architecture Design

## Aim
To design and compare different software architectures using
a Student Management System.

## Architectures Implemented

1. Monolithic Architecture
2. Layered Architecture
3. Client-Server Architecture

## Comparison Table

| Parameter | Monolithic | Layered | Client-Server |
|---|---|---|---|
| Structure | One combined application | Separate logical layers | Client and server communicate |
| Code organization | Simple, combined | Organized by responsibility | Divided between client and server |
| Communication | Function calls | Calls between layers | HTTP requests and responses |
| Complexity | Low for small projects | Medium | Medium |
| Maintenance | Can become difficult as it grows | Easier to modify individual layers | Client and server can be maintained separately |
| Network required | No | No, in this implementation | Local HTTP connection |
| Main advantage | Simple to develop and run | Separation of concerns | Supports multiple remote clients |
| Main limitation | Can become tightly coupled | Requires clear layer boundaries | Requires server availability and network handling |
| Suitable use | Small applications | Structured business applications | Network-based applications |

## Observations

1. Monolithic architecture combines application functions
   in one file and is easy to run for a small project.
2. Layered architecture separates presentation, business
   logic, and data access.
3. Client-server architecture separates the requesting client
   from the server that processes requests.

## Result
The three software architecture styles were implemented
using a Student Management System. Their structure,
communication, maintainability, and limitations were compared.
