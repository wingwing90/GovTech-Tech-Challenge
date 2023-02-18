WITH item_count AS(
SELECT
     ft.item_id
    ,SUM(item_count) total_item_count
FROM ft_purchase
GROUP BY 1
)

SELECT
item_id
,ROW_NUMBER(total_item_count) OVER(ORDER BY total_item_count DESC) row_num
FROM item_count
WHERE row_num <= 3
;