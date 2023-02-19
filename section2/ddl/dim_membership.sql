CREATE TABLE dim_membership
(
     id SERIAL PRIMARY KEY
    ,create_ts TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP()
    ,update_ts TIMESTAMP NULL DEFAULT NULL
    ,first_name VARCHAR(30) NOT NULL
    ,last_name VARCHAR(30) NOT NULL
    ,email VARCHAR(50) NOT NULL
    ,date_of_birth DATE NOT NULL
    ,mobile_no CHAR(8) NOT NULL
    ,CHECK (create_ts < update_ts)
)

CREATE UNIQUE INDEX U_IX_email ON dim_membership(email);
CREATE UNIQUE INDEX U_IX_mobile_no ON dim_membership(mobile_no);