CREATE TABLE ft_purchase
(
     id SERIAL PRIMARY KEY
    ,create_ts TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP()
    ,update_ts TIMESTAMP NULL DEFAULT NULL
    ,purchase_id INT NOT NULL
    ,item_id INT NOT NULL
    ,item_count SMALLINT NOT NULL
    ,item_param JSON NULL
    ,CHECK (create_ts < update_ts)
    ,FOREIGN KEY (purchase_id) REFERENCES dim_purchase(id)
    ,FOREIGN KEY (item_id) REFERENCES dim_item(id)
    ,CHECK (item_count > 0)
)