CREATE TABLE bank (
    index bigint,
    age integer,
    job text,
    marital text,
    education text,
    "default" boolean,
    balance double precision,
    housing boolean,
    loan boolean,
    campaign integer,
    pdays integer,
    previous integer,
    poutcome text,
    y boolean,
    pdays_bool boolean,
    PRIMARY KEY(index)
);


CREATE TABLE contact (
    index bigint,
    contact text,
    day integer,
    month text,
    duration integer,
    PRIMARY KEY(index),
    CONSTRAINT fk_bank
        FOREIGN KEY(index)
            REFERENCES bank(index)
);