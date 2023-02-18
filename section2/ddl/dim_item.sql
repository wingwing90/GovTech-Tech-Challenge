CREATE TABLE dim_item
(
     id INT PRIMARY KEY
    ,create_ts TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP()
    ,update_ts TIMESTAMP NULL DEFAULT NULL
    ,item_name VARCHAR(50) NOT NULL
    ,manufacturer_name VARCHAR(50) NOT NULL
    ,cost NUMERIC(8,2) NOT NULL
    ,weight NUMERIC(5,2) NOT NULL
    ,param JSON NULL
    ,CHECK (create_ts < update_ts)
    ,UNIQUE INDEX (item_name)
)
;

CREATE UNIQUE INDEX U_IX_item_name ON dim_item(item_name)
;