WITH full_purchase AS (
    SELECT
    dim_p.membership_id
    ,ft.item_id
    ,ft.item_count
    ,dim_i.item_cost
    ,ft.item_count * dim_i.item_cost AS item_total_cost

    FROM ft_purchase ft
        INNER JOIN dim_purchase dim_p ON ft.purchase_id = dim_p.id

        LEFT JOIN dim_item dim_i ON ft.purchase_id = dim_i.id
),

member_total_spend AS (
SELECT
 membership_id
,SUM(item_total_cost) sum_spend
FROM full_purchase
GROUP BY 1
)

SELECT
 membership_id
,ROW_NUMBER(sum_spend) OVER(ORDER BY sum_spend DESC) row_num
FROM member_total_spend
WHERE row_num <= 10
;