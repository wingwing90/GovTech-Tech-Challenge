CREATE TYPE ENUM_payment_method AS ENUM ('Credit Card', 'PayNow', 'Grab Pay')
;

CREATE TABLE dim_purchase
(
     id SERIAL PRIMARY KEY
    ,create_ts TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP()
    ,update_ts TIMESTAMP NULL DEFAULT NULL
    ,membership_id INT NOT NULL
    ,payment_method ENUM_payment_method
    ,FOREIGN KEY (membership_id) REFERENCES dim_membership(id)
)