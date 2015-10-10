drop table if exists areas;
create table areas (
  id integer primary key autoincrement,
  notam text not null,
  text text not null
);