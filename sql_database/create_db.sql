CREATE DATABASE AirportRecords;

USE AirportRecords;

CREATE TABLE flight_info (
    id SERIAL PRIMARY KEY, 
    departure VARCHAR(25) NOT NULL, 
    arrival VARCHAR(25) NOT NULL, 
    duration INTEGER NOT NULL
);

insert into flight_info (departure, arrival, duration) values ('Rechka', 'Na Kae', '812');
insert into flight_info (departure, arrival, duration) values ('Guifões', 'Saint Petersburg', '079');
insert into flight_info (departure, arrival, duration) values ('Kujung', 'Pyrgetós', '449');
insert into flight_info (departure, arrival, duration) values ('Ragay', 'Troitsk', '854');
insert into flight_info (departure, arrival, duration) values ('Santiago', 'Austin', '873');
insert into flight_info (departure, arrival, duration) values ('Madison', 'Jeżów', '445');
insert into flight_info (departure, arrival, duration) values ('Nūrābād', 'Gubengairlangga', '638');
insert into flight_info (departure, arrival, duration) values ('Shiyu', 'Nizhniy Bestyakh', '249');
insert into flight_info (departure, arrival, duration) values ('Fenghui', 'Eldoret', '156');
insert into flight_info (departure, arrival, duration) values ('Villa Alemana', 'Campos Novos', '886');


commit;



# DONE!
