CREATE TABLE ciudades(
		id serial PRIMARY KEY
		, descripcion varchar(60) UNIQUE
	);

CREATE TABLE public.paises (
	id serial NOT NULL,
	descripcion varchar(60) NOT NULL,
	CONSTRAINT paises_unique UNIQUE (descripcion),
	CONSTRAINT paises_pk PRIMARY KEY (id)
);


