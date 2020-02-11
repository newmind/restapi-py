CREATE DATABASE esport;
USE esport;

create table tournament
(
    id          int auto_increment     primary key,
    title       varchar(100)           not null,
    gameName    varchar(100)           not null,
    playerCount int unsigned default 0 not null,
    location    varchar(100)           not null,
    address     varchar(100)           null,
    startAt     datetime               null,
    endAt       datetime               null
);

