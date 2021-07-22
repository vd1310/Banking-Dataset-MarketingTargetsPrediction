
CREATE TABLE public.bank (
    index bigint primary key,
    age integer,
    job text,
    marital text,
    education text,
    "default" boolean,
    balance double precision,
    housing boolean,
    loan boolean,
    contact text,
    day integer,
    month text,
    duration integer,
    campaign integer,
    pdays integer,
    previous integer,
    poutcome text,
    y boolean
);